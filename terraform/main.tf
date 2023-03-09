terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.56.0"
    }
  }

  required_version = ">= 1.3.9"
}

provider "aws" {
  region = var.amazon_region 
}

# Create a VPC
resource "aws_vpc" "lineage_classess_vpc" {
  cidr_block = var.vpc_cidr_block 
  
  tags = {
    Name = "lc_vpc"
  }
} 

resource "aws_subnet" "lineage_classes_subnet" {
  vpc_id            = aws_vpc.lineage_classess_vpc.id
  cidr_block        = var.vpc_cidr_block
  availability_zone = var.azs

  tags = {
    Name = "lc_subnet"
  }
}

resource "aws_internet_gateway" "lineage_classes_gw" {
  vpc_id = aws_vpc.lineage_classess_vpc.id

  tags = {
    Name = "lc_igw"
  }
}

resource "aws_route_table" "lc_route" {
  vpc_id = aws_vpc.lineage_classess_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.lineage_classes_gw.id
  }

  tags = {
    Name = "lc_rt"
  }
}

resource "aws_route_table_association" "lc_route_associate" {
  subnet_id      = aws_subnet.lineage_classes_subnet.id
  route_table_id = aws_route_table.lc_route.id
}

resource "aws_security_group" "access_for_lc_vpc" {
  name        = "Allow access"
  description = "Allow inbound traffic"
  vpc_id      = aws_vpc.lineage_classess_vpc.id

  ingress {
    description      = "Security group for VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "SG for LC-VPC"
  }
}

resource "aws_security_group_rule" "http" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  security_group_id = aws_security_group.access_for_lc_vpc.id
}

resource "aws_instance" "lineage_classes_server" {
  ami           = "ami-0557a15b87f6559cf"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.lineage_classes_subnet.id
  associate_public_ip_address = true
  key_name = "lineage_web_server"
  vpc_security_group_ids = [aws_security_group.access_for_lc_vpc.id]

  tags = {
    Name = var.instance_name
  }
}
