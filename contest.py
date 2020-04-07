import os
import time
name=str(input("Enter the contest name : "))
try:
    os.mkdir(name)
    time.sleep(1)
    print("Folder created!!!")
except FileExistsError:
    print(f'{name} already exists')
 
try:
    number_of_problems= int(input("Enter the number of problems: "))
except Exception as e:
    print(e)


#To create a path to the folder to create all cpp files
path=f'{name}/'
problems=list()
start=65
while number_of_problems>0:
    problems.append(chr(start))  ##Appends A,B,C,D... and so on to the list depending on the number of the questions
    start+=1
    number_of_problems-=1
## To copy contents of template.cpp to the newly created file ##
for file_names in problems:
    with open(path+file_names+'.cpp','w') as to_create:
        with open('template.cpp','r') as source:
            for line in source:
                to_create.write(line)
    time.sleep(1)
    print(f'Created file {file_names}.cpp in {name}',end='\n')
##Creating additional input and output files ##
with open(path+'input.txt','w') as text:
    pass
time.sleep(1)
print(f'Created input.txt in {name}')
with open(path+'output.txt','w') as text:
    pass
time.sleep(1)
print(f'Created input.txt in {name}')



