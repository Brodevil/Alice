from os import environ
from dotenv import load_dotenv
import pyttsx3
from Assistant.exts.networks import localInfo, weather, internetConnection                                 # noqa
import shutil
import psutil
import string




__all__ = ("Client", "Contact", "ERROR_REPLIES", "NEGATIVE_REPLIES", "POSITIVE_REPLIES", "Storage")



def Storage():
    """ Function to get total harddrive storage as per the drive """
    totalStorage = 0
    usedStorage = 0
    freeStorage = 0
    for i in list(string.ascii_lowercase):
        try:
            storeInfo = list(map(lambda x : x//2**30, shutil.disk_usage(f"{i}:\\")))
            totalStorage += storeInfo[0]
            usedStorage += storeInfo[1]
            freeStorage += storeInfo[2]
        except Exception:
            pass
    return totalStorage, freeStorage, usedStorage




load_dotenv()
storageInfo = Storage()
engine = pyttsx3.init()
localInformation = localInfo()
try:
    battery = psutil.sensors_battery()
except Exception:
    battery = None




class Client:
    Assistantname = environ.get("AssistantName", "Alice")
    intro = f"Hey There! Now me to introduce myself, I am {Assistantname}. A virtual desktop assistant and I'm here to assist you with a verity of tasks as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home interface, system is now initializing!"
    aliceInfo =  "I am written in python by Abhinav, My birthday is 21 December of 2020."
    
    
    # Author Info
    author = "Abhinav(Brodevil)"
    contact = "brodevil89@gmail.com"
    github_assistant_repo = "https://github.com/Brodevil/Alice"


    # Client Choice to Alice
    voices = [engine.id for engine in engine.getProperty("voices")]
    voiceRate = int(environ.get("VoiceRate", 175))
    voice = int(environ.get("VoiceNumber", 1))
    if voice > len(voices):
        raise Exception(f"There are just {len(voices)} available in your system and you had choiced the {voice} number of voice! please Change it in .env file")
            

    # Few Computer status
    storage = {"Total": storageInfo[0], "Used": storageInfo[1], "Free": storageInfo[2]}     # values are in GB
    memory_status = psutil.virtual_memory().percent     # Used memory in percentage
    cpu_status = psutil.cpu_percent()   # cpu uses in percentage 
    internet = internetConnection()


    # Few user Info :
    musicDirectory = environ.get("MUSIC", r"C:\Users\ADMIN\Music")              # Music directory should be without space
    favorateMusic = environ.get("FavMusic", None)
    userGithub = environ.get("GITHUB", "Brodevil")


    if battery != None:
        battery_status = battery.percent
        battery_pugged = battery.power_plugged


    # Networks infos 
    if localInformation != None and weather() is not None:
        city = localInformation[0]
        location = localInformation[1]['country'], localInformation[1]["regionName"], localInformation[1]["city"]
        network = localInformation[1]["isp"]
        weatherInfo = weather()

    

        
    

class Contacts:
    emails = {'Abhinav Kumar Choudhary': 'abhinavchaudhary351@gmail.com',
            'Aditya sanjay kamble': 'adityasanjaykamble@gmail.com',
            'Aniket Bhagat. ': 'aniketbhagat0060@gmail.com',
            'Ankit Manoj Manjhi ': 'ankitmanojmanjhi@gmail.com',
            'Anshika Krishnadatt Upadhyay ': 'anu.upadhyay677@gmail.com',
            'Chandana Chandrakant Date ': 'pushadate@gamil.com',
            'Chaturthi Ramdas Padekar': 'chaturthipadekar@gmail.com',
            'Chetana isame': 'isamechetana@gmail.com',
            'Gaurav Tribhuvan Yadav': 'gaurav.t.y0884@gmail.com',
            'Gauri Sunil Chothe': 'gaurichothe23@gmail.com',
            'Gayatri Suresh Bagul': 'gayatribagul095@gmail.com',
            'Harsh khapare ': 'Khapareharsh@gmail.com',
            'Janhavi Mukane': 'mukanegirish@gmail.com',
            'Kaustubh Sonkamble ': 'santoshsonkamble1970@gmail.com',
            'Kushal Sadashiv Madhavi': 'Kushalmadhavi473@gmail.com',
            'Manaswi Madhukar Pingale ': 'manupingale2604@gmail.com',
            'Mayuri vishwanath ghute': 'ghutemayuri66@gmail.com',
            'Narendra tukaram jabar': 'narendrajabar@gmail.com',
            'Omraje jadhav': 'appameenakshi940@gmail.com',
            'Prachee Pradeep Dudhale': 'prachidudhale17@gmail.com',
            'Pranjal Dattatray Gunjal': 'pranjalgunjal99@gmail.com',
            'Pratik sandip valkar ': 'pratikvalkar08@gmail.com',
            'Rohit Kashinath khodka': 'sunitakhodka22@gmail.com',
            'SHREYAS BORATE': 'borateshreyas378@gmail.com',
            'Samiksha Sunil Dhule': 'samikshadhule10@gmail.com',
            'Sanika Rohidas Korade ': 'snkkorade@gmail.com',
            'Sarthak Ghule': 'sarthakghule24@gmail.com',
            'Shivam Gopale': 'shivamgopale31@gmail.com',
            'Shubham  mahesh Patil': 'shubhammpatil000@gmail.com',
            'Smit Mahendra gondane ': 'smitgondane1919@gmail.com',
            'Sumit kanojiya': 'srbkkanojiya@gmail.com',
            'Swati santosh badade': 'sandeshabadade31108@gmail.com',
            'Tejal Sanjay Gaykar': 'sanjaygaikar99@gmail.com',
            'Tejaswini kashinath vavre': 'vavarekashinath@gmail.com',
            'Trupti sameer bhoye': 'suvarnabhoye58@gmail.com',
            'Ujjwal Kantilal Patil': 'ujjwalpatil708@gmail.com',
            'Vaishnavi Kharade': 'kharadevaishnavi608@gmail.com',
            "archit":"archit.ghadshi@gmail.com",
            "papa":"cbcsudhir@gmail.com",
            "ekta":"ektachoudhary9892@gmail.com",
            "gautam":"chaudharygautam9963@gmail.com",
            "Marcus Kartik":"work.marcus315@gmail.com",
            "ganga":"dhanlakxmichoudhary38@gmail.com",
            "narmata":"bhaglakxmichoudhary@gmail.com",
            }



    contactNumber ={'Abhinav Kumar Choudhary': 7506095094,
            'Aditya sanjay kamble': 7045230049,
            'Aniket Bhagat. ': 9763992780,
            'Ankit Manoj Manjhi ': 9637396230,
            'Anshika Krishnadatt Upadhyay ': 8830134520,
            'Chandana Chandrakant Date ': 9158288644,
            'Chaturthi Ramdas Padekar': 9325394161,
            'Chetana isame': 9273721222,
            'Gaurav Tribhuvan Yadav': 8329559875,
            'Gauri Sunil Chothe': 7391812871,
            'Gayatri Suresh Bagul': 7387892219,
            'Harsh khapare ': 9226119874,
            'Janhavi Mukane': 9420744123,
            'Kaustubh Sonkamble ': 9527696181,
            'Kushal Sadashiv Madhavi': 8767164188,
            'Manaswi Madhukar Pingale ': 9209263397,
            'Mayuri vishwanath ghute': 9356055875,
            'Narendra tukaram jabar': 8788864820,
            'Omraje jadhav': 9403815699,
            'Prachee Pradeep Dudhale': 8381036497,
            'Pranjal Dattatray Gunjal': 9594118033,
            'Pratik sandip valkar ': 9049860840,
            'Rohit Kashinath khodka': 9359135803,
            'SHREYAS BORATE': 8355965254,
            'Samiksha Sunil Dhule': 7066536749,
            'Sanika Rohidas Korade ': 9226730906,
            'Sarthak Ghule': 9022901053,
            'Shivam Gopale': 8975057675,
            'Shubham  mahesh Patil': 9833613573,
            'Smit Mahendra gondane ': 9011150967,
            'Sumit kanojiya': 7020599034,
            'Swati santosh badade': 7666197459,
            'Tejal Sanjay Gaykar': 8082580049,
            'Tejaswini kashinath vavre': 9272569360,
            'Trupti sameer bhoye': 8355879138,
            'Ujjwal Kantilal Patil': 8600345095,
            'Vaishnavi Kharade': 9373783392,
            "papa":9967186153,
            "ekta":9892651308,
            "gautam":8850559026,
            "archit":9309997251,
            "banty":9069575574,
            "kunal":6377309679,
            "laksh" : 9671799394,
            "Marcus Kartik":7088283847,}



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
    # print(Client.storage)
    pass
