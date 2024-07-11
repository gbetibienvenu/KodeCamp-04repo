KCVPC Setup Guide
Objective
Design and set up a Virtual Private Cloud (VPC) with both public and private subnets in the AWS EU-West-1 (Ireland) region. Implement routing, security groups, and network access control lists (NACLs) to ensure proper communication and security within the VPC.
Steps
1. Create a VPC
VPC Dashboard in the AWS Management Console.
Click on "Create VPC".
Configure the following settings:
Name tag: KCVPC
IPv4 CIDR block: 10.0.0.0/16
Tenancy: Default
Click "Create VPC".
2. Create Subnets
Public Subnet
In the VPC Dashboard, I select "Subnets" then click on  "Create Subnet".
Configuration  settings:
Name tag: PublicSubnet
VPC: KCVPC
Availability Zone: Then I Select  one  from the region
IPv4 CIDR block: 10.0.1.0/24
I click on  "Create Subnet".
Private Subnet
In the VPC Dashboard, I select "Subnets" then  I click on  "Create Subnet".
Configuration settings:
Name tag: PrivateSubnet
VPC: KCVPC
Availability Zone: I select the same as the Public Subnet for simplicity
IPv4 CIDR block: 10.0.2.0/24
Then click "Create Subnet".
3. Configuration of  Internet Gateway (IGW)
In the VPC Dashboard, I select "Internet Gateways" then I click "Create internet gateway".
Configuration  settings:
Name tag: KCVPC-IGW
then click on  "Create internet gateway".
Attachment of  the IGW to KCVPC:
I select the created IGW.
Then I click on  "Actions" as well ,I select "Attach to VPC".
I choose KCVPC and click "Attach internet gateway".
4. Configuration of the  Route Tables
Public Route Table
In the VPC Dashboard,I select "Route Tables" then I click "Create route table".
Configuration  settings:
Name tag: PublicRouteTable
VPC: KCVPC
I click  on "Create route table".
Association of  the PublicSubnet with this route table:
I select the ‘created route table’.
Then I click on  "Subnet associations" and then on  "Edit subnet associations".
I select PublicSubnet and then  click on "Save associations".
Adding of the  Route to the IGW:
I select the route table.
Clicked on  "Routes" and then on  "Edit routes".
Clicked on  "Add route".
Configuration settings:
Destination: 0.0.0.0/0
Target: KCVPC-IGW
Click "Save routes".
Private Route Table
In the VPC Dashboard,I  select "Route Tables" and then  clicked on  "Create route table".
Configuration settings:
Name tag: PrivateRouteTable
VPC: KCVPC
Then Clicked on  "Create route table".
Association of  the PrivateSubnet with this route table:
I select  ‘created route table’.
Then Clicked "Subnet associations" and then on  "Edit subnet associations".
Also I select PrivateSubnet and then  clicked on  "Save associations".
5. Configuration of  NAT Gateway
In the VPC Dashboard,I  select "NAT Gateways" and clicked on  "Create NAT gateway".
Configuration settings:
Subnet: PublicSubnet
Elastic IP allocation ID: Clicked on  "Allocate Elastic IP" and then on  "Allocate" to get a new Elastic IP.
Click "Create NAT gateway".
Updating of  the PrivateRouteTable to the route internet traffic to the NAT Gateway:
I select the PrivateRouteTable.
Clicked on  "Routes" and then on  "Edit routes".
Clicked on  "Add route".
Configuration settings:
Destination: 0.0.0.0/0
Target: I select the created NAT Gateway
Clicked on  "Save routes".
6. Set Up of the  Security Groups
Public Security Group
In the VPC Dashboard,I  select "Security Groups" and then clicked on  "Create security group".
Configuration settings:
Security group name: PublicSG
Description: Security group for public instances
VPC: KCVPC
Click "Create security group".
Configure inbound rules:
Allow inbound HTTP (port 80) and HTTPS (port 443) traffic from anywhere (0.0.0.0/0).
Allow inbound SSH (port 22) traffic from a specific IP (e.g., your local IP).
Allowing  all outbound traffic.
Private Security Group
In the VPC Dashboard, I select "Security Groups" and then clicked on "Create security group".
Configuration settings:
Security group name: PrivateSG
Description: Security group for private instances
VPC: KCVPC
Clicked on  "Create security group".
Configure the  inbound rules:
Allow inbound traffic from the PublicSubnet on required specific  ports 
Allow all outbound traffic.
7. Network ACLs
Public Subnet NACL
In the VPC Dashboard, I select "Network ACLs" and click "Create network ACL".
Configure the following settings:
Name tag: PublicNACL
VPC: KCVPC
Clicked on  "Create".
Configure the binbound rules:
Allow inbound HTTP (port 80), HTTPS (port 443), and SSH (port 22) traffic.
Configure outbound rules:
Allow all outbound traffic.
Private Subnet NACL
In the VPC Dashboard, I select "Network ACLs" and click "Create network ACL".
Configure the following settings:
Name tag: PrivateNACL
VPC: KCVPC
Clicked on  "Create".
Configure the inbound rules:
Allow inbound traffic from the public subnet.
Configure outbound rules:
Allow outbound traffic to the public subnet and the internet.
Deliverables
A diagram of the VPC architecture, showing the VPC, subnets, route tables, and security configurations. 
A brief explanation of the purpose and function of each component created:
VPC: A virtual network dedicated to your AWS account.
Subnets: Subdivision of the VPC for organizing and securing resources.
IGW: Enables internet access for the VPC.
NAT Gateway: Allows private subnets to access the internet securely.
Route Tables: Directs traffic within the VPC.
Security Groups: Virtual firewalls for instances.
NACLs: Additional layer of security for subnets.


![image](https://github.com/gbetibienvenu/KodeCamp-04repo/assets/64703165/91e7609b-40d9-4756-b5e4-1084b6a15ca0)



