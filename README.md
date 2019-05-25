# ExcelDataToSQL

If you need to copy data from excel and create table this little python script will help you.
To run this you need python 3
Originally created on python 3.7.3
Just copy your excel data into "import.txt" and run the script.
It will generate the create table statement and insert into.


*Warning 

It needs to be formated in following way-
Table name is in the first line after "table="
In this sample I called table "Sample"

Afterwards you need to set type for your id and other fields.
*Disclaimer- your ID field needs to be called ID for this script to work.

Then you put the values in. Values and fields need to be separeted using tab.

table=Sample  
ID=number	SampleField1=varchar2  
1	TextSample  
2	TextSample  
3	TextSample  
4	TextSample  
5	TextSample  


As for length- for now I set length(10) for number and length(200) for varchar2. For other types length is 50.
You can modify it in parseData.py in function generateCreate(name, fieldNames)

Only varchar2 and number data types are working as of right now. 

After script is done you will be able to find your queries in file "queries.txt"
