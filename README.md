Section 1 - For the user!

# About

Hello! Welcome to LivePub's Github. The LivePub is a Open Source project witch will help you to self host your own Live Broadcast. With a user friendly panel, and a simple way to install! So i hope you will enjoy and Let's Start!


# Images

[Image 1](https://github.com/op3ny/LivePub/blob/main/images/Screenshot%20from%202024-07-16%2014-31-57.png)
[Image 2](https://github.com/op3ny/LivePub/blob/main/images/Screenshot%20from%202024-07-16%2014-31-49.png)
[Image 3](https://github.com/op3ny/LivePub/blob/main/images/Screenshot%20from%202024-07-16%2014-32-08.png)
[Video 1](https://github.com/op3ny/LivePub/raw/main/images/Screencast%20from%202024-07-16%2014-30-46.mp4)
[Video 2](https://github.com/op3ny/LivePub/raw/main/images/Screencast%20from%202024-07-16%2014-31-14.mp4)






# Let's Start!

Okey, before you start, you need to try use our demo of the LivePub (You can acess by: [Click here to open](http://livepub.ddns.net)).

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
wget https://raw.githubusercontent.com/op3ny/LivePub/main/script.sh
```
VERSION IN PORTUGUESE / VERÇÃO EM PORTUGUES ------^

```
wget https://github.com/op3ny/LivePub/raw/main/script2.sh
```
VERSION IN ENGLISH / VERÇÃO EM INGLES ---------^
```
chmod 777 script.sh
```
```
./script.sh
```

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


# Another Readme

[README in Portuguese / README em Portugues](README-pt-br.md)
