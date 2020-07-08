
resource "google_container_node_pool" "extra-pool" {
  name               = var.name
  location               = var.location
  cluster            = var.cluster
  project = var.project
  initial_node_count = var.initial_node_count
}