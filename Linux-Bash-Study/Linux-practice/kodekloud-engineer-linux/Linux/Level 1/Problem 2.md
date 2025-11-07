# KodeKloud Engineer - Linux Solutions (Project2 - level 1)

## Task: Create a User on App Server 2

### Requirements:
The system admin team at `xFusionCorp Industries` has streamlined access management by implementing group-based access control. Here's what you need to do:

a. Create a group named `nautilus_noc` across all App servers within the `Stratos Datacenter`.
b. Add the user `jarod` into the `nautilus_noc` group on all App servers. If the user doesn't exist, create it as well.

###Solution:
To solve this problem, we are going onto the servers one by one and we are gonna create a group and a user, inside the group.
1. App Server 1:
    a) ssh tony@stapp01 -> provide password if prompted
  	b) sudo useradd jarod -> this let's you generate the user jarod on the server
    c) sudo groupadd nautilus_noc -> group nautilus_noc is then genrated
    d) sudo usermod -aG nautilus_noc jarod -> this let's you add the user jarod to the group nautilus_noc
2. App Server 2:
    a) ssh steve@stapp02 -> provide password if prompted
  	b) sudo useradd jarod -> this let's you generate the user jarod on the server
    c) sudo groupadd nautilus_noc -> group nautilus_noc is then genrated
    d) sudo usermod -aG nautilus_noc jarod -> this let's you add the user jarod to the group nautilus_noc
1. App Server 3:
    a) ssh banner@stapp03 -> provide password if prompted
  	b) sudo useradd jarod -> this let's you generate the user jarod on the server
    c) sudo groupadd nautilus_noc -> group nautilus_noc is then genrated
    d) sudo usermod -aG nautilus_noc jarod -> this let's you add the user jarod to the group nautilus_noc



### Notes:
This one was very easy, but generally it was just bad, that I didn't know/still know how it is possible to add the user/group at alls ervers at once.
