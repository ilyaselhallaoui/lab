# KodeKloud Engineer - Linux Solutions (Project3 - level 1)

## Task: Create a User on App Server 1

### Requirements:
In response to the latest tool implementation at `xFusionCorp Industries`, the system admins require the creation of a service user account.
Here are the specifics:

Create a user named `mariyam` in `App Server 1` without a home directory.

### Solution:
To solve this problem, we are going onto the App server 1, and then create the user mariyam (also specify for her to not have any home directory).
1. App Server 1:
    a) ssh tony@stapp01 -> provide password if prompted
  	b) sudo useradd -M -d /nonexistent mariyam -> this let's you generate the user
        mariyam on the server, through the user add command.
        The -M option, allows you to have no home directory, and through the -d option, you still create a Path to /nonexistent.



### Notes:
This one was very easy, since we are still in the stage of creatuing and adding users :).
