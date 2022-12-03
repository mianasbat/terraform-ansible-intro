Ansible setup lab 6:
====================

Setup control node

1. Pick one of the ec-2 instance we created in Lab 5 as control node

2. Connect to the control node

3. Switch to root user

.. code:: bash

	$ sudo -i
	# 

1. Update the package list

.. code:: bash

	# yum update -y

1. Create a new user ansible-user

.. code:: bash

	# useradd ansible-user
	# password ansible-user
    # password123

1. Add privileges to the user ansible-user

.. code:: bash

	# usermod -aG wheel ansible-user


1. Switch to that user

.. code:: bash

	# su - ansible-user
	$

1. Now generate ssh keys

.. code:: bash
	
	ssh-keygen
	press enter three times to accept all the defaults.


1. Now enable password based authentication

.. code:: bash
	
	sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
	systemctl restart sshd


1. Now install Ansible 

.. code:: bash

	sudo amazon-linux-extras install ansible2 -y 

6. verify ansible Setup

.. code:: bash

	ansible --version

7. Create a folder in home directory i.e.

.. code:: bash
	
	cd
	mkdir ansible-dir
	cd ansible-dir
	touch hosts


