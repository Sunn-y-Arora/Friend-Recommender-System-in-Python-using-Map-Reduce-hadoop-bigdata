# Friend-Recommender-System-in-Python-using-Map-Reduce-hadoop-bigdata

People You may Know / Friend Recommender from the given data set (Stanfor CS)

To run this you need a 

	1. System with Hadoop installed on it.

	2. hadoop-streaming.jar 

Open the terminal and start hadoop

Step 1. First create an empty directory in your hdfs (hadoop)

	hdfs dfs -mkdir "name of directory"

Step 2. Put the dataset file inside the directory created

	hdfs dfs -put "path for dataset"  directory\

Step 3. Make your mapper.py and reducer.py exectuables

	chmod +x mapper.py
	chmod +x reducer.py

Step 4. Starting the mapReduce 

hadoop jar ../hadoop-streaming.jar -input ../inputDirectory -output ../outputDirectory -mapper ../mapper.py -reducer ../reducer.py

the output directory wil be automatically created and if it already exits remove it first or give another name for output directory

Step 5. Displaying Results
	hdfs dfs -cat outputDirect/part-r-00000     

	Note*** In some versions it may be part-00000 so change it accordingly. ***

To copy the result into local HDD 

	hdfs dfs -getmerge outputDir/   ../name.txt
