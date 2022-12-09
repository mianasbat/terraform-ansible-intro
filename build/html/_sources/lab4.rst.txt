EC2 instance using Terraform:
=============================

If lab-2 is working fine then you are all good to create EC2 instance using terraform.

Create a directory `terraform-config` in the home directory

.. code:: bash

    mkdir ~/terraform-config

Change directory to terraform-config

.. code:: bash

    cd ~/terraform-config


Create a file `main.tf` and paste the following code in it.


.. code:: bash

    terraform {
        required_version = ">= 1.2.0"
        required_providers {
            aws = {
            source  = "hashicorp/aws"
            version = "~> 4.16"
        }
    }

    provider "aws" {
        access-key="AKIAVJ6RD5VFNOO_DEMO"
        secret_key="BEg4DQzrrbzIVVkjptMpYOaUCBjJwbSuzf9_DEMO"
        region  = "us-west-2"
    }

    resource "aws_instance" "app_server" {
        ami           = "ami-830c94e3"
        instance_type = "t2.micro"
        tags = {
            Name = "ExampleAppServerInstance"
        }
    }


Now run the commands

.. code:: bash

    terraform init
    terraform plan
    terraform apply

Now login to EC console and check the ec2 instances section

To destroy the EC2 instance

run the command

.. code:: bash

    terraform destroy
