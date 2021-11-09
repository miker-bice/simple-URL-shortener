import pyshorteners
s = pyshorteners.Shortener()
BadAPIResponse = pyshorteners.exceptions.BadAPIRespinseException


def shorten_link(user_link):
    try:
        link = s.tinyurl.short(user_link)
    except BadAPIResponse:
        print("Sorry, please try again")
    return link


# Getting the input from the user
user_link = input("Enter your link: ")
shortened_link = shorten_link(user_link)
print(f"Your shortened link is: {shortened_link}")



