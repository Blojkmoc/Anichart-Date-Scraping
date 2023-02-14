from flask import Flask, render_template
import time
import web_scrape
import read_pickle

app = Flask(__name__)
events = []
def load_events():
    # loaded_anime_title = read_pickle.LoadLists('data/anime_title.pkl')
    # loaded_episode = read_pickle.LoadLists('data/episode.pkl')
    # loaded_countdown = read_pickle.LoadLists('data/countdown.pkl')
    loaded_anime_title, loaded_episode, loaded_countdown = web_scrape.run()
    for i in range(len(loaded_countdown)):
        events.append({
            'title': f'{loaded_anime_title[i]}: {loaded_episode[i]}',
            'start': loaded_countdown[i],
            'end': ''  
        })


@app.route('/')
def start():
    return render_template('cal.html',events=events)

if __name__ == '__main__':
    
    load_events()
    print(events)
    app.run(debug=True, port=5000)

    # starttime = time.time()
    # while True:
    #     print('Start Update')
    #     events = []
    #     web_scrape.run()
    #     load_events()
    #     print('End Update')
    #     time.sleep(60.0 - ((time.time() - starttime) % 60.0))   