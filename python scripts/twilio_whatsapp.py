from twilio.rest import Client

# imported credentials from myCredentials file which has some sensitive info so wouldn't upload thta file , you considered this as a placeholder of your all credentials
from myCredentials import account_sid, auth_token, my_cellno, my_twilio

# passed in all credentials to twilio Client 
client = Client(account_sid, auth_token) 

# message that you want to send
my_msg = 'Hello World! This is my first mssg through twilio dummy text dummy text dummy text dummy text dummy text dummy text dummy text'

mssg = client.messages.create(to = my_cellno, from_ = my_twilio, body = my_msg)
