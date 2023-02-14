import pickle

def LoadLists(file):
    open_file = open(file, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list

loaded_anime_title = LoadLists('data/anime_title.pkl')
loaded_episode = LoadLists('data/episode.pkl')
loaded_countdown = LoadLists('data/countdown.pkl')

# print(f'Anime Title: {loaded_anime_title}, {len(loaded_anime_title)}')
# print(f'Episode: {loaded_episode}, {len(loaded_episode)}')
# print(f'Countdown: {loaded_countdown}, {len(loaded_countdown)}')