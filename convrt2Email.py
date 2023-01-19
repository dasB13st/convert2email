import shutil

# Request name of file list and email domain name
fileList = "empNames.txt" #input ('Name of file list to convert to email: ')
eDomain = "usps.gov" #input ('Name of email domain: ')
# Make copy of file list
source = (fileList)
target = (fileList)+"_COPY"
shutil.copy (source, target)

# read each line of file list and turn into email address
with open((fileList), "r") as reader:
    lines = reader.readlines()
with open("emailList.txt", "w") as writer:
    for line in lines:
        line = line.replace(' ','.')
        modified_line = line.strip() + "@" + (eDomain)
        print(modified_line.lower())
        writer.write(modified_line.lower()+"\n")
