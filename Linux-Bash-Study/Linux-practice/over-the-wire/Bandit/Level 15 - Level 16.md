# Bandit Wargame: Level 15 → Level 16

## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port `30001` on `localhost` using SSL/TLS encryption.

**Helpful Note:** If you encounter messages like `DONE`, `RENEGOTIATING`, or `KEYUPDATE`, refer to the `CONNECTED COMMANDS` section in the `man` page for further guidance.

---

## Solution Steps

### 1. Connect to the Bandit Server
Establish an SSH connection to the Bandit server using the provided credentials:

```sh
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

Password:
```
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

### 2. Submit the Password to Port 30001 using SSL/TLS
Once logged in, use `ncat` with the `--ssl` flag to securely send the current password to port `30001` on `localhost`:

```sh
echo "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" | ncat --ssl localhost 30001
```

### 3. Retrieve the Next Level's Password
After sending the password, the server responds with the password for the next level:

```
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```

### 4. Use the New Password for the Next Level
Now, use the retrieved password to log in to Level 16:

```sh
ssh bandit16@bandit.labs.overthewire.org -p 2220
```

Password:
```
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```

---

## Key Takeaways
- Used `ncat` with `--ssl` to send data securely over a network connection.
- Interacted with a local service using encrypted communication.
- Successfully retrieved and used the password for the next level.

Proceed to Level 16 with the obtained password! 🚀
