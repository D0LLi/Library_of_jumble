# Library of jumble 
# A project similar to library of babel, but with english words.
# Github: https://www.github.com/lewisevans2007/library_of_jumble

import os
import secrets


words = open("src/words.txt", "r").read().split("\n")

def generate_book(): 
    book = ""

    title = ""
    for i in range(secrets.SystemRandom().randint(1, 4)):
        title += secrets.choice(words) + " "
    title = title[:-1]

    description = ""
    for i in range(secrets.SystemRandom().randint(1, 40)):
        description += secrets.choice(words) + " "
    description = description[:-1] + "."

    max_pages = secrets.SystemRandom().randint(1, 1000)
    pages = []
    for i in range(max_pages):
        page = ""
        capitalise_next = True
        for i in range(secrets.SystemRandom().randint(100, 400)):
            if capitalise_next:
                page += secrets.choice(words).capitalize() + " "
                capitalise_next = False
            else:
                page += secrets.choice(words) + " "

            if secrets.SystemRandom().randint(1, 12) == 1:
                page = page[:-1] # Remove the space
                page += ". "
                capitalise_next = True

            elif secrets.SystemRandom().randint(1, 24) == 1:
                page = page[:-1]
                page += ", "

            elif secrets.SystemRandom().randint(1, 40) == 1:
                page = page[:-1]
                page += "? "
                capitalise_next = True
            elif secrets.SystemRandom().randint(1, 40) == 1:
                page = page[:-1]    
                page += "! "
                capitalise_next = True
            elif secrets.SystemRandom().randint(1, 40) == 1:
                page = page[:-1]
                page += "; "
                capitalise_next = True
            elif secrets.SystemRandom().randint(1, 80) == 1:
                page = page[:-1]
                page += "\n\n"
                capitalise_next = True
    
        page = page[:-1]
        pages.append(page)

    book += title + "\n\n" + description + "\n\n---\n\n"
    for page in pages:
        book += page + "\n\n---\n\n"
    return book, title

while True:
    floor = secrets.SystemRandom().randint(1, 5)
    try:
        os.mkdir("data/" + str(floor))
    except:
        pass

    row = secrets.SystemRandom().randint(1, 10)
    try:
        os.mkdir("data/" + str(floor) + "/" + str(row))
    except:
        pass

    shelf = secrets.SystemRandom().randint(1, 10)
    try:
        os.mkdir("data/" + str(floor) + "/" + str(row) + "/" + str(shelf))
    except:
        pass

    if len(os.listdir("data/" + str(floor) + "/" + str(row) + "/" + str(shelf))) >= 100:
        print("Skipping shelf as it is full")
        continue

    book, title = generate_book()

    try:
        with open("data/" + str(floor) + "/" + str(row) + "/" + str(shelf) + "/" + title + ".txt", "w") as f:
            f.write(book)
        print("Wrote book to shelf " + str(floor) + "/" + str(row) + "/" + str(shelf) + "/" + title + ".txt")
    except:
        print("Failed to write book to shelf " + str(floor) + "/" + str(row) + "/" + str(shelf) + "/" + title + ".txt")
