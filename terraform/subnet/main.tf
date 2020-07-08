# create private subnet
resource "google_compute_subnetwork" "subnet" {
  provider      = google
  name          = var.name
  ip_cidr_range = var.ip_cidr_range
  network       = var.network
  region        = var.region
  project       = var.project

}