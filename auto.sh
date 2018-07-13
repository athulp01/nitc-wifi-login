#!/bin/bash

if [ 'iwgetid -r | grep C_Hostel' ]; then
	.login.py
fi
