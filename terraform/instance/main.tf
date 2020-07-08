
# Create VM #1
resource "google_compute_instance" "web_private_1" {
  name         = var.name
  machine_type = var.machine_type
  zone         = var.zone
  project      = var.project


  boot_disk {
    initialize_params {
      image = var.sourceimage
    }
  }

  network_interface {
    subnetwork    = var.subnet
    subnetwork_project = var.subnetproject
  }
}