# Digital meter

My Raspberry Pi collects the usage data of my electrical meter, every second.
The script P1uitlezen.py cleans this data and sends the clean JSON data to my webserver through its API (http://165.227.215.102:8000/restapi/)
My webserver collects all this data in its database.
For a visual representation, we read the data of our today usage and calculate the hourly usage.
This data gets represented in a graph, using Chart.js (http://165.227.215.102:8000/)

## DONE

- Install RPi in closet + SSH 
- Git setup
- Read data
- Clean data
- Create API
- Communicate with API
- Show data through interface
- Setup webserver
- Migrate to webserver
- Run RPI-script on startup in background
- Run webserver in background
- Secure API

## TO DO
