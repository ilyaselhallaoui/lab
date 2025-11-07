# Bandit Wargame: Leve 7 to Level 8

## Challenge Description
The password for the next level is stored in the file data.txt next to the word millionth




### Details:
- **Username**: `bandit7`
- **Password**: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit7@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. Now run: cat data.txt | grep "millionth"
9. now copy the password and exit

The Output of this file should be: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc


## Key take aways:
Through this challenge I now know how to grep stuff.
