


'''Create a python function that takes an integer number and
print the number in words'''

from num2words import num2words
def num_to_words():
    num=input("enter any number to translate to words \n")
    if num.isdigit():
        num_word=num2words(num, to='ordinal')
        print(num_word)
    else :
        print("the input not number ")
        num_to_words()
    return
num_to_words()





''' create a python function that takes a text from the user and
print the text in colors'''

from colorama import Fore
from colorama import Style
def  colored_text(): 
    tx=input("enter the text \n")
    print(f"{Fore.BLUE}"+tx)
colored_text()



'''create a python function that takes a url of an
image from google and save location , then download the image in the save
location'''
import os
import requests
def Google_Image_Downloader():
    image_url=input("enter url ")
    #"http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg"
    folder_name=input("enter name of folder ")

    os.mkdir(folder_name)
    os.chdir(folder_name)
    img_data = requests.get(image_url).content
    with open('soup.jpg', 'wb') as handler:
        handler.write(img_data)

    print("done")
Google_Image_Downloader()





'''create a python function that takes the user height , weight and
print the user BMI and if the user underweight , overweight or healthy'''

l=float(input("enter your height in metres :"))
w=float(input("enter your weidth :"))
def BMI_calculator(l,w):
    bmi=w/(l*l)
    print(f"your BMI ={round(bmi,2)}")
    if bmi<=25 and bmi>=18.5:
        print("normal weight")
    elif bmi<18.5:
        if bmi >=16:
            print("Weight loss")
        elif bmi >15 and bmi<16:
            print("severe weight loss")
        elif bmi <15:
            print("Very severe weight loss")
    elif bmi>25:
        
        if bmi <30:
            print("Increase in weight")
        elif bmi>30 and bmi<=35:
            print("first degree obesity")
        elif bmi>35 and bmi<=40:
            print("second degree obesity")
        else:
            print("Too obese")
    return "Thanks"
print(BMI_calculator(l,w))




'''Create a python script that take a desktop screenshot every
minute , and save them in a new folder on the desktop'''

import os
import pyautogui
import schedule
import time
def Screenshot_taker():
    sc=input("enter name of folder")
    path=os.path.join("Desktop",sc)
    if os.path.exists(path):
        print("the file there")
        os.system(f'start {os.path.realpath(path)}')
    else:
        os.mkdir(path)
    n=1
    while (True):
        image = pyautogui.screenshot()
        image = image.save(f'{path}/picofscreenoo{n}.png')
        time.sleep(60)
        n=n+1
    return
Screenshot_taker()




'''create a python function that takes a user birthdate and
print how many days left to the birthday'''

import datetime
def Birthday_Calculator():
    year0=int(input("enter birth year :"))
    month0=int(input("enter birth mont :"))
    day0=int(input("enter birth day :"))
    date_of_now=datetime.date.today()
    date_of_birth=datetime.date(year0,month0,day0)
    if date_of_birth.month<date_of_now.month:
        now1=date_of_now.year
        now1=now1+1
        next_birth=datetime.date(now1,month0,day0)
        Remaining=next_birth-date_of_now
        print(f"Remaining on your date of birth {Remaining}")
    elif date_of_birth.month>date_of_now.month:
        now2=date_of_now.year
        next_birth=datetime.date(now2,month0,day0)
        Remaining2=next_birth-date_of_now
        print(f"Remaining on your date of birth {Remaining2}")
    else :
        print("This day is your birthday")
Birthday_Calculator()





'''create a python function that takes user birthdate and prints
how old he is'''
import datetime
year=int(input('When is your birthday? [YY] '))
month=int(input('When is your birthday? [MM] '))
day=int(input('When is your birthday? [DD] '))
dtb = datetime.date(year, month, day)
dn=datetime.date.today()
print(f"Your age :\n{dn.year-year}years,{dn.month-month}months,{dn.day-day}days")





''' create a python
function the takes a string and prints how many time each unique word exists in
the sentence
'''
def  frequency():
    sentence=input("enter sentence \n")
    sentence=sentence.split(" ")
    count=dict()
    for i in sentence:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for x,y in count.items():
        print(f"{x,y}\n")
frequency()


# In[66]:


'''create a python function that takes an image path , the the
needed image size then resize the image to this size and save it in the same folder
'''

from PIL import Image
from resizeimage import resizeimage
def Image_resizer():
    img = Image.open(r'C:\Users\toto8\Desktop\imagee\picofscreenoo1.png')
    path=os.path.join("Desktop","imagee")
    resizeImage = img.resize((600, 600))
    resizeImage.save(f'{path}/ImageAfterResize.png')
    print('Image before Edit Size : ', img.size)
    print('Image After Edit Size : ', resizeImage.size)
    return
Image_resizer()





'''create a python script that can count how many words the
use type per minute'''

import time 
def Typing_Speed():
    t0 = time.time() #start time
    sentence=input()
    t1 = time.time() #stop time
    timeTaken = t1 - t0
    sentence=sentence.split(" ")
    count_ofwords=len(sentence)
    total_time=round(timeTaken,2)
    typing_speed=round((total_time/count_ofwords)/60,4)
    print(f'{typing_speed} minutes')
    return 
Typing_Speed()





import datetime
def Days_Calculator():
    print("enter first date \n")
    year=int(input('[YY] '))
    month=int(input('[MM] '))
    day=int(input('[DD] '))
    print("enter second date \n")
    year2=int(input('[YY] '))
    month2=int(input('[MM] '))
    day2=int(input('[DD] '))
    dtb = datetime.date(year, month, day)
    dtb2 = datetime.date(year2, month2, day2)
    days_between=abs(dtb2-dtb)
    print(f'the days between dates {days_between}')
    return 
Days_Calculator()






