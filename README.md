Section 1 - For the user!

# About me

Hello, my name is Humberto, but you can call me of op3n. Since i was 8 i started to create projects and Linux things, i always told that internet need to be more "free and open" for the people, and the Open Source, is exacly that, but another thing that i always told is advanced things on softwares need to be more simple, and this project (LivePub) is exacly that, turn the live broadcasts more simple and user-friendly to use. And i can help the developers, because you can use that on your Website!

# Let's Start!

Okey, before you start, you need to try use our demo of the LivePub (You can acess by: http://livepub.ddns.net).

This website will run locally on your computer, and i will explain how.

# Requirements:

Ram: 2gb
CPU: (Probably will work with your CPU)
Operating System: Ubuntu 22.04 LTS (I recomend you use Ubuntu 22.04 LTS or Ubuntu 20.04 LTS)
Applications: ffmpeg, python3, python3-pip, nginx (The script will do that for you!)

# The code!

First you will need to download our script
Code: 
```
sudo su
```
```
apt update && apt upgrade -y
```
```
apt install wget curl -y
```
```
wget lsdfjsdlfkjdlfkjflksdjflkj/script.sh
```
```
chmod 777 script.sh
```
```./script.sh```

After all you need to reboot your machine, with this command:
```
reboot
```

# New commands!

On your system, you will have three new commands (Works only on root)
```
livepub-start
```
Start the LivePub
```
livepub-stop
```
Stop the LivePub
```
livepub-uninstall
```
Will remove all the archives witch he installed (Nginx too)
