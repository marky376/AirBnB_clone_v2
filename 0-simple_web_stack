#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "<html><head><title>Test Page</title></head><body>This is a test page</body></html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart

exit 0
