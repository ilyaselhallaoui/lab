# Bandit Wargame: Level 11 to Level 12

## Challenge Description
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z)
letters have been rotated by 13 positions





### Details:
- **Username**: `bandit1`
- **Password**: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Connect via ssh:
      ssh bandit1@bandit.labs.overthewire.org -p 2220
3. Now provide the password when prompted
4. Now run:
  cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m’
First we gotta print the files content, using the cat comand. Then we pip the output of this to be translated.
Here it works the following way, we first define what needs to be translated (A-Za-z).
After this we provide the sets we wanna translate to, since the alphabet has 26 letters
and it is all shifted by 13, we can just shift the order in what needs to be translated (N-ZA-M).
This let's the system know it should shift the letters by 13 :).

9. now copy the password and exit

Password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

## Key take aways:
Before solving this challenge, I did not know about the tr command.
