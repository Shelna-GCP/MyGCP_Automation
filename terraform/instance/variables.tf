# vm varibles | vm-variable.tf

# define GCP machine type
variable "machine_type" {
  type = string
  description = "GCP machine type"
}

# define GCP tag
variable "tag" {
  type = list
  description = "tag"
}

# define boot disk
variable "boot_disk" {
  type = string
  description = "boot disk"
  default =""
}

# define region
variable "region" {
  type = string
  description = "region"
}

# define region
variable "zone" {
  type = string
  description = "zone"
}

variable "name" {
  type = string
  description = "name"
}

variable "network" {
  type = string
  description = "network"
  default = ""
}

variable "subnet" {
  type = string
  description = "subnet"
}

variable "sourceimage" {
  type = string
  description = "sourceimage"
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