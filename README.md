# 410.712_final_project
Dfam RepeatModeler Transposable Element Search


Description

A webpage that allows a user to navigate transposable element data from Dfam's RepeatModeler program. The data is stored in a mySQL database and is accessed using a webpage. The database is already populated with transposable element data for Uraeginthus cyancephalus, and more data can be added using an included script.


Requirements

Mozilla Firefox - This project was developed and tested using Firefox 87.0.
Other browsers may work but have not been validated.

JavaScript supported and enabled – This project uses AJAX for its interactive features, so JavaScript must be enabled in the browser for it to work properly.


Accessing the webpage to search the database

1. Go to the URL http://bfx3.aap.jhu.edu/amoosa1/final/search.html

2. Type in the name of a Dfam element type or family. A link is provided on the webpage to Dfam's classification site to find the different element types and families.

3. (Optional) Type in a DNA sequence to narrow down the results. The webpage will search for elements that match both the type/family and the sequence that are inputted.

4. To search only by sequence, leave the type/family field blank and simply type in a sequence.

5. Click ‘Submit’ to view results in the web browser. Click ‘Download’ to send the results to a FASTA file. Note that both ‘Submit’ and ‘Download’ give results based on what is typed into the search boxes.


To upload Dfam RepeatModeler Data to the Database:

Transposable element data for U. cyanocephalus is available with this project’s source code as ‘uraCya_rm2.45.fasta’. The contents of this file are already populated in the database. This and other Dfam RepeatModeler output files can be found at https://dfam.org/repository.

1. Download and get the path of the FASTA RepeatModeler output file.

2. Run the upload_te.py script using the FASTA file's path as the input (-i) parameter and the genus and 	species of the organism as the -g and -s parameters, respectively.

3. When the script terminates, the data will be added to the mySQL database and can be accessed.


Location of files on the class server

/var/www/html/amoosa1/final

Source code download from GitHub repository

https://github.com/amoosa9/410.712_final_project
