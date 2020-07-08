
resource "google_container_cluster" "test-primary" {
  name     = var.name
  location = var.location
  network            = var.network
  subnetwork = var.subnetwork
  # We can't create a cluster with no node pool defined, but we want to only use
  # separately managed node pools. So we create the smallest possible default
  # node pool and immediately delete it.
  remove_default_node_pool = var.remove_default_node_pool
  initial_node_count       = var.initial_node_count
  project = var.project
  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = var.issue_client_certificate
    }
  }
}
