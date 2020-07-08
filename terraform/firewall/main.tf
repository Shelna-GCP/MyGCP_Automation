resource "google_compute_firewall" "firewall" {
  name    = var.name
  network = var.network
  project = var.project

  allow {
    protocol = var.protocol
    ports    = var.ports
  }

}