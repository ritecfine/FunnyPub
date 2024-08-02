# /bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install nginx python3-pip python3 ffmpeg unzip libnginx-mod-rtmp -y
clear
echo "Requirements installed sucefully!"
sleep 3
sudo service nginx stop
sudo rm -r /var/www/html
cd /var/www/
wget https://github.com/op3ny/LivePub/blob/main/LivePub-en-us.zip
unzip LivePub-en-us.zip
sudo mkdir /root/livepub
cp main.zip /root/livepub/main.zip
mv /var/www/html/LivePub-en-us.zip /root/livepub/livepub-bkp.zip
rm -r LivePub-en-us.zip
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
