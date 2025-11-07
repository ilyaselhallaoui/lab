# Bandit Wargame: Leve 5 to Level 6

## Challenge Description
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
human-readable
1033 bytes in size
not executable




### Details:
- **Username**: `bandit5`
- **Password**: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`

---

## Solution Steps

1. Open your terminal.
2. Use the `ssh` command to connect to the server:
   ```bash
   ssh bandit5@bandit.labs.overthewire.org -p 2220
3. Now provide the password if prompted
4. Go into the into the inhere directory: cd inhere
5. to view files run: ls
6. to identify the file we need run: find . -type f -size 1033c ! -perm /111 -exec file {} + | grep 'text' -> output : ./maybehere07/.file2
7. now: cd maybehere07
8. ls -a -> to view all files (also hidden)
8. cat .file2
7. now copy the password and exit

The Output of this file should be: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG


## Key take aways:
Through this challenge I now know how to view hidden files, how the find and file command works and I could work with pipelines and the grep command. :)
