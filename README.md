# DistanceCalculator

## Description :

This Application will help you to identify the customers whose location are with in the given range from a source point. 
The locations are specified using the latitude and longitude.

## Features : 

1. The application can communicate with the user using files or through command line interface. Users can specify it via parameters. Users can provide the input via files and receive the output via commandline interface and vice versa is also possible. The code can be extended to support to any other input and output types.
2. The output can be sorted using different parameters like, user_id, name and distance of the customer from source using -so and -sp parameter .
3. All the parameters can be sorted either ascending or descending order. The users can specify them separately. 
4. You can use -h command for help which will provide you all the parameters and their usecase.

## Installation :
### Requirements :
		
1. Install java 1.5 and above.
2. Install latest maven. 
	
### Steps to install:
1. Download the github code from the repo 
>**git clone https://github.com/kannanshan/DistanceCalculator.git**
2. Move to the repository folder with the following command . 
>**cd DistanceCalculator**
3. Build the project using maven. Output will be a jar file located inside the target folder. 
>**mvn clean install**
		
## Execution : 

1. Once installation is done. We are ready to execute the application.
2. Command to execute : 
>**java -jar target/distancecalculator.jar -d 100 -s 53.339428 -6.257664**
3. We expect a file named input.txt containing the customers information in json format inside the directory. File with sample data is already present in the directory.
4. The output will be written to a file named output.txt in the same directory.
5. If you want the input and output file from a different directory , you can create a directory with input.txt and output.txt and set the working directory using the -w command.
6. If you want to use the command line for input and output, you can set the same using the -i and -o commands.
	
	
## Synopsis : 

1. Input the Distance range and the source coordinates in lat,long. 
		The input is read from the file named input.txt and outputs are written to the file named outputs.txt
>**java -jar distancecalculator.jar -d 100 -s 53.339428 -6.257664**
		
2. If you want to change the input via command line interface use the below command. 
		Default is vis files.
>**java -jar distancecalculator.jar -d 100 -s 53.339428 -6.257664 -i command_line -o file**
		
3. If you want to change the sort order using the name or distance from the source use the below command. 
		Default is using the id.
>**java -jar distancecalculator.jar -d 100 -s 53.339428 -6.257664 -i command_line -o file -sp name -so asc**
		
4. If you want to change the working directory use the below command. 
		Default is the current directory.
>**java -jar distancecalculator.jar -d 100 -s 53.339428 -6.257664 -i command_line -o file -sp name -so asc -w /Users/Kannan/Desktop**
		
## Help : 

 * usage: java -jar distancecalculator.jar (-h help)  (-d distance range in km) (-s latitude longitude) (-w working directory) (-so sorting order asc or desc) (-sp sorting parameter id or name or dis) (-i inputtype file or command_line) (-o outputtype file or command_line)
 	* -d  : Distance range to be measured. The values are in Kilometers. data type : double 
 	* -s  : Source coordinates. The source is generally provided using latitude and longtidue in degrees. data type : double 
 	* -w  : Working directory.data type : String . Default value : Current directory
 	* -so : Sorting order. asc or desc. data type : String . Default value : Ascending
	* -sp : Sorting parameter. id or name or dis (distance from source). data type : String . Default Value : user_id
 	* -i  : Input type. file or command_line. data type : String . Default value : File
 	* -o  : Output type. file or command_line. data type : String . Default value : File
 	* -h  : Help command. Will list all the supported commands and parameters
 
 * Distance range and source coordinates are  Mandatory Parameters 
 
 
 
## Test case inputs and outputs

### Missing data : 
1. Missing Distance.
	* Input : java -jar target/distancecalculator.jar -s 53.339428 -6.257664
	* Output : Invalid input. -d  parameter is missing or the range is < 0 or > 10000: check the help menu using the -h command to understand the inputs

2. Missing source cordinates.
	* Input : java -jar target/distancecalculator.jar -d 100
	* Output : Invalid input. -s parameter is missing : check the help menu using the -h command to understand the inputs
	
