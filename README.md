# DocTableToCSV
Turns a Word File Table into a CSV Document. 

This project is a Python script that extracts data from tables within a .docx file and converts it to a .csv file. The script ignores rows that contain the words "Subcategory" or "Cod" in the first column. This feature was added to address a WixStores export issue, but can easily be adjusted or removed.

# Requirements:
Python 3.6+ | python-docx

Install the required dependencies by running: pip install python-docx

# Usage
Save your .docx file containing tables in the same folder as the script or provide the correct path.

# Run the script
python doc2.py

The generated .csv file will be saved in the same directory.

# Configuration
Edit the function call docx_table_to_csv to specify the input and output paths: docx_table_to_csv("file.docx", "output.csv")


# Update gen3:
gen3 is another python file, which, when combined with doc2, makes it easier to create product categories in bulk for WixStores, since Wix does not have this option itself. While doc2 generates the CSV of Categories (collection), gen3 adapts the file to the Wix Template.
