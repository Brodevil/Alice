# How Run Alice :)
<br>


#### As you know :<br>Alice is your personal desktop Assistant which will going to help you in verity of tasks

**<br>So in this way Alice will need few following requirements to run it :**
<br>
1. First a fall, You will defiantly need to Clone the Project or Download the zip file 
<br><br>
2. Install the required modules by just running following commands in the same directory's terminal :<br>
   i.`pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl`    
   ii.`pip install -r Requirements.txt`
<br><br>
3. Then create .env file in that directory and put the following info :<br>
    1. `AssistantName=Alice`  **(You can change the name of Assistant)**
    2. `UserName=Abhinav`     **(Your name)**
    3. `GENDER=male`		  **(Your Gender)**<br><br>
    4. `VoiceRate=175`		  **(voice rate keep it as a 175 its totally fine, but you can change it as per your requirements)**
    5. `VoiceNumber=1`		  **(by the way keep it 1, you can get info about this by telling alice for `how many voices you have`)**
    6. `GITHUB=Brodevil`	   **(your [github](https://github.com/Brodevil) username)**<br><br>
    7. `MUSIC=C:\Users\ADMIN\Music`  **(your music directory path, where all your music are available)**
    8. `FavMusic=C;\Users\ADMIN\Music\cj.mp3` **(Your favorite  music path)**
       <br><br>
    9. `emailID=`   **(your Email Id eg. youremail@gmail.com)**
    10. `emailPassword=`   **(password of Email id)**<br>
    _Actually this just totally save we are not playing with your privacy, just for sending emails and all it's needed and
    Firstly Enable [Less Secure apps](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NqK_w8itXLmU61XOIaNEY6NxvbMEyJtfB_MinE6JyU4Z7IGUwfQ-tKUq4zs5_0AcJMxDWiGoEUyw1Eet__Q3mVr322wA) of that Google Account so that you will be able to email using Alice by just voice commands :}_<br><br>
    11. `OpenWeatherMapApi=` **(Your API key of Open Weather)**<br>
         Get your api key by creating a free account [here](https://home.openweathermap.org/users/sign_up), 
         and then you just log in by that account and copy your api key [here](https://home.openweathermap.org/api_keys), and paste it there.
        
   12. `NewsApiKey=`  **(Your API key of NewsAPI)**<br>
       Get your api key by creating a free account in [NewsAPI](https://newsapi.org/register), and then log in with your id and password afterwards you will be able to copy your api key from [here](https://newsapi.org/account), 
         and then paste your api key here.<br><br>
       ### For Example:
    ![envFile](https://raw.githubusercontent.com/Brodevil/Alice/main/Media/env_file.png)
        

<br><br>
4. In the [Application Folder](https://github.com/Brodevil/Alice/tree/main/Applications), Add the more applications 
   shortcuts, which you use in day to day life just like VS Code, PyCharm, Discord or which you have. So then we will be able to launch 
   this software easily by just voice command :}
   
<br><br>
5. Now, You have to open the [DailyWorks.xlsx](DailyWorks.xlsx) which is an Exel file and by the given example, 
   you can understand who to write the data. You just change to put the time in 24 Hr or in 12 Hr in first column
   and in the second column write the work which you have to do, So in this way the Alice will going to run whole