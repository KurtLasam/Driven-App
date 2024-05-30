# Tools and Module that i used to create the app#

from tkinter import *
from PIL import ImageTk, Image # type: ignore
import requests # type: ignore
import json

# Trying to switch the frames function#

def switch_to_frame(frame):
    frame.tkraise()

# Main File to access JSON file

def show_entry():
    # Labels would disapper and replaced by the #

    # Labels for FrameA#

    for widget in FrameA.winfo_children(): # Function to have child widgets#
        if widget != result_label: 
            widget.place_forget() 

    # Lables for FrameB#

    for widget in FrameB.winfo_children():
        if widget != result_label:
            widget.place_forget()

    # Labels for FrameC#

    for widget in FrameC.winfo_children():
        if isinstance(widget, Label) and widget != result_label: 
            widget.place_forget()
    
    # Custom title case function#

    def custom_title_case(word):
        exceptions = ["and", "the", "of", "da"]  # Exception for any other info given#
        return word.title() if word.lower() not in exceptions else word

    # Gathering information from the user to the app#

    entered_text = UserSearch.get() #Information from the selected country#
    formatted_text = ' '.join(custom_title_case(word) for word in entered_text.split())

    for country in data: # loop for each wanted country#
        if entered_text == country['NAME']['Similarity']: # if the input matches the Country in the API#
            official_name = country['NAME']['Exact'] # Gathering Data from the api to be used for the app#
            subregion = country.get('Subregions', 'Not Valid') # A secondary method for countries thatd ont have this kind of data#
            region = country.get('Main Regions', 'Not Valid')
            capital = country.get('Capital', '')
            continent = country.get('Continents', 'Not Valid')
            timezone = country.get('Timezone', 'Not Valid')
            weekstart = country.get('StartOfTheWeek', 'Not Valid')

            # Specific information from each country#
            try:

                currencies_data = country['Currencies', 'Not Valid']
                currencies_info = "\n".join([f"{code}: {info['Name']} ({info['Symbol']})" for code, info in currencies_data.items()])

            except KeyError as e:

                currencies_info = "The currency is Not Available."

            # Flag information#
            flag_info = country.get('Flag', {})
            flag_png_link = flag_info.get('png', 'default_flag.png')  # Default URL for flags#

            # Storing all information to one output#
            result_text = (
            f"Your Selected Country: {entered_text}\n"
            f"Name of the Country: {official_name}\n"
            f"Continents for that Country: {', '.join(continent)}\n"
            f"Regions for that Country : {region}\n"
            f"Subregion for the Country: {subregion}\n"
            f"Capitals for the Country: {', '.join(capital)}\n"
            f"Currencies that are used in the Country:\n{currencies_info}\n"
            f"Timezone for the Country: {', '.join(timezone)}\n"
            f"Start of the Week: {(weekstart)}\n"
            )

            # Check if 'alt' is available in the the flag_info#
            if 'alt' in flag_info:
                flag_alt_text = flag_info['alt']
            else:
                flag_alt_text = 'The Flag Information for the country is not valid.'

            # The output will be presented at FrameC#
            result_label.config(text=result_text, compound="TOP")

            try:

                # flag image using Pillow
                flag_image = Image.open(requests.get(flag_png_link, stream=True).raw)
                flag_image = ImageTk.PhotoImage(flag_image)
                # Displaying image in FrameA
                flag_label = Label(FrameA, image=flag_image)
                flag_label.image = flag_image
                flag_label.place(x=35, y=0, height=200)

            except Exception as e:

                # sometimes the info is not available this if for scondary messures
                print(f"Error loading flag image: {e}")
                flag_label = Label(FrameA, text="Flag Image Not Valid", bg='White')
                flag_label.place(x=35, y=0, height=200)

            
            alt_label = Label(FrameB, text=flag_alt_text, font=("Inter", 13), wraplength=380, bg='White')
            alt_label.place(x=10, y=10) 
            break 
    else:
        result_label.config(text=f"Country of choice: {entered_text}\nNot Found")

# The URL for the API#
url= "https://restcountries.com/v3.1/all"

# Data from the API#
response = requests.get(url)

#  Named Data from the variable#
data = response.json()

#  JSON File with the API Data#
file_name = "country_all_data.json"

#  Saved JSON file with Data#
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Open the JSON file for reading
with open(file_name, 'r') as json_file:

    # Load the JSON data from the file
    data = json.load(json_file)

