from intercom.client import Client 

def createUser(new_id, new_name, new_email):# Define function to create new users
    #intercom = Client(personal_access_token = 'Token') # access token for authorization
    
    for user in intercom.users.all():# iterate through database of current users 
        if user.id != new_id and user.email != new_email: # Check to see if user is in database
            intercom.users.create(id = str(new_id), name = str(new_name), email= str(new_email)) #create new user if not in databse
        else:
            print('User already in database')# alert that user is already in databse



