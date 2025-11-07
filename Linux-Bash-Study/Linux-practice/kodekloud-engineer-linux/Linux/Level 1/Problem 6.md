# Problem 6: Filter and Relocate User Data on App Server 2

## **Requirement**
Due to an **accidental data mix-up**, user data was unintentionally mingled on **Nautilus App Server 2** at the `/home/usersdata` location by the Nautilus production support team in Stratos DC. The task requires filtering and moving files owned by user `siva` while **preserving the directory structure** to the `/news` directory.

## **Solution**
### **1. Access App Server 2**
```bash
ssh steve@stapp02
```
(Password will be required but is not provided here for security reasons.)

### **2. Locate files owned by `siva`** (excluding directories)
```bash
find /home/usersdata -type f -user siva
```
This command lists all files (not directories) owned by `siva`.

### **3. Copy files while preserving directory structure**
```bash
find /home/usersdata -type f -user siva -exec cp --parents {} /news/ \;
```
- `find`: Searches for files
- `-type f`: Ensures only files are listed (not directories)
- `-user siva`: Filters files owned by `siva`
- `-exec cp --parents {}`: Copies files while maintaining directory structure
- `/news/ \;`: Destination directory

### **4. Verify copied files**
```bash
ls -lR /news/
```
This checks that the files are correctly copied and the structure is preserved.

## **Summary of Commands**
| Step | Description | Command |
|------|-------------|----------|
| Access Server | Connect to App Server 2 | `ssh steve@stapp02` |
| Locate Files | Find files owned by `siva` | `find /home/usersdata -type f -user siva` |
| Copy Files | Copy files to `/news/` while preserving structure | `find /home/usersdata -type f -user siva -exec cp --parents {} /news/ \;` |
| Verify | Ensure files are copied properly | `ls -lR /news/` |

## **Notes**
- The `find` command is efficient for locating files by ownership.
- The `--parents` flag in `cp` ensures the directory structure is maintained.
- Always verify the copied files to avoid missing data.

✅ **Task Completed Successfully** ✅

