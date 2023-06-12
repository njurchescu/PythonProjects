class User:
    # self is the object being created/initialised
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Methods allways need to have a self parameter/it knows the object that called it
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Nick")
user_2 = User("002", "Oana")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
