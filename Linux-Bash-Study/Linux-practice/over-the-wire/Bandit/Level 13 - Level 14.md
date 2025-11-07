# Bandit Wargame: Level 13 → Level 14

## Level Goal
The password for the next level is stored in `/etc/bandit_pass/bandit14` and can only be read by user `bandit14`. For this level, you don’t get the next password directly, but you receive a private SSH key that can be used to log into the next level.

> **Note:** `localhost` is a hostname that refers to the machine you are working on.

## Solution Steps

### 1. Connect to the Bandit Server
First, establish an SSH connection to the Bandit server using the credentials from Level 12:
```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
```
**Password:** `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

### 2. Locate the SSH Key
After logging in, check for an SSH private key file:
```bash
ls -la
```
If found, it will be used to authenticate as `bandit14`.

### 3. Set the Correct File Permissions
SSH private keys require proper permissions to work correctly. Adjust the key's permissions:
```bash
chmod 600 sshkey.private
```

### 4. Use the SSH Key to Log in as `bandit14`
Use the provided private SSH key to connect to `bandit14` on `localhost`:
```bash
ssh -i sshkey.private bandit14@localhost -p 2220
```

### 5. Retrieve the Password for the Next Level
Once logged in as `bandit14`, read the stored password:
```bash
cat /etc/bandit_pass/bandit14
```
This will display the password for `bandit15`.

## Solution Output
The final password retrieved is:
```
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
Use this password to log in to the next level!

---

## Key Takeaways
- Used SSH to connect to the Bandit server.
- Located and used a private SSH key to switch users securely.
- Adjusted file permissions (`chmod 600`) to allow key-based authentication.
- Successfully retrieved the next level's password.

Proceed to **Level 14** with the obtained password! 🚀

