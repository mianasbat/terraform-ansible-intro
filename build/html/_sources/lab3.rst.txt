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
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 4.16"
        }
    }

    required_version = ">= 1.2.0"
    }

    provider "aws" {
    region  = "us-west-2"
    }

    resource "aws_instance" "app_server" {
    ami           = "ami-830c94e3"
    instance_type = "t2.micro"

    tags = {
        Name = "ExampleAppServerInstance"
    }
    }


