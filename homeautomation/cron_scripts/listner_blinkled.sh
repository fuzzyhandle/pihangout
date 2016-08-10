#!/bin/bash
/usr/bin/docker run --rm --cap-add SYS_RAWIO --device /dev/mem -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -e PYTHONUNBUFFERED=1 -v /HDPiAutomation/listner_blinkled:/data hrishikesh/tweepy4iot /usr/bin/python /data/listner_blinkled.py

