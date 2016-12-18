class UserAccount :
    """
    A class that models a user account for mega-social-media website, GuessMySecret
    """

    def __init__(self, username_input, password_input, secret_input):
        """
        Initialize the UserAccount object:
        :param username: user name (string)
        :param password: password to gain access to account (string)
        :param secret: user's secret, accessible only with password (string)
        """
  #      print(secret_input)
        self.username = username_input
        #Complete the __init__ method
        self.password = password_input
        
        self.secret = secret_input
  #      print(self.password)
        print(self.secret_input)
        
    def print_secret(self,password_attempt):
        """
        Checks user input, password_attempt - if this matches the user's
        password, then the user's secret is printed to the screen.

        :param password_attempt: guess for the password (string)
        """
        #Complete this method - check the input variable, password_attempt,
        #against the password for this user (the value of the instance variable, password).
        #If, and only if, there's a match, then print the user's secret to the screen.
        print('hi!!!')
##        username=('yazan the cool')
##        password=('somoneyazan15@1')
        
first_user_account = UserAccount('Yazan', 'great', 'im cool')
