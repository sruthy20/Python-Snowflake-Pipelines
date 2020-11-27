import requests
import json
import snowflake.connector

class Snowdataload():
    
    def __init__(self):
        
        self.connectionstring={
        'user':'UserName',
        'password':'PassWord!',
        'account':'Full Account Name',
        'warehouse':'Warehouse Name',
        'database':'DB_Name',
        'schema':'PUBLIC'
        }
       
        self.URL='https://jsonplaceholder.typicode.com/todos'
        
    def getdata(self):        # method for webscraping
        
        
        try:
            response=requests.get(self.URL)
            data=response.json()
        
        except requests.exceptions.RequestException as e: 
            print('Something is wrong !', e)
        
        else:
            
            self.dbcreate()
            self.dbinsert(data)
                          
        
    def dbcheck(self):       # method for snowflake connection check
        
        self.conn=snowflake.connector.connect(**self.connectionstring)
        cur=self.conn.cursor()
        Checkquery="SELECT current_version();" 
        
        try: 
            cur.execute(Checkquery)
            result = cur.fetchone()
        except snowflake.connector.errors.ProgrammingError as e:
            print(e)
        else:
            print('*** DB connection response *** : ',result)
                
        finally:
            cur.close()
                
    def dbcreate(self):     # method to create database objects
        
        
        createSQL="create table if not exists User_Details (userId int, id int,title varchar(100),completed varchar(50)); "
        cur=self.conn.cursor()
        try: 
            cur.execute(createSQL)
            resu=cur.fetchall()
        except snowflake.connector.errors.ProgrammingError as e:
            
            print(e)
        else:
            print('*** Response of DB object creation *** : ',resu)

        finally:
            cur.close()
            
   
    def dbinsert(self,data):  # methods to insert data
        
        cur=self.conn.cursor()
        try:
            
            for i in data:
            
                insert_query="insert into User_Details (USERID,ID,TITLE,COMPLETED) values (%s,%s,%s,%s); "
                val=(i['userId'],i['id'],i['title'],i['completed'])
                cur.execute(insert_query,val)
                result=cur.fetchall()
                
                
        except snowflake.connector.errors.ProgrammingError as e:
            
            print(e)
        
        else:
            print(result)
            self.conn.commit()
            
        finally:
            cur.close()
            self.conn.close()
            print('************ Database connection is closed ***********')

            
def main():
    
    load=Snowdataload()       # object creation
    load.dbcheck()            # Establish snowflake connection
    
    load.getdata()           # Web scraping to get data from the URL
    
    
    
if __name__=='__main__':
      main()


    


