# KodeKloud Engineer - Linux Solutions (Project5 - level 1)

## Task: Create a User on App Server 1

### Requirements:
As part of the temporary assignment to the `Nautilus` project, a developer named `kareem` requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed. Here's what you need to do:

Create a user named `kareem` on `App Server 1` in Stratos Datacenter. Set the expiry date to `2024-02-17`, ensuring the user is created in lowercase as per standard protocol.

### Solution:
To solve this problem, we are going onto the App server 1, and then create the user mariyam (also specify for her to not have any home directory).
1. App Server 1:
    a) ssh tony@stapp01 -> provide password if prompted
  	b) sudo useradd -m -e 2024-02-17 kareem -> this let's you generate the user
        kareem on the server, through the user add command.
        The -m option, allows you to have a home directory, and through the -e option and the date, you define when the user
        should be eliminated.



### Notes:
This one was very easy, since we are still in the stage of creatuing and adding users, but it is interesting to reinforce stuff, like how to create temporary users.

