from playwright.sync_api import sync_playwright 
from bs4 import BeautifulSoup
import time
import pickle
from datetime import datetime

url = "https://anichart.net/" 
anime_title = []
Episode = []
Countdown = []

def run():
	while len(anime_title)<=0:
		
		with sync_playwright() as p: 
			browser = p.chromium.launch() 
			page = browser.new_page() 
		
			# page.on("response", lambda response: print( 
			# 	"<<", response.status, response.url, "END")) 
			page.goto(url, wait_until="networkidle", timeout=90000) 
			# page.mouse.wheel(horizontally, vertically(positive is 
			# scrolling down, negative is scrolling up)
			for i in range(8): #make the range as long as needed
				page.mouse.wheel(0, 15000)
				time.sleep(1)
				i += 1
			
			time.sleep(1) 
			#print(page.content()) 
		
			content = page.content()
			page.context.close() 
			browser.close()
		soup = BeautifulSoup(content, features="html.parser")
		# # Creating the HTML file
		# file_html = open("page_source.html", "w", encoding='utf-8')
		# file_html.write(str(soup))
		# # Saving the data into the HTML file
		# file_html.close()

		card_elements = soup.find_all("div",class_="media-card")
		for card in card_elements:
			#Title
			overlay = card.find_all("div", class_="overlay")
			for o in overlay:
				title = o.find("a").contents[0]
				title = str(title)
				#print(type(title))
				anime_title.append(title)
			#Episode
			episodes = card.find_all("div",class_="episode")
			for episode in episodes:
				Episode.append(str(episode.text))
			#Countdown
			countdown = card.find_all("div",class_="countdown")
			if len(countdown)==0:
				countdown = card.find_all("div",class_="date")
				for count in countdown:
					try:
						date_object = datetime.strptime(str(count.text), '%B %d, %Y').date()
						#print(type(date_object))
						#print(date_object)  # printed in default format
						date_string = datetime.strftime(date_object, '%Y-%m-%d')
						#print(type(date_string))
						#print(date_string)
					except ValueError:
						date_string = str(count.text)
					
					Countdown.append(date_string)
			
			else:
				time_now = time.time()
				for count in countdown:
					count_string = str(count.text)
					x = count_string.split(", ")
					std_time = time_now
					for j in x:
						seperate = j.split(" ")
						numerator = int(seperate[0])
						if seperate[1] == 'days' or seperate[1] == 'day':
							std_time += 60*60*24*numerator
						elif seperate[1] == 'hours' or seperate[1] == 'hour':
							std_time += 60*60*numerator
						elif seperate[1] == 'mins' or seperate[1] == 'min':
							std_time += 60*numerator
						elif seperate[1] == 'seconds' or seperate[1] == 'second':
							std_time += numerator
					Countdown.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(std_time)))
					#Countdown.append(str(count.text))

		# card_elements = soup.find_all("div", class_="overlay")
		# for card_element in card_elements:
		#     #cover = card_element.find("div", class_="cover")
		#     #overlay = cover.find("div", class_="overlay")
		#     title = card_element.find("a").contents[0]
		#     #print(title, '\n')
		#     anime_title.append(title)
		# #print(anime_title)
		# episodes = soup.find_all("div",class_="episode")
		# for episode in episodes:
		# 	Episode.append(episode.text)
		# countdowns = soup.find_all("div",class_="countdown")
		# for countdown in countdowns:
		# 	Countdown.append(countdown.text)
		# print(anime_title, len(anime_title))
		# print(Episode,len(Episode))
		# print(Countdown,len(Countdown))
		if len(anime_title) > 0:
			#Save to pickle
			# f = open('data/anime_title.pkl', 'wb')
			# pickle.dump(anime_title, f)
			# f = open('data/episode.pkl', 'wb')
			# pickle.dump(Episode, f)
			# f = open('data/countdown.pkl', 'wb')
			# pickle.dump(Countdown, f)
			return anime_title, Episode, Countdown


if __name__ == '__main__':
	run()