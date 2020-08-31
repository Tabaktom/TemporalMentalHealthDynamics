import GetOldTweets3 as got
import pandas as pd
import os
import time

#df = pd.read_csv(r'/Users/tom/Desktop/france_tweets/initial/France_exp_group.csv', parse_dates=True)
df = pd.read_csv(r'/Users/tom/Desktop/france_tweets/initial/France_exp_part1.csv', index_col=0)
#destination = [fname[:-8] for fname in os.listdir(r'/Users/tom/Desktop/Development_Depression_Country_A/control_group_tweets')]
#dest2 = [fname[:-8] for fname in os.listdir(r'/Users/tom/Desktop/Development_Depression_Country_A/Diagnosed_Depression_Tweets')]
usernames_to_get= list(set(df.usernames))

print(len(usernames_to_get))
dates = pd.date_range(start=pd.datetime(2019, 12, 1), end=pd.datetime(2020, 5, 15)).tolist()
d = [days.strftime('%Y-%m-%d') for days in dates]

destination_path1 = r'/Users/tom/Desktop/france_tweets/experiment/pre_lockdown_og'
destination_path2 = r'/Users/tom/Desktop/france_tweets/experiment/during_lockdown_og'
destination_usernames1 = [fname[:-8] for fname in os.listdir(destination_path1)]
destination_usernames2 = [fname[:-8] for fname in os.listdir(destination_path1)]
destination_usernames = list(set(destination_usernames1+destination_usernames2))
usernames_to_get = [u for u in usernames_to_get if u not in destination_usernames]
sp = pd.DataFrame({'Username':pd.Series(usernames_to_get)}, index=[ind for ind in range(len(usernames_to_get))])
sp1 = sp[:int(len(sp.index)*0.5)]
sp2 = sp[int(len(sp.index)*0.5):]
sp2.to_csv(r'/Users/tom/Desktop/france_usernames3.csv')
for i, u in enumerate(sp1['Username'].values):
    if u not in destination_usernames:
        criteria = got.manager.TweetCriteria().setUsername(u).setSince(d[0]).setUntil(d[-1]).setMaxTweets(5000)
        tweets = got.manager.TweetManager.getTweets(criteria)
        ID_pre, username_pre, tweet_pre, date_pre = [], [], [], []
        ID, username, tweet, date = [], [], [], []
        no_tweets = 0
        for t in tweets:
            if t.date.strftime('%Y-%m-%d') >= '2020-03-17':
                ID.append(t.id)
                username.append(t.username)
                tweet.append(t.text)
                date.append(t.date)
            else:
                ID_pre.append(t.id)
                username_pre.append(t.username)
                tweet_pre.append(t.text)
                date_pre.append(t.date)
            no_tweets+=1
        if no_tweets > 20:
            done1 = pd.DataFrame({'Date': pd.Series(date_pre), 'Username': pd.Series(username_pre), 'Tweet': pd.Series(tweet_pre),
                                 'ID': pd.Series(ID_pre)})
            done1.to_csv(destination_path1+r'/{}_got.csv'.format(u))
            done2 = pd.DataFrame({'Date': pd.Series(date), 'Username': pd.Series(username), 'Tweet': pd.Series(tweet),
                                 'ID': pd.Series(ID)})
            done2.to_csv(destination_path2+r'/{}_got.csv'.format(u))
        print('Done {}'.format(u), i, 'of:{}'.format(len(sp1['Username'].values)))
        time.sleep(250)

    else:
        print('rejected: {}, {}'.format(u, i))