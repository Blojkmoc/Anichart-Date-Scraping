from flask import Flask, render_template
import time
import web_scrape
import read_pickle
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
events = []
def load_events():
    events.clear()
    web_scrape.run()
    loaded_anime_title = read_pickle.LoadLists('data/anime_title.pkl')
    loaded_episode = read_pickle.LoadLists('data/episode.pkl')
    loaded_countdown = read_pickle.LoadLists('data/countdown.pkl')
    # loaded_anime_title, loaded_episode, loaded_countdown = web_scrape.run()
    for i in range(len(loaded_countdown)):
        events.append({
            'title': f'{loaded_anime_title[i]}: {loaded_episode[i]}',
            'start': loaded_countdown[i],
            'end': ''  
        })

sched = BackgroundScheduler(daemon=True)
sched.add_job(load_events,'interval',minutes=2)
sched.start()

@app.route('/')
def start():
    # events.clear()
    # web_scrape.run()
    # load_events()
    #print(events)
    return render_template('cal.html',events=events)

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