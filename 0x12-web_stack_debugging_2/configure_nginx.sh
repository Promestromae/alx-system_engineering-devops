#!/bin/bash

# Configure Nginx to run as the nginx user and listen on all active IPs on port 8080
sed -i "s/user www-data;/user nginx;/g" /etc/nginx/nginx.conf
sed -i "s/listen 80 default_server;/listen 8080 default_server;/g" /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
service nginx restart

# Display Nginx processes and check port 8080
ps auxff | grep ngin[x]
nc -z 0 8080
