import requests

def NewsFromMilliyet():
    query_params = {
        "source": "milliyet.com.tr",
        "sortBy": "top",
        "apiKey": "" #uyelik https://newsapi.org/s/turkey-news-api
    }
    main_url = "http://newsapi.org/v2/top-headlines?country=tr&apiKey=73abf5c84ea4463eb34dff988302cea7"

    res = requests.get(main_url, params=query_params)
    open_milliyet = res.json()


    article = open_milliyet["articles"]


    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])


# Driver Code
if __name__ == '__main__':
    NewsFromMilliyet()
