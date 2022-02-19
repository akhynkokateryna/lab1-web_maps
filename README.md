# Creation of web maps
The file takes four arguments: year when the film was produced, latitude, longitude, and path to database with films.
Then is created a web map with 8 marks with filming locations that were the closest to given location.

To convert locations from database into coordinates, was used library geopy, and to create a map and add layers to it, was used folium.

Example:

`>>> python main.py 2014 49.83826 24.02324 locator1.list`

![web mape image](https://github.com/akhynkokateryna/lab1-web_maps/blob/master/web%20map.png)
