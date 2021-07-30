# How Run Alice :)

### As you know, Alice is your personal desktop Assistant which will going to help you in verity of tasks!<br>

**So basically Alice will need few requirements to run it, Please Go thorugh the following steps and nothing:**
<br><br>
1. First a fall, You will defiantly need to Clone the Project or Download the zip file<br>
2. Install python stable version for your machine from [python.org](https://www.python.org/downloads/release/python-387/)<br>
3. Install the required modules by just running following commands in the same directory's terminal :<br>
   i.`pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl`    
   ii.`pip install -r Requirements.txt`
<br><br>
4. Then create .env file in that main directory and put the following info :<br>
    1. `AssistantName=Alice`  **(You can change the name of Assistant)**
    2. `UserName=Abhinav`     **(Your name)**
    3. `GENDER=male`		  **(Your Gender)**
    4. `ALICE_PASSWORD=` **YOu can put password for your Alice** (Optional, you can also leave it)**<br><br>
    5. `VoiceRate=175`		  **(voice rate keep it as a 175 its totally fine, but you can change it as per your requirements)**
    6. `VoiceNumber=1`		  **(by the way keep it 1, you can get info about this by telling alice for `how many voices you have`)**
    7. `GITHUB=Brodevil`	   **(your [github](https://github.com/Brodevil) username)**<br><br>
    8. `MUSIC=C:\Users\ADMIN\Music`  **(your music directory path, where all your music are available)**
    9. `FavMusic=C;\Users\ADMIN\Music\cj.mp3` **(Your favorite  music path)**
       <br><br>
    10. `emailID=`   **(your Email Id eg. youremail@gmail.com)**
    11. `emailPassword=`   **(password of Email id)**<br>
    Actually this just totally save we are not playing with your privacy, just for sending emails and all it's needed and
    Firstly Enable [Less Secure apps](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NqK_w8itXLmU61XOIaNEY6NxvbMEyJtfB_MinE6JyU4Z7IGUwfQ-tKUq4zs5_0AcJMxDWiGoEUyw1Eet__Q3mVr322wA) of that Google Account so that you will be able to email using Alice by just voice commands :}<br><br>
    11. `OpenWeatherMapApi=` **(Your API key of Open Weather)**<br>
         Get your api key by creating a free account [here](https://home.openweathermap.org/users/sign_up), 
         and then you just log in by that account and copy your api key [here](https://home.openweathermap.org/api_keys), and paste it there.
        
   12. `NewsApiKey=`  **(Your API key of NewsAPI)**<br>
       Get your api key by creating a free account in [NewsAPI](https://newsapi.org/register), and then log in with your id and password afterwards you will be able to copy your api key from [here](https://newsapi.org/account), 
         and then paste your api key here.<br><br>
   
       ### For Example:
    ![envFile](https://raw.githubusercontent.com/Brodevil/Alice/main/Assistant/resources/Images/env_file.png)
        

<br><br>
5. In the [Application Folder](https://github.com/Brodevil/Alice/tree/main/Applications), There are several inbuile windows 10 Applicatinos, add more applications 
   shortcuts, which you use in day to day life just like VS Code, PyCharm, Discord or which you have. So then we will be able to launch 
   this software easily by just voice command :}<br>
 
6. Now, You have to open the [DailyWorks.xlsx](https://github.com/Brodevil/Alice/blob/main/DailyWorks.xlsx) which is an Exel file, there are some present examples there, but you can delete those, and write the time and the work you had, so that the Alice will be reminding you when ever it will be running, it will remind you at time to time. <br><br>
   ![DailyWorks](https://raw.githubusercontent.com/Brodevil/Alice/main/Assistant/resources/Images/DailyWorksExel.gif)
<br>

7. Now, you had to open the [Contact.xlsx](Contact.xlsx) which is also a execl file, there are some example of contacts, you delete them and put your contacts there,`|Name | Email| Phone Number|`, You can also leave email or phone any one of them if you not have then, Note : Put `'` before putting phone number, example : `'+91 9034982425`.<br><br>
   ![Contacts Exel](https://raw.githubusercontent.com/Brodevil/Alice/main/Assistant/resources/Images/contacts.gif)<br><br>

8. Now, you can run the [run.py](run.py) file or just use `python run.py` command in terminal to run the file.

## That's it
