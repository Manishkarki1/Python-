from instabot import Bot
bot=Bot()
bot.login(username="manishkarki",password="")
#To follow anyone
bot.follow("swostikathapa")
#To unfollow anyone
bot.unfollow("bimalshrestha")
#To upload image
bot.upload_photo("#write path",caption="This is my first post")
#To send message to multiple person
bot.send_message("#write message here",["nirdhojkarki","bishalshrestha"])
#To see followers
followers=bot.get_user_followers("manishkarki")
for follower in followers:
    print(bot.get_user_info(follower))
#To see following
following=bot.get_user_following("manishkarki")
for follow in following:
    print(bot.get_user_info(follow))