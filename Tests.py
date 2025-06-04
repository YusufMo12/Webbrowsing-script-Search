from pystyle import *
import webbrowser


print(Box.Lines("Python With  Projects :"))


Write.Print("This is Program for web  browsing The website search  \n",
            Colors.purple_to_red, interval=0.1)

print(Box.DoubleCube("Welcome To Projects"))

website_name = input("Enter Your Website:")

webbrowser.open(website_name)
