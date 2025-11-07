# Bandit Wargame: Level 12 to Level 13

## Challenge Description
The password for the next level is stored in a compressed file that has been compressed multiple times. Your task is to extract the password by recursively decompressing the file.

---

## Solution Steps

### 1. Connect to the Bandit server
```sh
ssh bandit12@bandit.labs.overthewire.org -p 2220
```
Password: `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

### 2. Create a Temporary Working Directory
To avoid clutter and ensure a clean workspace, create a temporary directory:
```sh
mktemp -d
```
Example output:
```sh
/tmp/tmp.qyRcuMZbOE
```
Navigate into the directory:
```sh
cd /tmp/tmp.qyRcuMZbOE
```

### 3. Copy `data.txt` into the Temporary Directory
```sh
cp ~/data.txt .
```

### 4. Reverse the Hexdump
The provided file is in a hexdump format. Convert it back to its original binary format:
```sh
xxd -r data.txt > original_file
```

### 5. Identify the Compression Format
Use the `file` command to check the file type:
```sh
file original_file
```
Based on the output, extract the file accordingly:

- **gzip:**
  ```sh
  mv original_file original_file.gz
  gunzip original_file.gz
  ```
- **bzip2:**
  ```sh
  mv original_file original_file.bz2
  bzip2 -d original_file.bz2
  ```
- **tar:**
  ```sh
  mv original_file original_file.tar
  tar -xf original_file.tar
  ```
- **xz:**
  ```sh
  mv original_file original_file.xz
  unxz original_file.xz
  ```

### 6. Repeat Steps for Each Compressed File
The file will go through multiple decompression layers. Use `file` after each extraction and proceed accordingly.

Files encountered:
1. `data6.bin`
2. `data6.bin.out`
3. `data8.bin`

After fully decompressing, the final file will be identified as ASCII text.

### 7. Retrieve the Password
Once the final file is an ASCII text file, display its content using:
```sh
cat final_filename
```
The password will be printed on the screen.

---

## Solution Output
After completing all decompression steps, the final password is:
```
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

Use this password to log in to the next level.

---

## Key Takeaways
- Used `mktemp -d` to create a temporary workspace.
- Converted a hexdump file back to its original form with `xxd -r`.
- Identified file types with `file` and extracted them iteratively.
- Learned about multiple compression formats (`gzip`, `bzip2`, `tar`, `xz`).
- Successfully retrieved the password after handling multiple decompression layers.

---

Proceed to **Level 13** with the obtained password!

