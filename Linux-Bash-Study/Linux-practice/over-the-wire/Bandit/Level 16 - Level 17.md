# Bandit Level 16 → Level 17 Walkthrough

## Objective
The credentials for the next level can be retrieved by submitting the current level's password to a service listening on localhost on a port in the range **31000 to 32000**. Among these services:
- Some will echo back the input.
- Some will use SSL/TLS.
- Only **one correct port** will provide the next level’s credentials.

---

## **Step 1: Find Open Ports**
We start by scanning for open ports in the range 31000-32000:

```bash
nmap -p 31000-32000 localhost
```

Example output:
```
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```

---

## **Step 2: Determine if Each Port Uses SSL/TLS or Plaintext**
For each port, we check:
1. **Plaintext test** (Using `nc` - netcat):
   ```bash
   nc localhost <PORT>
   ```
   If nothing happens, it's likely an SSL/TLS port.

2. **SSL/TLS test** (Using `openssl s_client`):
   ```bash
   openssl s_client -connect localhost:<PORT>
   ```
   If we see a successful SSL handshake, the port is using SSL/TLS.

From our tests:
- **Ports 31046 & 31691** gave an "unexpected message" error → Not SSL.
- **Ports 31518 & 31790** had a valid SSL handshake.

---

## **Step 3: Submitting the Password to Each SSL Port**
We need to send the current level’s password to each valid SSL port.

Using **port 31518**:
```bash
echo "<CURRENT_PASSWORD>" | openssl s_client -connect localhost:31518 -quiet
```
Output:
```
Wrong! Please enter the correct current password.
```
This means the port is **not the correct one**.

Using **port 31790**:
```bash
echo "<CURRENT_PASSWORD>" | openssl s_client -connect localhost:31790 -quiet
```
Output:
```
Correct!
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
```

This confirms that **port 31790 is the correct port** and has returned an **RSA private key** for the next level.

---

## **Step 4: Saving and Using the RSA Key**
1. Copy the **entire private key**, including `BEGIN RSA PRIVATE KEY` and `END RSA PRIVATE KEY`.
2. Save it as a file:
   ```bash
   nano bandit17_key.pem
   ```
   - Paste the private key inside.
   - Save the file (`CTRL + X`, then `Y`, then `Enter`).
3. **Set the correct file permissions:**
   ```bash
   chmod 600 bandit17_key.pem
   ```
4. **SSH into Bandit17 using the private key:**
   ```bash
   ssh -i bandit17_key.pem bandit17@bandit.labs.overthewire.org -p 2220
   ```
   If successful, you are now in **Bandit Level 17**! 🎉

---

## **Summary**
✅ Used `nmap` to identify open ports.
✅ Checked each port for plaintext or SSL/TLS.
✅ Identified **port 31790** as the correct one.
✅ Submitted the password and received an **RSA private key**.
✅ Used the private key to SSH into Bandit Level 17.

You’ve successfully completed **Bandit Level 16 → Level 17**! 🚀
