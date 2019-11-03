# Code-With-Mosh-Playlist-Downloader

> Bash/Python Script: A script to download full course from [codewithmosh.com](https://codewithmosh.com), given one has the valid login credentials <br />

### Topics Available:

| 1                | 2                            | 3                                                            |
| ---------------- | ---------------------------- | ------------------------------------------------------------ |
| ReactJS          | NodeJS                       | AngularJS: Beginner to Pro                                   |
| Redux in Angular | Angular4 Crash               | JS: Basics                                                   |
| JS: OOPS         | Complete Python              | Python Developers                                            |
| SQL              | C# Basics                    | C# Intermediate                                              |
| C# Advanced      | C# Xamarin Native Apps       | The Complete ASP.NET MVC 5 Course                            |
| C# Unit test     | Clean Coding and Refactoring | Build a Real-world App with ASP.NET Core 1.0+ and Angular 2+ |

### :pushpin: Aim

- Help those who want to avoid themselves from 'clicks-and-saves'
- To share a mixed-cum-messed-up learning experience (Python, JS, Shell Script etc)
- Would try include a flow graph of events and Progress

### :v: Missions Accomplised:

- Include as many Tutorials as possible
- Implemented using Scraping Module in Python and Bash Scripts

### :eyeglasses: Download Options

- [x] Download Playlist for a specific topic
- [x] Download all Playlists at once (only mentioned Topics)

## :cloud: Installation

#### Prerequisites
- ##### Install Python (Python2, if not installed on the system by default, like Ubuntu 18.04)
```shell
   sudo apt update
   sudo apt install python-pip
   pip --version
```

- ##### Install Beautiful Soup4 (python scraping module)
```shell
   sudo pip install beautifulsoup4 
```
- ##### Install lxml HTML parser
```shell
   sudo pip install lxml
```

#### Basic Steps

1. Clone the Repository and open ./core
2. Open the following files
   - [scrape_list_via_login.py](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/scrape_list_via_login.py)
   - [scrape_via_login.py](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/scrape_via_login.py)
3. Change the login credentials
   - USERNAME (email)
   - PASSWORD
   - SCHOOL_ID (A numerical value found in your URL as you login)
     ```shell
     Sample URL: "https://sso.teachable.com/secure/121212/users/sign_in?clean_login=true&reset_purchase_session=1"
     Here the 121212 represents your SCHOOL_ID
      ```

#### Download a specific Playlist (say NodeJS)

4. Open Topic_list.url
5. Copy the URL of the desired topic (here NodeJS) from [Topic_list.url](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/Topic_list.url)
6. Run

```shell
    chmod 777 ./playlist_downloader.sh
    playlist_downloaded.sh <topic_url> <topic_name>
```
7. A new file named "<topic_name>.txt" will be generated
8. Make a folder and copy the curl_script.sh and <topic_name>.txt to it
9. Run
```shell
   chmod 777 ./curl_script.sh 
   ./curl_script.sh <topic_name>.txt
```
10. This will start the download

#### Download All Playlists Available

4. Run

```shell
    chmod 777 ./full_playlist_downloader.sh
    ./full_playlist_downloader.sh Topic_list.url
```
5. New files named "<topic_name>.txt" will be generated.
   These files will have the content urls for download.
   
6. For each file, that you want the playlist to download, make a folder and copy the curl_script.sh and <topic_name>.txt to it
7. Run
```shell
   chmod 777 ./curl_script.sh 
   ./curl_script.sh <topic_name>.txt
```
8. This will start the download

##### NOTE: The ReactJS playlist consumes upto 17 GB of your total data

##### Other modules can consume upto 35 GB (rough estimate) of your data

##### Recommended to use over Wifi only

## :books: About

> [AboutTheFiles.md](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/AboutTheFiles.md) contains the details about the files used in this module.

## :star2: Issues and Contributions
- Want to contribute and be a part of this small project. Check the simplest contributing guidelines [here](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/CONTRIBUTING.md)
- Contributions don't have to be very special. From 'simple typos' to 'serious bugs' all kinds of contributions are welcome! :smile:

Thanks! :heart:

## :scroll: License

[MIT](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/LICENSE) © [Anshul Garg](https://github.com/garganshul108)
