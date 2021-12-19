# YoutubeAPITest

This is a small project created with the help of [YouTube Data API v3](https://developers.google.com/youtube/v3) , which searches for a query and returns a paginated response

## Features
- Server continuosly stores the reponses for a query term on a MongoDB Collection.
- The GET Request to the API returns a paginated response of the data stored in the collection in a reverse-chronological order.
- The documents in the collection are indexed uniquely

## PROJECT SETUP

#### Basic Requirements
The project requires python to be installed on the system.

This is a Django Project which depends on certain libraries to run. Install the requirements using the requirements.txt file as:

 ```pip install -r requirements.txt```

If prompted, migrate the project:
##### On Windows
```python manage.py migrate ```
##### On Mac/Linux
```python3 manage.py runserver```

#### Add environment variables for the project

Add the following environment variables in a `.env` file under `youtubeAPI/ytapi`
- `YOUTUBE_API_KEY` The Api Key Obtained from Youtube Data API v3
- `YOUTUBE_QUERY_TERM` The Query term that the server will search on the Youtube API
- `MONGO_DB_PORT` - Port for connecting to MongoDB Database
- `MONGO_DB_HOST` - Host for connecting to MongoDB Database
- `SLEEP_INTERVAL` - Interval at which the server refreshes the content of the database

#### Running the application
❗ Make sure that the connection to appropriate MongoDB database is made.
Run the server using
##### On Windows
```python manage.py runserver --noreload```
##### On Mac/Linux
```python3 manage.py runserver --noreload```
❗It is important to run the server in `--noreload` mode

## API usage
The API returns reponse in `JSON` format. It returns top 10 results from the database per page.

#### Query Parameters:
- `page` - gets this page from the results

#### API endpoint
Access the api using the following structure
```http://<host>/?page=<page_number>```
For example, if the server is running on `localhost`, use

```http://localhost:8000/?page=2``` for accessing the second page of the results

- To clear the database record use ``````http://<host>/delete``````

## Example

```
[
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "Pnx9EVv4KUA"
    },
    "title": "எந்த Movie Best?!? | Spiderman No Way Home Vs Pushpa The Rise | Best Movie Public Opinion | CW!",
    "description": "Spider Man No Way Home Vs Pushpa Best Movie Public Opinion by Chennai Waalaa. Spiderman No Way Home Vs Pushpa The ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/Pnx9EVv4KUA/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/Pnx9EVv4KUA/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/Pnx9EVv4KUA/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T13:23:57Z",
    "channel": "Chennai Waalaa"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "tHxulYpLt4k"
    },
    "title": "Jak No Way Home zmienił całe MCU? Wyjaśnienie zakończenia filmu!",
    "description": "Kocham Kino. Jak No Way Home zmienił całe MCU? Wyjaśnienie zakończenia filmu! sklep dla graczy z niesamowitymi ofertami: ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/tHxulYpLt4k/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/tHxulYpLt4k/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/tHxulYpLt4k/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T13:15:43Z",
    "channel": "Kocham Kino"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "Lo0l1iYS0Po"
    },
    "title": "ความรู้สึกหลังดู(ไม่สปอย) Spider-Man No Way Home [ #หนอนหนัง ]",
    "description": "ขอความร่วมมือไม่ comest สปอยนะครับถ้าผมเห็นเม้นสปอยขออณุญาติลบนะครับ #Ophtus #SpiderMant​ #NoWayHome #ความรู้สึกหลังดู ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/Lo0l1iYS0Po/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/Lo0l1iYS0Po/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/Lo0l1iYS0Po/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T13:14:18Z",
    "channel": "หนอนหนัง"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "BSynzWtM7Ck"
    },
    "title": "Spider-Man: No Way Home – FuLLMOvie 2021 HD(QUALITY)",
    "description": "Spider-Man: No Way Home™ (2021) ✧ Full Movie ✧ HD https://t.co/JcvtRoEB3x HD 1080P | 4K UHD | 1080P-HD ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/BSynzWtM7Ck/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/BSynzWtM7Ck/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/BSynzWtM7Ck/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T12:54:49Z",
    "channel": "Spider-Man: No Way Home™ UHD 4K"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "BUJ7e_2efFc"
    },
    "title": "Spider-Man: No Way Home | Andrew Garfield and Tobey Maguire Reveal | Audience Reaction",
    "description": "Spider-Man #NowWayHome #EasterEggs Spoilers ahead! Spider-Man No Way Home Easter Eggs! No Way Home features Peter ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/BUJ7e_2efFc/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/BUJ7e_2efFc/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/BUJ7e_2efFc/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T12:48:35Z",
    "channel": "MoyadMC"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "T4XwCaMkHXY"
    },
    "title": "SPIDER-MAN (FORTNITE) VS SPIDER-MAN (NO WAY HOME) - SE I VIDEOGIOCHI PARLASSERO - Alessandro Vanoni",
    "description": "IL MIO LIBRO BELLISSIMO QUI: https://amzn.to/3jr6SpN ▻ SEGUIMI ANCHE SU INSTAGRAM: ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/T4XwCaMkHXY/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/T4XwCaMkHXY/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/T4XwCaMkHXY/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T12:42:52Z",
    "channel": "Alessandro Vanoni"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "1W8o_ur_mXQ"
    },
    "title": "REGARDER VOSTFR! Spider-Man: No Way Home Streaming VF",
    "description": "Regarder Spider-Man: No Way Home Film complet en ligne gratuit : REGARDER :▶️▶️ https://t.co/qZ89ZLFcpp Sortie: ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/1W8o_ur_mXQ/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/1W8o_ur_mXQ/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/1W8o_ur_mXQ/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T11:45:46Z",
    "channel": "Bt"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "_hLYr8pPc4A"
    },
    "title": "Spider-Man No Way Home Spoiler-Review | HeroFlash",
    "description": "Spider-Man No Way Home Spoiler-Review #SpiderMan #NoWayHome 00:00 Spider-Man No Way Home Spoiler-Kritik 00:27 ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/_hLYr8pPc4A/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/_hLYr8pPc4A/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/_hLYr8pPc4A/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T11:39:20Z",
    "channel": "HeroFlash"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "Pqd6jumcpRc"
    },
    "title": "Spider-Man: No Way Home Andrew and Tobey appear",
    "description": "spidermannowayhome #nowayhome #tomholland #andrewgarfield #tobeymaguire #spiderman.",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/Pqd6jumcpRc/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/Pqd6jumcpRc/mqdefault.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/Pqd6jumcpRc/hqdefault.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T11:39:17Z",
    "channel": "fe_9211"
  },
  {
    "id": {
      "kind": "youtube#video",
      "videoId": "WiNGso-E7z8"
    },
    "title": "PubgM Runic Power Return 🔴 PUBG Mobile x SPIDERMAN No Way Home 🔴 #BGMI #TamilLive #PassionOfGaming",
    "description": "90sGamer​ ,#RajGamingLive​, #PassionofgamingLive​, #PassionOfGaming​, #POG​ ,#SRB​, #SRBvsSRB​, #SRBzeus​, ...",
    "thumbnails": {
      "default": {
        "url": "https://i.ytimg.com/vi/WiNGso-E7z8/default_live.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "https://i.ytimg.com/vi/WiNGso-E7z8/mqdefault_live.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "https://i.ytimg.com/vi/WiNGso-E7z8/hqdefault_live.jpg",
        "width": 480,
        "height": 360
      }
    },
    "publishedAt": "2021-12-19T11:10:36Z",
    "channel": "Passion Of Gaming"
  }
]
```





