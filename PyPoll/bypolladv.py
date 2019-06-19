import os
import csv
import operator

vote = 0
candidates = []
Final_Result = {}
vote_percent= {}

election_data = os.path.join(r"c:\users\engmo\desktop\python-challenge\pypoll\election_data.csv")

#opening CSV file
with open(election_data,newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
#looping in csv to get candidates name into a list
#  geting each candidates total votes into a dictnary
   for row in csvreader:
        vote = vote + 1
        if row[2] not in Final_Result:
            candidates.append(row[2])
            Final_Result[row[2]]=1  
        elif row[2] in candidates:
            Final_Result[row[2]]+=1      
            
#Total Votes 
totalvotes=sum(Final_Result.values())

# getting the vote percent for each candidate
for key, value in Final_Result.items():
    vote_percent[key] = str(round(((value/totalvotes) * 100), 3)) + "% ("+str(value) + ")"
 

# printing out the results 
print (f'Election Results\n-------------------------\nTotal Votes:{vote}')
print (' -------------------------')
for key, value in vote_percent.items():
        print(key, ": ", value)
print (' -------------------------')
print (f'Winner:{max(Final_Result.items(), key=operator.itemgetter(1))[0]}')
print (' -------------------------')

#write result to a text file

output_path = os.path.join(r'c:\users\engmo\desktop\python-challenge\pypoll\poll_data.txt')

with open(output_path,'w', newline='') as txtfile:
    
    
    txtfile.write(f'Election Results\r\n')
    txtfile.write('-------------------------\r\n')
    txtfile.write(f'Total Votes:{vote}\r\n')
    txtfile.write("----------------------------------------\r\n")
    for key, value in vote_percent.items():
        txtfile.write((key + ": " + value)+ '\r\n')
    txtfile.write("----------------------------------------\r\n")
    txtfile.write(f'Winner:{max(Final_Result.items(), key=operator.itemgetter(1))[0]}')




