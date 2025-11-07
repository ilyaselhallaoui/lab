s# Bandit Wargame: Leve 3 to Level 4

## Challenge Description
The password for the next level is stored in a hidden file in the inhere directory.




### Details:
- **Username**: `bandit3`
- **Password**: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit3@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. List the contents of home directory: ls
5. navigate to the inhere directory: cd inhere
6. to view hidden files run: ls -a
7. now run: cat .hidden to view the cat file
8. save the password and exit

The Output of this file should be: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ


## Key take aways:
Through this challenge you now know, how to view and open hidden files.
