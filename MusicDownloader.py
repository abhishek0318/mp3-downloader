import requests
from bs4 import BeautifulSoup
import wget
import sys
import os

def fetch_first_result(Query):
	"""
	Returns the URL of first youtube video corresponding to the query.
	"""
	SearchResultURL = 'https://www.youtube.com/results?search_query=' + Query.replace(' ', '+')
	SearchResultHTML = requests.get(SearchResultURL).text
	SearchResultSoup = BeautifulSoup(SearchResultHTML, 'html.parser')
	try:
		VideoURL = SearchResultSoup.find('a', class_='yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link ').get('href')
	except AttributeError:
		print("Couldn't find song!")
		sys.exit()
	VideoURL = 'https://www.youtube.com' + VideoURL
	return VideoURL

def download_mp3_file(VideoURL):
	"""
	Downloads mp3 file from a YouTube Video URL
	"""
	KeepVidURL = "http://keepvid.com/?url=" + VideoURL
	KeepVidHTML = requests.get(KeepVidURL).text
	KeepVidSoup = BeautifulSoup(KeepVidHTML, 'html.parser')
	try:
		Text = KeepVidSoup.find(text = " M4A - 128 kbps ")
	except AttributeError:
		print("Error downloading mp3 file!")
		sys.exit()
	DownloadLink = Text.parent.parent.get('href')
	FileName = ' '.join(KeepVidSoup.h3.string.split()[:6]) + ".m4a"
	print("Downloading {FN}..".format(FN = FileName))
	try:
		wget.download(DownloadLink, FileName)
	except KeyboardInterrupt:
		print("\nDownload cancelled.")
		# Deletes partially downloaded file
		for file in os.listdir():
			if file.startswith(FileName):
				os.remove(file)
		sys.exit()
	print("\nDownload completed.")

try:
	Query = input("Enter the name of song : ")
except KeyboardInterrupt:
	print("\nProgram Stopped!")
	sys.exit()
download_mp3_file(fetch_first_result(Query))
