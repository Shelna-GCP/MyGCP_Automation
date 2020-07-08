# setup the GCP provider | provider.tf

provider "google" {
  project = var.project
  credentials = file(var.gcp_auth_file)
  region  = var.gcp_region_1
  zone    = var.gcp_zone_1
  version = "~> 3.25"
}
