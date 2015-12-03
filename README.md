# NYC Taxi Data Analysis


This document contains the descriptions of all the code components present in our system, and how they are meant to be used.  

###The Data:
The NYC taxi data was originally through a Freedom of Information Law (FOIL) request from the New York City Taxi & Limousine Commission (NYCT&L). The dataset is available for download publicly at multiple hosting sites. You can download the data from any of the following links:  
http://www.andresmh.com/nyctaxitrips/  
OR  
https://uofi.app.box.com/NYCtaxidata


###./k-means/  
This folder contains the PySpark code to perform K-means clustering on the txi data, using MLlib. Your system needs to have Spark installed and working to run this. Alternative, it can also be deployed as a spark-job on EMR clusters.  

###./*.ipynb  
The .ipynb files are the IPython notebooks, which are used for data exploration and cleaning, as well as analysis of trends observed in the data. The system needs to have Anaconda installed to run the IPython notebooks. They are split into multiple ode chunks, with chunk performing a particular task. This allows us to execute one task at a time, rather than all at once. These notebooks are also used to create some visualization charts to describe the general trends observed in the data.  

###./visualizations/
This folder contains the visulization code used to generate the Google Map visuals, depicting the most popular taxi-routes in New York City. It leverages JavaScript and HTML, as well as Google Maps API.  

  



