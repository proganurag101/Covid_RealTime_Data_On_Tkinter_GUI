# do all imports
import requests
import bs4
import tkinter as tk
import time
import datetimec


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_india():
    url = "https://www.worldometers.info/coronavirus/country/india/"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div1 = bs.find("div", class_="content-inner").find_all("div", id="maincounter-wrap")
    l = list()
    all_details = ""
    for block in info_div1:
        count = block.find("span").get_text()
        text = block.find("h1").get_text()
        all_details = all_details + text + " : " + count + "\n"

    return (all_details)


# creating GUI
root = tk.Tk()
root.geometry("200x200")

root.title("CORONA DATA TRACKER INDIA")
f = ("poppins", 25, "bold")
mainLabel = tk.Label(root, text=get_corona_detail_of_india())
mainLabel.pack()

root.mainloop()

get_corona_detail_of_india()
