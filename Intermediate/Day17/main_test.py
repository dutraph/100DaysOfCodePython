class User:
    def __init__(self, user_id, username, age):
        self.id = user_id
        self.username = username
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', "Paulo", 32)
user_2 = User('002', "Joyce", 29)

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)
