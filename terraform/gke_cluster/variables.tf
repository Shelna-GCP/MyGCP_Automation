# Google Cloud connection & authentication and Application configuration | variables.tf

# GCP authentication file
variable "name" {
  type = string
  description = "GCP cluster name"
   default =""
}

# define GCP project name
variable "project" {
  type = string
  description = "GCP project name"
   default =""
}

variable "network" {
  type = string
  description = "network"
  default =""
}

variable "subnetwork" {
  type = string
  description = "subnetwork"
  default =""
}

variable "location" {
  type = string
  description = "location / zone"
  default =""
}

variable "initial_node_count" {
  type = number
  description = "count of nodes"
  default = 1

}

variable "issue_client_certificate" {
  type = bool
  description = "issue_client_certificate"
  default =false
}

variable "remove_default_node_pool" {
  type = bool
  description = "remove_default_node_pool"
  default =true
}
