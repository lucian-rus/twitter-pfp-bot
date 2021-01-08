# this file handles the main application loop and represents the entry-point 

import json
import time
import apimanager as tw
import loop as it
import os

# this function tweets a new status and saves its id
def get_last_tweet(cnt):
    tweet_str = 'tweet number  ' + str(cnt) + '. this tweet is scripted and the first media reply will change my profile picture #profilepic #script'
    tw.tweet(tweet_str)
    
    client    = tw.init_api()
    client_id = client.me().id
    name      = client.me().screen_name
    
    tweet = client.user_timeline(id = client_id, count = 1)[0]
    id    = tweet.id
    
    print('updated scripted status. waiting for replies')

    return name, id

# writes the tweet data to the 'tweets.json' file 
def write_to_json(cnt):
    name, id = get_last_tweet(cnt)

    data = {}
    user = {}
    user['screen_name'] = name
    
    data['user'] = user 
    data['id']   = id

    with open('..\\resources\\json\\tweets.json', 'w') as out:
        json.dump(data, out)

    # updates the profile picture 
    tw.update_profile_pic('..\\resources\\pic.jpg', it.generate_data())

    cnt = cnt + 1
    return cnt

# main loop of the application. waits 15 minutes to tweet then waits for the reply until tweeting again
def main():
    cnt = write_to_json(1)

    while True:
        print('waiting for the next tweet to occur')
        time.sleep(900)
        cnt = write_to_json(cnt)

# create the json directory 
def setup():
    os.mkdir('..\\resources\\json')
    print('json directory created')

if __name__ == "__main__":
    # check if the json directory exists. if not, create it
    if not os.path.isdir('..\\resources\\json'):
        print('json directory does not exist. creating directory...')
        setup()
    
    main()
