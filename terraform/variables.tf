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