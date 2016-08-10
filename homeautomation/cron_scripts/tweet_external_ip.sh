#/bin/bash
/usr/bin/docker run --rm --cap-add SYS_RAWIO --device /dev/mem  -e PYTHONUNBUFFERED=1 -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -v /HDPiAutomation/job_tweetexternal_ip:/data hrishikesh/tweepy4iot /usr/bin/python /data/tweetexternal_ip.py
