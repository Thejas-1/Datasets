##1) Clone/Download these datasets and sore them in the same folder as matlab is insalled.

##2) Then execute the heat diffusion equation by changing the path in the first line to that 
   of each of the files.

In order to download the datasets from Web of Science,

1) Enter Web of Science through login details and enter the following query into the 
   advanced query bar:
   
   OG = 'Institution_Name' and TS = 'Name_of_the_topic'
   
   and click on the option to search.

2) You'll receive a new page consisting of a set of papers corresponding to the entered query.

3) Filter the result to a particular insitution by selecting one from the list in the left hand
   side of the page.

4) click of the option of 'Create citations report' on he top right hand corner.
 
5) Uncheck the option of 'self citations' from the new page and then click on 'analyze results'.

6) Select the option to filter results by time and then download the datasets. 

7) The downloaded datasets will be in .txt format(name of he file will be analyze.txt). 

8) In order to filter the datasets, erase the first and the last lines from the .txt file, copy the
   file to the same folder as that of 'analyzer.py' and execute 'python2.7 analyzer.py'. 
 
9) You will be asked for a file name. Enter the name in which you want to store the file(Keep the 
   format as .csv).

10) Your file will be saved. Go to steps ##1 and ##2 for using the datasets in the matlab equation.

Please note: The datasets are for plotting the graph of influence diffusion in the domain of astronomy.
             Moreover, the graphs measure the spread of influence from Harvard University to the rest whose
  	     names are mentioned as file names of the csv files.