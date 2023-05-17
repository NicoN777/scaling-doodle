#!/bin/bash
#Author: Nicolas Nunez
#Comments: Install Redis from sources (from Redis site)
wget https://download.redis.io/redis-stable.tar.gz
tar -xzvf redis-stable.tar.gz && cd redis-stable
sudo make
#Because it's a good idea
#sudo make test
#Install binaries in /usr/local/bin
sudo make install







