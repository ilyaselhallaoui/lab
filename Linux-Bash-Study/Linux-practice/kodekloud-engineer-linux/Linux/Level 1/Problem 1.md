# KodeKloud Engineer - Linux Solutions (Level 1)

## Task: Create a User on App Server 2

### Requirements:
- Create a user named **yousuf** on **App Server 2** in **Stratos Datacenter**.
- Set UID to **(UID not recorded)**.
- Set home directory to **/var/www/yousuf**.

### Solution:

1. **Access the App Server 2 via SSH:**
   ssh yousuf@serverapp02
   (Replace `serverapp02` with the actual hostname or IP of the server)

2. **Provide the required password when prompted.**

3. **Create the user with the specified UID and home directory:**
   useradd -u <UID> -d /var/www/yousuf yousuf

   (Replace `<UID>` with the correct user ID value)

4. **Set a password for the user:**
   passwd yousuf

5. **Verify that the user was created correctly:**
   id yousuf
   ls -ld /var/www/yousuf

### Notes:
I found that the biggest obstacle here was understanding structure of the project, like data centers, etc. Everything else was fairly easy, since this is Level 1.
