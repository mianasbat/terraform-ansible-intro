EC2 instance from AWS Console:
==============================

In this section we will do a hands on lab to do two tasks. Task 1 is to create an ec2 instance from the AWS Console and task 2 is to destroy the ec2 instance. Follow the following steps to complete the lab.

Create EC2 instance:
--------------------

Step 1: Login to the aws console https://go.aws/3F0QiHo

.. figure:: images/aws-login.png
   :alt: aws login page

Step 2: Search for ec2 in the search box and click EC2 section 

.. figure:: images/ec2-section.png
   :alt: ec2 section


Step 3: Click instances from the left menu 

.. figure:: images/instances-section.png
   :alt: instances section

Step 4: Click launch instance button to start creating ec2 instance

.. figure:: images/launch-instance.png
   :alt: launch-instance

Step 5: Give name of the instance

.. figure:: images/ec2-name.png
   :alt: ec2-name

Step 6: The key name will be selected and automatically downloaded to your computer. Now click the launch button to create the instance.

.. figure:: images/launch-button.png
   :alt: click launch button

Step 7: A new page will appear showing the confirmation of ec2 instance creation. Click instances to go to the instances section.

.. figure:: images/instance-created.png
   :alt: instance created successfully


Step 8: The newly created EC2 instance will appear in the ec2 instances list.

.. figure:: images/ec2-instance-final.png
   :alt: instance created successfully


Destroy EC2 instance:
---------------------

Now we will delete/destroy the newly created EC2 instance. The steps are

Step 1: Click the check box in front of the EC2 instance you want to destroy.

.. figure:: images/destroy-1.png
   :alt: Select the instance

Step 2: Click the `Instance state` button and then from the menu click `Terminate instance` button.

.. figure:: images/destroy-2.png
   :alt: click terminate button

Step 3: Click `Terminate` button again to confirm termination.

.. figure:: images/terminate-3.png
   :alt: verify terminate

Step 4: Green verification message will verify that the instance is successfully terminated. The instance will disappear after some time.

.. figure:: images/terminate-4.png
   :alt: Termination complete