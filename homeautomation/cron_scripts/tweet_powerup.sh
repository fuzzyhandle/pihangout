#!/bin/bash
/usr/bin/docker run --rm --cap-add SYS_RAWIO --device /dev/mem -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -e PYTHONUNBUFFERED=1 -v /HDPiAutomation/job_tweetpowerup:/data hrishikesh/tweepy4iot /usr/bin/python /data/tweetpowerup.py
