from exts import contactInfo


class Contacts:
    contact = contactInfo()
    emails = {name : email for name in contact.key() for email in contact.value()[0]}   
    contactNumber = {name:number for name in contact.key() for number in contact.value()[1]}

    emails.append({
        "archit":"archit.ghadshi@gmail.com",
        "papa":"cbcsudhir@gmail.com",
        "ekta":"ektachoudhary9892@gmail.com",
        "gautam":"chaudharygautam9963@gmail.com",
    })
    contactNumber.append({
        "papa":9967186153,
        "ekta":9892651308,
        "gautam":8850559026,
        "archit":9309997251,
        "banty":9069575574,
        "kuanl":6377309679,
        "laksh" : 9671799394,
    })


ERROR_REPLIES = [
    "Please don't do that.",
    "You have to stop.",
    "Do you mind?",
    "In the future, don't do that.",
    "That was a mistake.",
    "You blew it.",
    "You're bad at computers.",
    "Are you trying to kill me?",
    "Noooooo!!",
    "I can't believe you've done this",
]

NEGATIVE_REPLIES = [
    "Noooooo!!",
    "Nope.",
    "I'm sorry Dave, I'm afraid I can't do that.",
    "I don't think so.",
    "Not gonna happen.",
    "Out of the question.",
    "Huh? No.",
    "Nah.",
    "Naw.",
    "Not likely.",
    "No way, José.",
    "Not in a million years.",
    "Fat chance.",
    "Certainly not.",
    "NEGATORY.",
    "Nuh-uh.",
    "Not in my house!",
]

POSITIVE_REPLIES = [
    "Yep.",
    "Absolutely!",
    "Can do!",
    "Affirmative!",
    "Yeah okay.",
    "Sure.",
    "Sure thing!",
    "You're the boss!",
    "Okay.",
    "No problem.",
    "I got you.",
    "Alright.",
    "You got it!",
    "ROGER THAT",
    "Of course!",
    "Aye aye, cap'n!",
    "I'll allow it.",
]


if __name__ == "__main__":
    pass
