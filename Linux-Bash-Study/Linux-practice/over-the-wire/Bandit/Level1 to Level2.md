# Bandit Wargame: Level 1 to Level 2

## Challenge Description
The password for the next level is stored in a file called - located in the home directory


### Details:
- **Username**: `bandit1`
- **Password**: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit1@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. Now cat the file called -
      to do this prompt: cat ./-
The Output of this file should be: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx


## Key take aways:
Through this challenge you now know, how to open a dashed file name. For this you pu ./ in front.

- is the filename, and you prompt ./- to open file.
