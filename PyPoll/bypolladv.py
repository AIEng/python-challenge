import os
import csv
import operator

vote = 0
khan = 0
Correy = 0
Li = 0
nt=0
OTooley = nt
candidates = []
Final_Result = {}
vote_percent= {}

election_data = os.path.join(".", "election_data.csv")

#this is a useless message
#opening CSV file
with open(election_data,newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
#looping in csv to get the total vote and candidates name
   for row in csvreader:
        vote = vote + 1
        if row[2] not in Final_Result:
            candidates.append(row[2])
            Final_Result[row[2]]=1  
        elif row[2] in candidates:
            Final_Result[row[2]]+=1      
            
#calculating each candidate votes and percetnage 
totalvotes=sum(Final_Result.values())


for key, value in Final_Result.items():
    vote_percent[key] = str(round(((value/totalvotes) * 100), 3)) + "% ("+str(value) + ")"
    

#creating a dictionary for results 
result = dict(zip(candidates, result))


print (f'Election Results\n-------------------------\nTotal Votes:{vote}')
print (' -------------------------')
print (f'Khane: {khan_percent}% ({khan})')
print (f'Correy: {Correy_percent}% ({Correy})')
print (f'Li: {Li_percent}% ({Li})')
print (f'OTooley: {OTooley_percent}% ({nt})')
print (' -------------------------')
print (f'Winner:{max(Final_Result.items(), key=operator.itemgetter(1))[0]}')


#write result to a text file

output_path = os.path.join(r'C:\Users\engmo\Desktop\PREWORK_MIQ\Module-3\poll_data.txt')

with open(output_path,'w', newline='') as txtfile:
    
    
    txtfile.write(f'Election Results\r\n')
    txtfile.write('-------------------------\r\n')
    txtfile.write(f'Total Votes:{vote}\r\n')
    txtfile.write("----------------------------------------\r\n")
    txtfile.write(f'Khane: {khan_percent}% ({khan})\r\n')
    txtfile.write(f'Correy: {Correy_percent}% ({Correy})\r\n')
    txtfile.write(f'Li: {Li_percent}% ({Li})\r\n')
    txtfile.write(f'OTooley: {OTooley_percent}% ({nt})\r\n')
    txtfile.write("----------------------------------------\r\n")
    txtfile.write(f'Winner:{max(results.items(), key=operator.itemgetter(1))[0]}')




