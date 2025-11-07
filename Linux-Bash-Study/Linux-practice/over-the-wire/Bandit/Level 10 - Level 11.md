# Bandit Wargame: Level 10 to Level 11

## Challenge Description
The password for the next level is stored in the file data.txt, which contains base64 encoded data.



### Details:
- **Username**: `bandit10`
- **Password**: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Connect via ssh:
      ssh bandit10@bandit.labs.overthewire.org -p 2220
3. Now provide the password when prompted
4. Now run:
  cat data.txt | base64 --decode
First we gotta print the files content, using the cat comand. Then we pip the output of this to decode the base64 encoded data,
to make it human readable and get the password :)
9. now copy the password and exit

Password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

## Key take aways:
Before solving this challenge, I didn't know about the string command and how it isused. Also I could again practice the usage of pipelines in connection with the grep command.