# Thinker Window
root = Tk()
root.title("World Finder!!") #Title of the APP
root.geometry('1000x700') #Size of the window 
root.resizable(0,0) #Fixed Window Sized

# Start Frame
Start_frame = Frame(root, bg='#8c92ac')
img = ImageTk.PhotoImage(Image.open("LOGO PNG.png") )
# Display the logo image
label = Label(Start_frame, image=img, bg='#8c92ac')
label.place(x=250, y=0)
Button(Start_frame, text="INPUT", font=("Impact", 30), bg='#8c92ac', fg='black', bd=0, 
       command=lambda: switch_to_frame(frame1)).place(x=440, y= 500)
Start_frame.place(x=0,y=0, width=1000,height=700)

#  Opening Frame for Frame 1
frame1 = Frame(root, bg='#8c92ac')
Label(frame1, text="Welcome To World Finder!!",fg='black',bg='#8c92ac', font=("Inter", 40)).place(x=200, y=200)
Label(frame1, text="World Finder!! is an app that makes you see the world in you eyes",
      fg='black',bg='#8c92ac', font=("Open Sans", 20)).place(x=100, y=300)
Label(frame1, text="Uncover, Join, and View the Worlds:\nYour eyes in the World",
      fg='black',bg='#8c92ac', font=("Open Sans", 20)).place(x=200, y=335)
Label(frame1, text="Made by ; KURT LASAM \n Bathspa University , YEAR 2 ",
      fg='black',bg='#8c92ac', font=("Open Sans", 15)).place(x=10, y=30)
Button(frame1, text="See the Wolrd in your EYES", font=('Inter', 30), bg='#8c92ac', fg='#00227A', bd='0',
       command=lambda: switch_to_frame(frame2)).place(x=330, y= 500)
frame1.place(x=0,y=0, width=1000,height=700)

# frame 2, tagline page
frame2 = Frame(root, bg='#8c92ac')
Label(frame2, text="World Finder!!",
      fg='black',bg='#8c92ac', font=("Inter", 30)).place(x=390, y=30)
Label(frame2, text="Selected Country:", fg='black', bg='#8c92ac', 
      font=("Inter", 20)).place(x=250, y=100)
UserSearch = Entry(frame2, width=25, font=("Open Sans", 15))
UserSearch.place(x=450, y=110)
search_button = Button(frame2, text="Find", command=show_entry, font=("Inter", 20), bg='#8c92ac', fg='black', bd='0')
search_button.place(x=750, y=95)
frame2.place(x=0,y=0, width=1000,height=700)

# Frame 2

# Inside Frame 2
miniframe = Frame(frame2, bg='#8EABD1')
miniframe.place(x=30,y=180, width=940,height=500)

# Frame A 
FrameA = Frame(miniframe, bg='white', bd='1', relief='ridge')
Label(FrameA, text="Flag will be displayed here:", font=("Open Sans", 13), bg='white').place(x=10, y=10)
FrameA.place(x=20,y=20, width=400,height=200)

# Frame B
FrameB = Frame(miniframe, bg='white', bd='1', relief='ridge')
Label(FrameB, text="Flag discription displayed here:", font=("Open Sans", 13), bg='white').place(x=10, y=10)
FrameB.place(x=20,y=250, width=400,height=210)

# Frame C
FrameC = Frame(miniframe, bg='white', bd='1', relief='ridge')
Label(FrameC, text="Details Displayed Here:", font=("Open Sans", 13), bg='white').place(x=10, y=10)
result_label = Label(FrameC, font=("Open Sans", 13), justify="left", wraplength=300, bg='white')
result_label.place(x=120, y=30)
Button(FrameC, text="END", font=('Inter', 30), bg='white', fg='black', bd='0',
       command=lambda: switch_to_frame(lastframe)).place(x=350, y= 350)
FrameC.place(x=450,y=20, width=460,height=440)

# Last Frame 
lastframe = Frame(root, bg='#8c92ac')
Label(lastframe, text="We appreciate you for using World Finder!!",fg='black',bg='#8c92ac', font=("Inter", 40)).place(x=120, y=200)
Button(lastframe, text="Use Again", font=('Inter', 30), bg='#8c92ac', fg='#00227A', bd=0,
       command=lambda: switch_to_frame(Start_frame)).place(x=400, y= 400)
lastframe.place(x=0,y=0, width=1000,height=700)


# Start Initially
switch_to_frame(Start_frame)

root.mainloop()