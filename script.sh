# /bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install nginx python3-pip python3 ffmpeg unzip -y
clear
echo "Requirements installed sucefully!"
sleep 3
sudo service stop nginx
sudo rm -r /var/www/html/*
sudo rm -r /var/www/html
sudo mkdir /var/www/html
wget https://github.com/op3ny/LivePub/archive/refs/heads/main.zip
sudo mkdir /root/livepub
cp main.zip /root/livepub/main.zip
mv /root/livepub/main.zip /root/livepub/livepub-bkp.zip
cp /root/livepub/livepub-bkp.zip /var/www/html/livepub.zip
cd /var/www/html
unzip livepub.zip
cp /var/www/html/LivePub-main/* ..
rm -r /var/www/html/LivePub-main
rm -r livepub.zip
rm -r /etc/nginx/nginx.conf
wget https://raw.githubusercontent.com/op3ny/LivePub/main/backend/nginx.conf
cp nginx.conf /etc/nginx/nginx.conf
clear
echo "LivePub Downloaded Sucefully!"
sleep 3
python3 /var/www/html/backend/render.py &
python3 /var/www/html/backend/delete.py &
service nginx restart
clear
echo "LivePub Installed Sucefully! Bye bye!"
wget https://raw.githubusercontent.com/op3ny/LivePub/main/commands/livepub-start
wget https://raw.githubusercontent.com/op3ny/LivePub/main/commands/livepub-stop
mv livepub-start /bin/livepub-start && chmod 777 /bin/livepub-start
mv livepub-stop /bin/livepub-stop && chmod 777 /bin/livepub-stop
sleep 3
echo "Rebooting the system..."
sleep 2
reboot
