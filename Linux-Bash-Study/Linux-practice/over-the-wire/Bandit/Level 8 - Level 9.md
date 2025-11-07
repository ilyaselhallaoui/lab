# Bandit Wargame: Level 8 to Level 9

## Challenge Description
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once



### Details:
- **Username**: `bandit8`
- **Password**: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Connect via ssh:
      ssh bandit8@bandit.labs.overthewire.org -p 2220
3. Now provide the password when prompted
4. Now runto find the unique line: 
      sort data.txt | uniq -u
-> this sorts the data in the file in alphabetical order and then let's you filter out, if there are doubles.
9. now copy the password and exit

Output to be expected: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM


## Key take aways:
Before solving this challenge, I didn't know about the sort command and the uniq command.
Sort: Sorts the data in an alphabetical order, which leads to dupliact3es being adjacent- The uniq command then filters out the unique line.
