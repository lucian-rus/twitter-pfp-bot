import requests
import replies as rep
import apimanager as tw
import twitter
import time

# function that loops until finds a media reply to the user's tweet
def loop():
    data = rep.get_tweet_data()

    # checks if the 'tweets.json' file size is 0, if so, loops until something is written inside the file
    while len(data) == 0:
        
        # checks if there is a reply every 3 seconds
        time.sleep(3)
        data = rep.get_tweet_data()

        print('number of replies is still ' + str(len(data)))

    # returns the name of the user that replied and the media url
    for name, likes, url in data[:1]:
        print('found a url: ' + url)
        return name, url

# generates the image from the media url and returns the name of the user that replied
def generate_data():
    name, url = loop()
    with open('..\\resources\\pic.jpg', 'wb') as handler:
        
        print(url)
        res = requests.get(url)
        if not res.ok:
            print(res)

        for block in res.iter_content(1024):
            if not block:
                break
            handler.write(block)

    return name