variable "project" {
  description = "The ID of the project where this VPC will be created"
  default =""
}

variable "region" {
  description = "The region"
  default = ""
}

variable "name" {
  description = "The name of the network being created"
  default = ""
}

variable "routing_mode" {
  type        = string
  default     = "GLOBAL"
  description = "The network routing mode (default 'GLOBAL')"
}

variable "shared_vpc_host" {
  type        = bool
  description = "Makes this project a Shared VPC host if 'true' (default 'false')"
  default     = false
}

variable "ip_cidr_range" {
  type        = string
  description = "ip range"
  default = ""
}
variable "ip_cidr_range1" {
  type        = string
  description = "ip range"
  default = ""
}
variable "network" {
  type        = string
  description = "ip range"
  default = ""
}

variable "auto_create_subnetworks" {
  type        = bool
  description = "When set to true, the network is created in 'auto subnet mode' and it will create a subnet for each region automatically across the 10.128.0.0/9 address range. When set to false, the network is created in 'custom subnet mode' so the user can explicitly connect subnetwork resources."
  default     = false
}

variable "delete_default_internet_gateway_routes" {
  type        = bool
  description = "If set, ensure that all routes within the network specified whose names begin with 'default-route' and with a next hop of 'default-internet-gateway' are deleted"
  default     = false
}

variable "access_config" {
  type        = string
  description = "access config"
  default     = ""
}

variable "metadata" {
  type        = string
  description = "metadata"
  default     = ""
}
