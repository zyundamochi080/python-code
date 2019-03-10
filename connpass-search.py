import requests
import bs4
import sys

def main():
    keyword = None
    while keyword != "":
        keyword = input("キーワード:")
        if keyword == "exit":
            sys.exit()
        keySearch(keyword)


def keySearch(searchKey):
    url = "https://connpass.com/api/v1/event/?keyword=" + searchKey
    r = requests.get(url)
    data = r.json()

    if r.status_code != 200:
        print("Error")
        sys.exit()

    events = data["events"]
    for event in events:
        for k, v in event.items():
            if k == "event_url":
                print("url:"+v)
            if k == "owner_display_name":
                print("開催者:"+v)
            if k == "title":
                print("イベント名:"+v)
            if k == "place":
                print("場所:"+v)
        print("\n")

if __name__ == '__main__':
    main()
