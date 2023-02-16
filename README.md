# Anichart-Date-Scraping
This repository was created based on my personal hobby of Japanese anime and manga. I was intrigued by Anichart website and wanted to try on my side if I can scrape some
useful information about the seasonal anime that are airing currently

This repo thus uses the following Python libraries to help the cause:
- BeautifulSoup4
- Playwright
- Flask

This app is only applicable on the personal computer and for some reason, it does not work when I try to host it on an Azure Web App.

It uses Flask to host the website as it scrapes for useful information and these data is then shown on a calendar using fullCalendar.io
