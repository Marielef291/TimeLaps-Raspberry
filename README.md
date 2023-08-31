# TimeLaps Raspberry

This project is used to generate a time lapse with a Raspberry.
I used it to create a time lapse of my garden over a year.
I used a Raspberry pi zero 2w with a camera.

## time_lapse_garden.py
It is used to capture a photo from the Raspberry each time the script is triggered.

## transfer_ftp.sh
This file will be used to transfer the photos to a server.

## cron.txt
In crontab I added the lines present in this file in order to trigger a photo every 30 minutes.



<!-- - [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html) -->

