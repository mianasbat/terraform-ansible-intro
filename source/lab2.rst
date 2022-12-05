Setup the environment:
======================

This section describes how to install, verify and configure AWS CLI and Terraform on our systems.

Install Terraform:
------------------

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


Install AWS CLI:
----------------

Steps to install AWS CLI on Mac, Windows and Linux are given on the AWS documentation website https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html. Feel free to install it from the Terraform website or follow the steps as per your operating system. 

Mac:
----

Step 1: Download the package

.. code:: bash

    curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
    

Step 2: Install the package

.. code:: bash

    sudo installer -pkg ./AWSCLIV2.pkg -target /

Step 3: Verify installation

.. code:: bash

    which aws
    aws --version


Windows:
--------

Step 1: To Download and Install the AWS CLI, run the command

.. code:: bash

    choco install awscli


Linux:
------

Step 1: To Download and Install the AWS CLI, run the command

.. code:: bash

    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"


Step 2: Unzip the downloaded package

.. code:: bash

    unzip awscliv2.zip


Step 3: Install the package

.. code:: bash

    sudo ./aws/install


Configure AWS CLI:
------------------

Step 1: Open command prompt on Windows

Step 2: Run the command `aws configure` to start the configuration of AWS CLI. Provided the required details

.. code:: bash

    aws configure
    AWS Access Key ID [None]: PASTE YOUR ACCESS KEY 
    AWS Secret Access Key [None]: PASTE YOUR SECRET KEY
    Default region name [None]: us-east-1
    Default output format [None]: json

