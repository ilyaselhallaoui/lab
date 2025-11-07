# Bandit Wargame: Level 9 to Level 10

## Challenge Description
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.




### Details:
- **Username**: `bandit9`
- **Password**: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Connect via ssh:
      ssh bandit9@bandit.labs.overthewire.org -p 2220
3. Now provide the password when prompted
4. Now run:
  strings data.txt | grep '====’
The string command filters the human readable/printable files, then through the grep command only the lines, which include === signs are printed.
9. now copy the password and exit

Password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

## Key take aways:
Before solving this challenge, I didn't know about the string command and how it isused. Also I could again practice the usage of pipelines in connection with the grep command.
