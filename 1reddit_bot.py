import praw
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def get_recepient_email():
    #Reddit API credentials
    reddit = praw.Reddit(
        client_id = os.getenv('client_id'),
        client_secret = os.getenv('client_secret'),
        user_agent = os.getenv('user_agent'),
       
    )
    #print(reddit.read_only)

    #Email credentials
    sender_email = os.getenv('sender_email')
    receiver_email = input('Enter email address to receive notification: ')
    password = os.getenv('password')


    #Subreddit and keyword to monitor
    subreddit_name = ('worldnews')
    keyword = ('israel ')

    #Monitor subreddit for new posts
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.stream.submissions():
    #for submission in subreddit.hot(limit = 10):
        #print(submission.title)

        #Check if the keyword is in the title
        if keyword in submission.title.lower():
            #print(submission.title)
            
            #Prepare email message
            message = MIMEText(f'New post in /r/{subreddit_name} matching keyword `{keyword}`:\n\n{submission.title}\n\n{submission.url}')
            message['Subject'] = (f'New post matching keyword `{keyword}` in /r/{subreddit_name}')
            message['From'] = sender_email 
            message['To'] = receiver_email

            #Send email notification
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, password)
                server.send_message(message)
                return ('Notification email sent')

print(get_recepient_email())                         
                            

            

        
