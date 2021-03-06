/******************************************
	VPC configuration
 *****************************************/
resource "google_compute_network" "network" {
  name                            = var.name
  auto_create_subnetworks         = var.auto_create_subnetworks
  routing_mode                    = var.routing_mode
  project                         = var.project
  description                     = var.description
  delete_default_routes_on_create = var.delete_default_internet_gateway_routes
}


