import os

#Locating file
os.chdir(r'[path to file]')
        #[path to file] contains the path to locating the file to be read
        # Ex. C:\Users\name\Downloads 

#Reading the file
vaccine = open('[file1.txt]', 'r', encoding='utf-8')
        #[file1.txt] is the text file to be read
content = vaccine.read()
        #Reading the text inside the file
content_split = content.split()
        #Splitting the string into separate substrings with space as its delimiter
#Writing content

with open('[file2.txt]', 'w', encoding='utf-8') as file:
        #[file2.txt] serves as the file that will be written on
        for w in content_split:
                if "[word]" in w:
                        file.write(str(w))
                        file.write('\n')
                #[word] is the desired string to be searched for in content_split

vaccine.close()