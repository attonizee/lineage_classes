variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "LineageClassesWebServer"
}

variable "amazon_region" {
  description = "Value of Amazon region for resources"
  type = string
  default = "us-east-1"
}

variable "azs" {
  description = "Describe Availability Zones"
  type = string
  default = "us-east-1b"
}

variable "vpc_cidr_block" {
  description = "Define CIDR block for VPC"
  type = string
  default = "192.168.0.0/16"
}

variable "private_subnets" {
    description = "Describe private subnets for VPC"
    type = string
    default = "192.168.10.0/24"
}

variable "public_subnets" {
  description = "Describe public subnets for VPC"
  type = string
  default = "192.168.20.0/24"
}