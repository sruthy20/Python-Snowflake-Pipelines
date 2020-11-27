
The below section includes my works done as part of exploring the diverse opportunities of using python and Snowflake data warehouse. Snowflake is a cloud-based data warehouse that provides Software-as-a-Service(SaaS) feature. What makes Snowflake different from the traditional on-premises data warehouse is that it relies completely on the cloud infrastructure with better performance and enhanced security features and ease of data analysis. 

Let's explore the activities done as part of this learning experience.

# 1. Web Scraping ,information extraction and data load into Snowflake datawarehouse objects

The first activity demonstrates a simple python code for Web scraping and extracting information from a URL, establishing the snowflake data warehouse connections, object creations, and finally inserting the extracted data into the snowflake data warehouse. 

To start with this hands-on, the prerequisites include:
* Active Snowflake account
* Python

the various steps involved in this Hands-on includes:

* Step1: Creation of Snowflake account

Create a trial version account in the snowflake datawarehouse. 

* Step2: Installation of Snowflake connector for python

```
pip install  snowflake-connector-python
```

The python code used for creating the pipeline is given above :Webscraping_SnowflakeDB.py

The logic involved in each of the methods is as explained below.

* def __init__() :

All the connections details necessary for this integration and the source URL is initialized in this methods

* def getdata(): 

HTTP requests specified in this method gets the data and store the response in the form of JSON.
 
 *  dbcheck():
 
 This method is for establishing the connection with the snowflake database and to ensure the successful connection
 
 * def dbcreate():
 
 Creates the desired table in the specified schema with a similar structure of data obtained from webscarping
 
 * def dbinsert():
 
 Method for insrting the JSON responses to the table created in the above step
 
 
 
For more information on the snowflake, visit the official site : https://docs.snowflake.com/en/user-guide/intro-key-concepts.html


