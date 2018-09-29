class Application:
   
    orders = []

    
    def signup(self, user):
        self.users[user.email] = user

