
# do all imports
import requests
import bs4
import tkinter as tk
import time
import datetime
import selenium


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_india():
    url = "https://www.worldometers.info/coronavirus/country/india/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="content-inner").find_all("div",id="maincounter-wrap")
    all_data =""
    for i in range(3):
        text =  info_div[i].find("h1", class_ = None).get_text()
        count = info_div[i].find("span", class_ = None).get_text()
        all_data = all_data + text + " " + count + "\n"
    return all_data


def reload():
    new_data = get_corona_detail_of_india()
    mainlabel['text']=new_data


get_corona_detail_of_india()

#GUI

root = tk.Tk()
root.geometry("500x500")
root.title("CORONA DATA TRACKER INDIA")
f = ("poppins",25,"bold")

banner = tk.PhotoImage(file="covid.png")
bannerlabel = tk.Label(root,image=banner)
bannerlabel.pack()



mainlabel = tk.Label(root,text=get_corona_detail_of_india(),font=f)
mainlabel.pack()


rbtn = tk.Button(root,text='Reload',font=f,relief='solid',command=reload())
rbtn.pack()

root.mainloop()

