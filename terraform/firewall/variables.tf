# vm varibles | vm-variable.tf

# define GCP machine type
variable "protocol" {
  type = string
  description = "protocol"
  default =""
}

# define GCP tag
variable "ports" {
  type = list
  description = "ports"
  default =[]
}



# define region
variable "region" {
  type = string
  description = "region"
  default = ""
}

# define region
variable "zone" {
  type = string
  description = "zone"
  default = ""
}

variable "name" {
  type = string
  description = "name"
  default = ""
}

variable "network" {
  type = string
  description = "network"
  default = ""
}

variable "subnet" {
  type = string
  description = "subnet"
  default = ""
}

variable "project" {
  type = string
  description = "project"
  default = ""
}

variable "subnetproject" {
  type = string
  description = "subnetproject"
  default = ""
}