#!/bin/bash
#Author: Nicolas Nunez
#Make system "usable"

dnf update -y
dnf install -y sudo ncurses which unzip man wget tar gcc make expect python3-pip python3-devel libpq-devel libaio

