variable "project" {
  description = "The ID of the project where this VPC will be created"
  default = ""
}

variable "region" {
  description = "The region"
}

variable "zone" {
  description = "The zone"
}

variable "name" {
  description = "The name of the network being created"
}

variable "network" {
  type        = string
  default     = ""
  description = "network"
}

variable "peernetwork" {
  type        = string
  description = "peer_network"
  default     = ""
}

variable "description" {
  type        = string
  description = "An optional description of this resource. The resource must be recreated to modify this field."
  default     = ""
}

variable "autocreateroutes" {
  type        = string
  description = "When set to true, the network is created in 'auto subnet mode' and it will create a subnet for each region automatically across the 10.128.0.0/9 address range. When set to false, the network is created in 'custom subnet mode' so the user can explicitly connect subnetwork resources."
  default     = ""
}

variable "delete_default_internet_gateway_routes" {
  type        = bool
  description = "If set, ensure that all routes within the network specified whose names begin with 'default-route' and with a next hop of 'default-internet-gateway' are deleted"
  default     = false
}