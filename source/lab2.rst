Install Terraform:
================

Steps to install Terraform on Mac, Windows and Linux are given on the Terraform website https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform. Feel free to install it from the Terraform website or follow the steps as per your operating system. 


Mac:
----

Step 1: Install home brew using the following command, if it is not installed. For more details visit https://brew.sh/

.. code:: bash

	$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Step 2: Install the HashiCorp tap, a repository of all our Homebrew packages.

.. code:: bash

    $ brew tap hashicorp/tap

Step 3: install Terraform with hashicorp/tap/terraform.

.. code:: bash

    $ brew install hashicorp/tap/terraform


Windows:
--------

Step 1: Open powershell with administrative privileges

.. figure:: images/open-powershell.png
   :alt: open-powershell with administrative privileges


Step 2: Run the following command in the powershell to install Chocolatey given on website https://chocolatey.org/install 

.. code:: bash

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

Step 3: Now install terraform using the command

.. code:: bash

    choco install terraform

Step 4: Verify the terraform installation by running the following command to get terraform help.

.. code:: bash

    terraform -help


Linux:
------
Follow the following steps for Ubuntu OS

Step 1: Run the command to update the package list

.. code:: bash

    sudo apt update

Step 2: To install terraform run the command 

.. code:: bash

    sudo apt-get install terraform

Step 3: To verify installation

.. code:: bash

    terraform -help
