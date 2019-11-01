from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
# import wtf # for Flask

def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    r = requests.get("https://www.bing.com/images/search", params=params)
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_ob = requests.get(item.attrs["href"])
            print("Getting ", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            # title = title.split("?")[0]
            # print(title)
            try:
                img = Image.open(BytesIO(img_ob.content))
                # print(img.format)
                # img.save("./scraped_images/" + title, img.format)
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Could not save image.")
        except:
            print("Could not request image.")

    StartSearch()

StartSearch()