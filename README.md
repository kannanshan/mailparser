# DistanceCalculator

## Description :

This Application will help you to identify the customers whose location are with in the given range from a source point. 
The locations are specified using the latitude and longitude.

## Features : 

1. The application can communicate with the user using files or through command line interface. Users can specify it via parameters. Users can provide the input via files and receive the output via commandline interface and vice versa is also possible. The code can be extended to support to any other input and output types.
2. The output can be sorted using different parameters like, user_id, name and distance of the customer from source.
3. All the parameters can be sorted either ascending or descending order. The users can specify them separately. 
4. You can use -h command for help which will provide you all the parameters and their usecase.

## Installation :
### Requirements :
		
1. Install java 1.5 and above.
2. Install latest maven. 
	
### Steps to install:
1. Download the github code from the repo https://github.com/kannanshan/DistanceCalculator.git
2. Move to the repository folder with the following command . "cd DistanceCalculator"
3. Build the project using maven. Output will be a jar file located inside the target folder . "mvn clean install"
4. Either you can execute the jar in the same folder or move to separate folder.
		
## Execution : 

1. Once installation is done. We are ready to execute the application.
2. Command to execute : java -jar distancecalculator.jar -d 100 -s 53.339428, -6.257664.
3. We expect a file named input.txt containing the customers information in json format inside the directory.
4. The output will be written to a file named output.txt in the same directory.
	
	
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
'''
 		usage: java -jar distancecalculator.jar (-h help)  (-d distance range in km) (-s latitude longitude) (-w working directory) (-so sorting order asc or desc) (-sp sorting parameter id or name or dis) (-i inputtype file or command_line) (-o outputtype file or command_line)
 
-d  : *Distance range to be measured. The values are in Kilometers. data type : double 
-s  : *Source coordinates. The source is generally provided using latitude and longtidue in degrees. data type : double 
-w  : Working directory.data type : String . Default value : Current directory
-so : Sorting order. asc or desc. data type : String . Default value : Ascending
-sp : Sorting parameter. id or name or dis (distance from source). data type : String . Default Value : user_id
-i  : Input type. file or command_line. data type : String . Default value : File
-o  : Output type. file or command_line. data type : String . Default value : File
 
-* : Mandatory Parameters 
'''
 
		
		
		
		
		
		
		
		
		
		
		
