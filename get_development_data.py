import GetOldTweets3 as got
import pandas as pd
import os
import time


df = pd.read_csv(r'/Users/tom/Desktop/spain_tweets/initial/spain_control_group.csv', parse_dates=True, index_col=0)
diag = pd.read_csv(r'/Users/tom/Desktop/Countries_depressed_usernames/spain_new_dep_usernames.csv', index_col=0)



dest_path = r'/Users/tom/Desktop/spain_tweets/development/control_group_tweets/'
#dest_path=r'/Users/tom/Desktop/spain_tweets/development/diagnosed_depression_tweets/'
#dest_path=r'/Users/tom/Desktop/Italy_tweets/development/diagnosed_depression_tweets/'
#dest_path =r'/Users/tom/Desktop/France_tweets/development/diagnosed_depression_tweets/'
destination = [fname[:-8] for fname in os.listdir(dest_path)]

usernames_to_get= list(set([u for u in list(set(df.username)) if u not in destination]))


#df=pd.read_csv('/Users/tom/Desktop/Countries_depressed_usernames/French_annot_Laura.csv', index_col=0, engine='python')
#df1 = df.where(df['diagnosed']=='yes').dropna(subset=['diagnosed'])

#usernames_to_get = list(set(df1.username.values))


print(len(usernames_to_get))
dates = pd.date_range(start=pd.datetime(2015, 1, 1), end=pd.datetime(2019, 11, 30)).tolist()
d = [days.strftime('%Y-%m-%d') for days in dates]


destination_usernames = list(set([fname[:-8] for fname in os.listdir(dest_path)]))


for i, u in enumerate(usernames_to_get):
    if u not in destination_usernames and i>1400:
        criteria = got.manager.TweetCriteria().setUsername(u).setSince(d[0]).setUntil(d[-1]).setMaxTweets(5000)
        tweets = got.manager.TweetManager.getTweets(criteria)
        ID, username, tweet, date = [], [], [], []
        no_tweets = 0
        for t in tweets:
            ID.append(t.id)
            username.append(t.username)
            tweet.append(t.text)
            date.append(t.date)
            no_tweets+=1
        destination_usernames.append(u)
        if no_tweets > 20:
            done = pd.DataFrame({'Date': pd.Series(date), 'Username': pd.Series(username), 'Tweet': pd.Series(tweet),
                                 'ID': pd.Series(ID)})
            done.to_csv(dest_path+r'/{}_got.csv'.format(u))
        print('Done {}'.format(u), i, 'of:{}'.format(len(usernames_to_get)))
        time.sleep(300)

    else:
        print('rejected: {}, {}'.format(u, i))