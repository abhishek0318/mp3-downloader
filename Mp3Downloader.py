import requests
from bs4 import BeautifulSoup
import wget

def fetch_first_result(Query):
	"""
	Returns the URL of first youtube video corresponding to the query.
	"""
	SearchResultURL = 'https://www.youtube.com/results?search_query=' + Query.replace(' ', '+')
	SearchResultHTML = requests.get(SearchResultURL).text
	SearchResultSoup = BeautifulSoup(SearchResultHTML, 'html.parser')
	VideoURL = SearchResultSoup.find('a', class_='yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link ').get('href')
	VideoURL = 'https://www.youtube.com' + VideoURL
	return VideoURL

def download_mp3_file(VideoURL):
	"""
	Downloads mp3 file from a YouTube Video URL
	"""
	KeepVidURL = "http://keepvid.com/?url=" + VideoURL
	KeepVidHTML = requests.get(KeepVidURL).text
	KeepVidSoup = BeautifulSoup(KeepVidHTML, 'html.parser')
	Text = KeepVidSoup.find(text = " M4A - 128 kbps ")
	DownloadLink = Text.parent.parent.get('href')
	FileName = KeepVidSoup.h3.string[:40] + ".mp3"
	wget.download(DownloadLink, FileName)

Query = input("Enter the name of song : ")
download_mp3_file(fetch_first_result(Query))