3. File not found.
	* Input : java -jar target/distancecalculator.jar -d 100 -s 53.339428 -6.257664
	* Output : Input file not found. Please check the working directory and the file with name input.txt


### Invalid data : 
1. Invalid json data in file.
	* Input : java -jar target/distancecalculator.jar -d 100 -s 53.339428 -6.257664
	* Output : Invalid customer data format. Please make sure the inputs are in proper json format. Please find the sample: "{"latitude": "52.986375", 		"user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}"

2. Improper parameter names.
	* Input : java -jar target/distancecalculator.jar -d 100 -s 53.339428 -6.257664
	* Output : Invalid customer data format. Please make sure the inputs are in proper json format. Please find the sample: "{"latitude": "52.986375", 		"user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}"

3. Distance should be less than 10000 km
	* Input : java -jar target/distancecalculator.jar -d 10000 -s 53.339428 -6.257664
	* Output : Invalid input. -d  parameter is missing or the range is < 0 or > 10000: check the help menu using the -h command to understand the inputs

4. Lat/Long value between the perimissible range
	* Input : java -jar target/distancecalculator.jar -d 10000 -s 153.339428 -6.257664	
	* Output : Latitude value should be in the range -90 to 90

### Success case :

inputs.txt file : 


		{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-8.522366"}
		
		
		{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}
		
		
		{"latitude": "52.986375", "user_id": 2, "name": "Ian McArdle", "longitude": "-6.043701"}
		
		
		{"latitude": "53.807778", "user_id": 3, "name": "Jack Enright", "longitude": "-7.714444"}

1. Success case. 
	* Input : java -jar target/distancecalculator.jar -d 100 -s 53.339428 -6.257664
	* Output : { "name" : "Ian McArdle", "user_id" : 2 }

2. Empty results.
	* Input : java -jar target/distancecalculator.jar -d 10 -s 53.339428 -6.257664
	* Output : {}

3. Empty results.
	* Input : java -jar target/distancecalculator.jar -d 1000 -s 53.339428 -6.257664
	* Output : {}

4. Sort the outputs based on the  user id : ascending order
	* Input : java -jar target/distancecalculator.jar -d 200 -s 53.339428 -6.257664
	* Output : {"user_id":2, "name":Ian McArdle"} {"user_id":3, "name":Jack Enright"} {"user_id":12, "name":Christina McArdle"}

5. Sort the outputs based on the  user id : descending order	
	* Input : java -jar target/distancecalculator.jar -d 200 -s 53.339428 -6.257664 -so desc
	* Output : {"user_id":12, "name":Christina McArdle"} {"user_id":3, "name":Jack Enright"} {"user_id":2, "name":Ian McArdle"}

6. Sort the outputs based on the  user name : ascending order	
	* Input : java -jar target/distancecalculator.jar -d 200 -s 53.339428 -6.257664 -sp name -so asc
	* Output : {"user_id":12, "name":Christina McArdle"} {"user_id":2, "name":Ian McArdle"} {"user_id":3, "name":Jack Enright"}

7. Sort the outputs based on the distance from the source : ascending order	
	* Input : java -jar target/distancecalculator.jar -d 200 -s 53.339428 -6.257664 -so desc -sp dist
	* Output : {"user_id":12, "name":Christina McArdle"} {"user_id":3, "name":Jack Enright"} {"user_id":2, "name":Ian McArdle"}

8. Output the results in Command line. 
	* Input : java -jar target/distancecalculator.jar -d 200 -s 53.339428 -6.257664 -o command_line
	* Output : {"user_id":2, "name":Ian McArdle"} {"user_id":3, "name":Jack Enright"} {"user_id":12, "name":Christina McArdle"}
	   
9. Input from Command line and output to file. 
	* Input : java -jar target/distancecalculator.jar -d 200 -s 53.339428 -6.257664 -o command_line -i file
	* Output : {"user_id":2, "name":Ian McArdle"} {"user_id":3, "name":Jack Enright"} {"user_id":12, "name":Christina McArdle"}
 

 
		
		
		
		
		
		
		
		
		
		
		
