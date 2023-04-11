#PascalCase For ClassesNaming
#camelCase is usedFor not really used
#snake_case used for everything else

class User:
    def __init__(self, id, username, password):
        print("new user being created ...")
        self.id = id
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User(1, "aa", "pass")

user_2 = User(2, "bb", "pass")

user_1.follow(user_2)
print("1 Following: " + str(user_1.following))
print("1 Followers: " + str(user_1.followers))

user_2.follow(user_1)
print("2 Following: " + str(user_1.following))
print("2 Followers: " + str(user_1.followers))






