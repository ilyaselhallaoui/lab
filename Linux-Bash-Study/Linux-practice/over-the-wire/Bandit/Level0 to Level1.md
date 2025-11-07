# Bandit Wargame: Level 0 to Level 1

## Challenge Description
The goal of Level 0 to Level 1 is to connect to the Bandit server via SSH. This challenge introduces the concept of logging into a remote server
using a username and password.

### Details:
- **Username**: `bandit0`
- **Password**: bandit0
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit0@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted

## Key take aways:
Through this challenge you now know, how to SSH into a remote server. The general structure is:
```bash
ssh <user>@<hostname> <-p and port number, if you want to>

In our example bandit0 is the user, bandit.labs.overthewire.org is the hostname and 2220 is the port number.
