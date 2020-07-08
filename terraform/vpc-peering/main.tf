resource "google_compute_network_peering" "local_network_peering" {
  provider             = google
  name                 = var.name
  network              = var.network
  peer_network         = var.peernetwork




}