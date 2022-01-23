import requests
from tkinter import *
from bs4 import BeautifulSoup

req = requests.get("https://www.worldometers.info/coronavirus/")
soup  = BeautifulSoup(req.content,'html.parser')
def total_data():
    global Total_Cases
    global deaths
    global recovered
    Total_Cases = soup.find(style = "color:#aaa").get_text()
    deaths = str(soup.find_all(class_ = "maincounter-number")[1]).split()[2].lstrip('<span>').rstrip('</span>')
    recovered = str(soup.find_all(class_ = "maincounter-number")[2]).split()[4].lstrip('<span>').rstrip('</span>')

root = Tk()
root.title('Covid Tracker')
root.resizable(0,0)
root.geometry('800x600')
total_data()

def country_data(c):
    global Country_Cases
    global Country_Deaths
    country = {}
    country_recovered = {}
    country_deaths = {}
    data = soup.find('table').find('tbody').find_all('tr')
    for rows in data:
        for i in rows.find_all('td'):
            for j in i.find_all(class_='mt_a'):
                value1 = rows.find(style ='font-weight: bold; text-align:right').get_text()
                value2 = rows.find_all(style ='font-weight: bold; text-align:right')[1].get_text()
                value3 = rows.find_all('td')[4].get_text()
                country[j.get_text().lower()] = value1
                country_recovered[j.get_text().lower()] = value2
                country_deaths[j.get_text().lower()] = value3

    if c.lower() in country:
        label4 = Label(root,text=c.upper()+' -',font=("Arial", 23))
        label4.place(x = 100,y=238)
        label5 = Label(root,text='Total Cases',font=("Arial", 25))
        label5.place(x = 50,y=300)
        lbltxt1 = Label(root,text=country[c.lower()],font=("Arial", 20))
        lbltxt1.place(x = 58,y= 335)
        label6 = Label(root,text='Total Recovered',font=("Arial", 25))
        label6.place(x = 300,y=300)
        lbltxt2 = Label(root,text=country_recovered[c.lower()],font=("Arial", 20))
        lbltxt2.place(x = 324,y=335)
        label7 = Label(root,text='Total Deaths',font=("Arial", 25))
        label7.place(x = 600,y=300)
        lbltxt3 = Label(root,text=country_deaths[c.lower()],font=("Arial", 20))
        lbltxt3.place(x = 619,y=335)

    inpfield.delete('0','end')




label1 = Label(root,text='Total Cases',font=("Arial", 25))
label1.place(x=50,y=30)
lbltxt = Label(root,text=Total_Cases,font=("Arial", 23))
lbltxt.place(x = 55,y=80)
label2 = Label(root,text='Total Recovered',font=("Arial", 25))
label2.place(x=300,y=30)
lbltxt1 = Label(root,text=recovered,font=("Arial", 23))
lbltxt1.place(x = 320,y=80)
label3 = Label(root,text='Total Deaths',font=("Arial", 25))
label3.place(x=600,y=30)
lbltxt2 = Label(root,text=deaths,font=("Arial", 23))
lbltxt2.place(x = 615,y=80)
inpfield = Entry(root,width=54,font=("Arial",20))
inpfield.place(x =81,y=150)
inpfield.insert(0,'Search Country here...')
inpfield.bind("<FocusIn>", lambda args: inpfield.delete('0', 'end'))
button = Button(root,text='Search',width='58',height=2,font=("Arial",17),command=lambda:country_data(inpfield.get()))
button.place(x=114,y=188)
root.mainloop()









