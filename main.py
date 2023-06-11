import PyPDF2

pdffiles=[]

while True:
    pdf=input("Enter the pdf file name in .pdf format")
    pdffiles.append(pdf)
    a=input("Enter y to continue and n to discontinue")
    if(a== 'n'):
        break
merger=PyPDF2.PdfMerger()
for filename in pdffiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
pdfFile.close()
print("The merged pdf is saved in merged.pdf")
merger.write('merged.pdf')
