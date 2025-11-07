# Bandit Wargame: Leve 6 to Level 7

## Challenge Description
The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size





### Details:
- **Username**: `bandit6`
- **Password**: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit6@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. Now run: find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
5. tnext cd into the output: cd /var/lib/dpkg/info
6. ls | grep "bandit"
7. next : cat bandit7.password
9. now copy the password and exit

The Output of this file should be: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG


## Key take aways:
Through this challenge I now know how to filter certain files, used grep.
