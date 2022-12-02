Ansible setup lab 6:
====================

Setup control node
------------------

1. Pick one of the ec-2 instance we created in Lab 5 as control node

2. Connect to the control node

3. Switch to root user
```
sudo -i
```
4. Update the package list
```
yum update -y
```
5. Create a new user ansible-user
```
useradd ansible-user
password ansible-user
password123
```

6. Add privileges to the user ansible-user
```
usermod -aG wheel ansible-user
```

7. Switch to that user
```
su - ansible-user
```

4. Now generate ssh keys
```
ssh-keygen
press enter three times to accept all the defaults.
```

5. Now enable password based authentication
```
nano /etc/ssh/sshd_config
Change the following two lines 
#PasswordAuthentication yes
to
PasswordAuthentication yes

and
PasswordAuthentication no
to
PasswordAuthentication yes

ctrl+x
save changes
exit

Now restart sshd
systemctl restart sshd
```

5. Now install Ansible 
sudo amazon-linux-extras install ansible2 -y 

6. verify ansible Setup
ansible --version

7. Create a folder in home directory i.e.
cd
mkdir ansible-dir
cd ansible-dir
touch hosts


