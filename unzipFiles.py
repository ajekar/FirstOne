import zipfile
import glob

for f in glob.glob1("D:\Stocks", "*.zip"):
    print(f)
    zip_ref = zipfile.ZipFile("D:\Stocks\\" + f, 'r')
    zip_ref.extractall("D:\Stocks")
    zip_ref.close()



