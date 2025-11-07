# Bandit Wargame: Level 14 → Level 15

## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on `localhost`.

## Solution Steps

### 1. Connect to the Bandit Server
First, establish an SSH connection to the Bandit server using the provided credentials:

```sh
ssh bandit14@bandit.labs.overthewire.org -p 2220
```

Password:
```sh
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

### 2. Submit the Password to Port 30000
Once logged in, use Netcat (`nc`) to send the current level's password to `localhost` on port `30000`:

```sh
echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS" | nc localhost 30000
```

### 3. Retrieve the Next Level's Password
Upon submitting the password, the server responds with the password for the next level:

```sh
Correct! 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

### 4. Use the New Password for the Next Level
Now, use the retrieved password to log in to Level 15:

```sh
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

Password:
```sh
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

## Key Takeaways
- Used **Netcat (nc)** to send data over a network connection.
- Sent the current password to a specific port to retrieve the next level's password.
- Learned how to interact with local services using basic networking tools.

Proceed to Level 15 with the obtained password! 🚀

