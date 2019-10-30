# Code-With-Mosh-Playlist-Downloader

> Bash/Python Script: A script to download full course from [codewithmosh.com](https://codewithmosh.com) <br />

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

#### Basic Steps

1. Clone the Repository
2. Open the following files
   - [scrape_list_via_login.py](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/scrape_list_via_login.py)
   - [scrape_via_login.py](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/scrape_via_login.py)
3. Change the login credentials
   - USERNAME (email)
   - PASSWORD
   - SCHOOL_ID (A numerical value found in your URL as you login)

#### Download All Playlists Available

4. Run

```shell
    chmod 777 ./full_playlist_downloader.sh
    ./full_playlist_downloader.sh Topic_list.url
```

#### Download a specific Playlist (say NodeJS)

4. Open Topic_list.url
5. Copy the URL of the desired topic (here NodeJS) from [Topic_list.url](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/Topic_list.url)
6. Run

```shell
    chmod 777 ./playlist_downloader.sh
    playlist_downloaded.sh <topic_url>
```

##### NOTE: The ReactJS playlist consumes upto 17 GB of your total data
##### Other modules can consume upto 35 GB (rough estimate) of your data
##### Recommended to use over Wifi only

## :books: About
> [AboutTheFiles.md](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/AboutTheFiles.md) contains the details about the files used in this module.

Thanks! :heart:

## :scroll: License

[MIT](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/LICENSE) © [Anshul Garg](https://github.com/garganshul108)
