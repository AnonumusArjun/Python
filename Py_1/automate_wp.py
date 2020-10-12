from twilio.rest import Client 
 
account_sid = 'AC6a20d597927ffbbad36dd79941f60764' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Heya...',      
                              to='whatsapp:+918866910911' 
                          ) 
 
print(message.sid)
