class User:

    def __init__(self, user_id, name, username):
        print("New User Being Created....")
        self.id = user_id
        self.name = name
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001" ,"Shivam Vijaykumar Gupta" ,"shivamrvgupta")
user_2 = User("002" ,"Nimisha Nitin Joshi" ,"nimishannjoshi")
print(user_2.name)

user_1.follow(user_2)
# user_2.follow(user_1)

print(user_2.followers)
print(user_1.following)
