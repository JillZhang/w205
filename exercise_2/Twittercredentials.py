import tweepy

consumer_key = "5O7d4or6khFOr07uDEy4nMcNf";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret="bAOn4OLWRxgVtcw0RmaBY667bctWj4uaqGFOgHXaTq1OI45cU0";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "	843631973860040712-ulSvFRFkk9JEa2Ujdi2ivoQPKzlZlIz";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret="cK5u2FtO5luSs9Kn1pBbzkGi97ARxdbubwbVtwBygexYo";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



