import tweepy, requests
import win10toast

def init_api():
    # consumer keys provided by the twitter api
    consumer_key    = ''
    consumer_secret = ''

    # access keys provided by the twitter api
    access_token  = ''
    access_secret = ''

    try:
        # give access to the api based on the user keys
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)
    except tweepy.TweepError:
        print('authentication error')

    return api    

# tweets the input alongside the given media
def tweet_media(img, message):
    api  = init_api()

    try:
        api.update_with_media(img, status=message)

    except tweepy.TweepError:
        print('error while updating status')

# tweets the input
def tweet(message):
    api = init_api()

    try:
        api.update_status(message)
    except tweepy.TweepError as e:
        print('error while updating status')
        print(e)

# updates the profile picture based on the input 
def update_profile_pic(img, name):
    api = init_api()
    msg = 'user @' + name + ' updated my profile pic. thank you' 

    try:
        api.update_profile_image(img)
        
        # tweets the name of the user that provided the update and tweets the picture
        api.update_with_media(img, status=msg)

        notify()

        print('someone updated your profile pic')
    except tweepy.TweepError:
        print('error while updating profile picture')

# function that pushes a windows notification when the twitter profile picture has been updated
def notify():
    notifier = win10toast.ToastNotifier()
    title    = 'twitter'
    message  = 'updated profile pic'

    notifier.show_toast(title=title, msg=message, icon_path='..\\resources\\icon\\icon.ico', duration=10, threaded=True)
