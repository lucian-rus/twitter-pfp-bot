# twitter-pfp-bot

## <u> About </u> 

This application represent a twitter bot that updates the users profile picture based on the first reply to a given tweet. The scripted tweets are automatically posted to Twitter by the application. To get started you need a valid Twitter API account and your own credentials which can be later exported as environment variables inside the application.

<b> Requirements </b>

* valid Twitter API account alongside a Twitter application
* credentials as mentioned above
* Python 3.8.6 or later

<b> Required libraries </b>

* python-twitter
* tweepy
* requests
* win10toaster

## <u> How it works?</u>

After running the script, your status will be updated and the necessary data will be stored in a Json file called `tweets.json` that will act as the input file for the rest of the application. Every 3 seconds, the scripts will look for media replies to your new status, looping until it finds a fit reply. Based on the `media_url` attribute, a request will be made to download the media file attached to the reply, which will be downloaded in the `resources` file. The application makes an API call to update the profile picture and if there's no error, the profile picture is updated and a new tweet is posted with a message about the user that replied first alongside the new profile picture. The script waits for 15 minutes until tweeting again and the process repeats.

## <u> Notes </u>

Special thanks to [edsu](https://github.com/edsu) for his repository that made getting replies to a tweet way easier. His repository can be found [here](https://gist.github.com/edsu/54e6f7d63df3866a87a15aed17b51eaf).

I look forward to continuing developing this bot to allow more functionality in the future as well as a proper interface. Possible future updates:
* interface
* logging
* user-defined timeframe for tweet frequency