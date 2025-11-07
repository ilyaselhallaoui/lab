# Bandit Wargame: Leve 2 to Level 3

## Challenge Description
The password for the next level is stored in a file called spaces in this filename located in the home directory


### Details:
- **Username**: `bandit2`
- **Password**: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit2@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. List the contents of home directory: ls
4. Now cat the file called spaces in the filename (use qoutation marks)
      to do this prompt: cat "spaces in the filename"

The Output of this file should be: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx


## Key take aways:
Through this challenge you now know, how to open a file, with spaces in the name. For this you have to utilize qoutation marks.
