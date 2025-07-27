#Task 2
task2file= input("Enter text to write to the file :")
with open("output.txt",'w') as file:
    file.write(task2file+"\n")
    print("Data succesfully writtne to output.txt\n")

task2file=input('Enter additional text to append:')
with open("output.txt",'a') as file:
    file.write(task2file + "\n")
    print('Data succesfully append.\n')

print('Final content of output.txt:')
task2file=open("output.txt","r")
content= task2file.read()
print(content)
task2file.close()
