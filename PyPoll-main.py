#Homework 3 Python_Challenge

#Import Dependencies 
import os 
import csv 

# Set Path For File 
csvpath = os.path.join("..","Pypoll", "Resources", "election_data.csv")

# Open & Read CSV File 
with open(csvpath, newline="") as csvfile:

#Define Variables 
    total_votes = 0 
    Khan_votes = 0 
    Correy_votes = 0 
    Li_votes = 0 
    Otolley_votes = 0 

#csv Reader Specifies the delimiter & Variable that holds the contents 
csvreader = csv.reader(csvfile, delimiter= ".")

#Header Row will be read first (If there is no Header Skip)
csv_header = next(csvreader)
row = next(csvreader)

#Read Row of data after Header 
for row in csvreader:

#Calculate number of Votes Cast 
    total_votes +=1

#Calculate number of Votes Candidate Won
if(row[2] == "Khan"):
    Khan_votes += 1
elif (row[2] == "Correy"):
    Correy_votes += 1 
elif (row[2] == "Li"):
    Li_votes += 1
else:
    Otolley_votes += 1 

#Calculate Percentage of Votes Candidate Won
    Khan_percent = Khan_votes / total_votes
    Correy_percent = Correy_votes / total_votes
    Li_percent = Li_votes / total_votes
    Otolley_percent = Otolley_votes/ total_votes


#Calculate Winner 
winner = max(Khan_votes, Correy_votes, Li_votes, Otolley_votes)
if winner == Khan_votes:
    winner_name = "Khan"
elif winner == Correy_votes:
    winner_name = "Correy"
elif winner == Li_votes:
    winner_name = "Li"
else:
    winner_name = "Otolley"

#Print Data
    print(f"Election Results")
    print(f"----------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------------")
    print(f"Khan {Khan_percent:.3%}({Khan_votes})")
    print(f"Correy {Correy_percent:.3%}({Correy_votes})")
    print(f"Li {Li_percent:.3%}({Li_votes})")
    print(f"O'tooley {Otooley_percent:.3%}({Otooley_votes})")
    print(f"----------------------------------------")
    print(f"Winner:{winner_name}")
    print(f"------------------------------------------")

#Revised Data with Winner Info 
output_file = os.path.join(".","Pypoll", "Resources", "election_data.csv")

#Open File 
with open(output_file, "w",) as txtfile:

#Print New Data 
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Total Votes {total_votes}\n")
    txtfile.write(f"--------------------------\n")
    txtfile.write(f"Khan {Khan_percent:.3%}({Khan_votes})")
    txtfile.write(f"Correy {Correy_percent:.3%}({Correy_votes})")
    txtfile.write(f"Li {Li_percent:.3%}({Li_votes})")
    txtfile.write(f"O'tooley {Otooley_percent:.3%}({Otooley_votes})")
    txtfile.write(f"----------------------------------------")
    txtfile.write(f"Winner: {winner_name}")
    txtfile.write(f"------------------------------------------")