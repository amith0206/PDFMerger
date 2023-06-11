# PDF Merger
The PDF Merger is a Python script that allows you to merge multiple PDF files into a single PDF document using the PyPDF2 library.

# Prerequisites
Python 3.x
PyPDF2 library

# Usage
Place the PDF files you want to merge in the same directory as the script.
Run the script using the command python main.py (replace main.py with the actual name of your script).
Follow the prompts:
Enter the name of the PDF file you want to merge (including the file extension '.pdf').
Enter 'q' to discontinue adding more files or 'y' to continue adding files.
Once you're done adding files, the script will merge them into a single PDF named 'merged.pdf' in the same directory.
The merged PDF will be saved, and you'll see a message indicating the completion of the process.

# License
This project is licensed under the terms of the MIT License. See the LICENSE file for more details.

# Limitations
The script assumes that the PDF files to be merged are located in the same directory as the script. If the files are in a different directory, you need to provide the correct file path.
The PyPDF2 library might have limitations on the types of PDF files it can merge, such as encrypted or password-protected files.

# Acknowledgements
I would also like to extend my thanks to the open-source community for their continuous support and contributions to the PyPDF2 library. The collaborative nature of the community has allowed me to benefit from the library's capabilities and enhance my work.
