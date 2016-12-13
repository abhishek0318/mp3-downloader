# MP3 Downloader

This program written in python 3.5 takes in name of song and downloads it. This is done by first fetching the URL of first corresponding YouTube result and then using the URL to download the mp3 file with help [KeepVid.com]("https://keepvid.com"). 

## Getting Started

To run and test the program you need to install python 3 from the [official link]("https://www.python.org/downloads/").

### Prerequisites

To run the program, you need to install Beautiful Soup 4, Requests, Wget module. Do this by running the following commands in cmd or the terminal.
```
pip install beautifulsoup4
```
```
pip install requests 
```
```
pip install wget 
```

### Runnning the program

#### Windows
* To use the program in Windows just double the .py file.
* A prompt asking you for the name of the song will come up.

    ```
    Enter the name of song :
    ```

* Enter the name of the song and the mp3 file will be downloaded to the same directory.

#### Linux
* To run the program open the terminal and navigate to the folder the python file is in.
* Type the following in the terminal

    ```
    python3 MusicDownloader.py
    ```

* A prompt asking you for the name of the song will come up.

  ```
    Enter the name of song :
    ```

* Enter the name of the song and the mp3 file will be downloaded to the same directory.


## Built With

* Python 3.5
* Beautful Soup
* Requests
* Wget

## Contributing

You are free to contribute to this project.

## Authors

* **Abhishek Sharma** - *Initial work*

See also the list of [contributors](https://github.com/abhishek0318/mp3-downloader/graphs/contributors) who participated in this project.

