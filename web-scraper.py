import os
import requests as res

print("web-scraper  v0.1")

#asking for the url
url = input("enter the url you want to scrape(give file url, if you give the direct url it will download the index page.):")

#asking for name of the file
name = input("enter the file name:")

#asking for the directory
dir = input("enter the directory")

#asking for thw user to wait
print("wait..")

#downloading the content
rq = res.get(url)

#making a directory
os.mkdir(dir)

#making a statement for directory at the end
dirst = "check your files in " + dir

#making the dir for making file
dir = dir + "/" + name

#making file
with open(dir , 'w') as f:
    f.write(rq.text)

#print the final statements
print("done!")
print(dirst)