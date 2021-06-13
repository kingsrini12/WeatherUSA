This Python program get the weather data using a API and moves the data to S3

This requires the followng package to be imported, Please use the followng commands to install the packages.

pip install requests
pip install boto3
pip install datetime

====================

Run python main.py
Enter the City name.
The script create a Weather Report file for the given city and moves to S3.
s
Once Data us moved to S3, Please use the followng commnads to load the s3 files to Redshift table in AWS.

Create a table in RedShift and load the files from S3 using the below commands:

create table WeatherData 
(
 LoadDate varchar(100),
 longitude varchar(100),
 latitude varchar(100),
 id varchar(100),
  main varchar(100),
description varchar(100),
icon varchar(100),
base varchar(100),
temp varchar(100),
feels_like varchar(100),
temp_min varchar(100),
temp_max varchar(100),
pressure varchar(100),
humidity varchar(100),
visibility varchar(100),
speed varchar(100),
deg varchar(100),
ID1 varchar(100),
cloudsAll varchar(100),
ID_cloud varchar(100),
sunrise varchar(100),
sunset varchar(100),
timezone varchar(100),
id_1 varchar(100),
name varchar(100),
cod varchar(100)
 );

copy WeatherData from 's3://weatherusa/' iam_role 'arn:aws:iam::<AWS ID>:role/<AWS Role>' DELIMITER ',' NULL as '' FILLRECORD IGNOREHEADER 1;

select loaddate, name, * from WeatherData order by loaddate, name;
