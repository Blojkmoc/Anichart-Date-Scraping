from flask import Flask, render_template
import time
import web_scrape
import read_pickle
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
events = []
time_now = ''
def load_events():
    global time_now 
    global events
    time_now = time.ctime()
    print(f'{time_now}')
    events.clear()
    web_scrape.run()
    loaded_anime_title = read_pickle.LoadLists('data/anime_title.pickle')
    loaded_episode = read_pickle.LoadLists('data/episode.pickle')
    loaded_countdown = read_pickle.LoadLists('data/countdown.pickle')
    # loaded_anime_title, loaded_episode, loaded_countdown = web_scrape.run()
    #print(loaded_countdown)
    for i in range(len(loaded_countdown)):
        events.append({
            'title': f'{loaded_anime_title[i]}: {loaded_episode[i]}',
            'start': loaded_countdown[i],
            'end': ''  
        })
load_events()
sched = BackgroundScheduler(daemon=True)
sched.add_job(load_events,'interval',minutes=2)
sched.start()

@app.route('/')
def start():

    return render_template('cal.html',events=events, time_now = time_now)

if __name__ == '__main__':
    
    # load_events()
    # print(events)
    app.run()

    # starttime = time.time()
    # while True:
    #     print('Start Update')
    #     events = []
    #     web_scrape.run()
    #     load_events()
    #     print('End Update')
    #     time.sleep(60.0 - ((time.time() - starttime) % 60.0))   