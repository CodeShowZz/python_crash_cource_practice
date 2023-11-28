current_users = ['Michael','admin','lin','Anne','Joanna']

new_users = ['michaeL','Boren','Willam','Jony','joanna']

for user in new_users:
    exist = False
    for current_user in current_users:
        if(user.lower() == current_user.lower()):
             exist = True        
    if exist:        
        print(f'the {user} will need to enter a new username')
    else:
        print(f'the {current_user} is available')     
     
  