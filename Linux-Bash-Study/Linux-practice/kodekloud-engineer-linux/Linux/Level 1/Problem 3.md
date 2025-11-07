# KodeKloud Engineer - Linux Solutions (Project4 - level 1)

## Task: Create a User on App Server 3

### Requirements:
To accommodate the backup agent tool's specifications, the system admin team at `xFusionCorp Industries` requires the creation of a user with a non-interactive shell.
Here's your task:
Create a user named `siva` with a non-interactive shell on `App Server 3`.


###Solution:
To solve this problem, we are going onto the App server 1, and then create the user mariyam (also specify for her to not have any home directory).
1. App Server 1:
    a) ssh banner@stapp03 -> provide password if prompted
  	b) sudo useradd -m -s /usr/sbin/nologin siva
      this let's you generate the user siva on the server, through the user add command.
      -m addon, let's you create a home directory and the -s /usr/sbin/nologin sets the sheel to (/usr/sbin/nologin) this prevents interactive shell.
        



### Notes:
This one was very easy, since we are still in the stage of creatuing and adding users, whilst I slowly learn new stuff like the -s option, which might be useful. :)
