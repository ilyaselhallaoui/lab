# Bandit Wargame: Leve 4 to Level 5

## Challenge Description
The password for the next level is stored in the only human-readable file in the inhere directory. 
ip: if your terminal is messed up, try the “reset” command.




### Details:
- **Username**: `bandit4`
- **Password**: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit4@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. Go into the into the inhere directory: cd inhere
5. to view files run: ls
6. to identify the human readable file: file ./* ->(file with ASCII)
8. cat <human readable file>
7. now copy the password and exit

The Output of this file should be: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw


## Key take aways:
Through this challenge I now know, how to view  human readble files!
