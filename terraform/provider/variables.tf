# Google Cloud connection & authentication and Application configuration | variables.tf

# GCP authentication file
variable "gcp_auth_file" {
  type = string
  description = "GCP authentication file"
}

# define GCP project name
variable "project" {
  type = string
  description = "GCP project name"
}

variable "gcp_region_1" {
  type = string
  description = "region"
}

variable "gcp_zone_1" {
  type = string
  description = "zone"
}