#File Handling
#How to Read a Text, and Write into it using python code


#Function - which function to read a file
#inbuilt function - open()
#open("file_name" , "mode")

#Mode -
#r - for reading (Default)
#w - for writing (creates a b=new file or truncates an existing one)
#a - for appending
#b - for binary mode. zoom.exe - binary
#+ - for updating (reading and writing)

#Read and Write Content
#Read a file
#Reading Entire Content : Content = file_object.read()
#line = file_object.readline() for a single line.
#lines = file_objecy.readlines() for all lines in a list.
#Close the file


file = open("TestData",'r') #opens the file from txt file we created
content = file.read() #read the file
print(content) #print the output
file.close() #closes the file