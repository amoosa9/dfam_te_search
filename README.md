# 410.712_final_project
My final project for Advanced Practical Computer Concepts for Bioinformatics

To upload Dfam RepeatModeler Data to the Database:

1. Get the path of the FASTA RepeatModeler output file.
2. Run the upload_te.py script using the FASTA file's path as the input (-i)
   parameter and the genus and species of the organism as the -g and -s
   parameters, respectively.
3. When the script terminates, the data will be added to the mySQL database
   and can be accessed.
