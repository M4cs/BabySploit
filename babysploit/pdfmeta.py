def start():
    from PyPDF3 import PdfFileReader, PdfFileWriter
    import os, glob
    print("Put PDF file in pdfs/")
    print("Which PDF file would you like to read the meta data for?")
    for d in glob.iglob("pdfs/*"):
        if "emptyfile" not in d:
            print(d.replace("pdfs/"))
    ans = str(input("> "))
    if ".pdf" in ans:
        pass
    else:
        ans = ans + ".pdf"
    pdffile = PdfFileReader(file(ans, 'rb'))
    docInfo = pdffile.getDocumentInfo()
    for metaItem in docInfo:
        print("- " + metaItem + ":" + docInfo[metaItem])
    print("\n")