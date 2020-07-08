
testflagssubnet = {
    'noofresources': 'No. of Subnets',
    'isresourcename': 'Subnet Name',
    'iscustomsubnet': 'Subnet creation mode',
    'fid': 'Subnet Name',
    'resid':'SUBNET'

    }

testflagcluster = {
    'isdeploy': 'Deployment',
    'noofresources': 'initial_node_count',
    'isresourcename': 'node_name',
    'fid': 'Node Name',
    'resid':'NODE'
    }

vpc_subnet_fields = {

    'Region': 'region',
    'Zone': 'zone',
    # VPC fields
    'VPC Name': 'name',
    'Description': 'description',
    'Subnet creation mode': 'auto_create_subnetworks',
    'Routing Mode': 'routing_mode',
    'Project ID': 'project',
    'Delete default': 'delete_default_routes_on_create',

    # Subnet Fields
    'Subnet Name': 'name',
    'Subnet CIDR': 'ip_cidr_range',
    'Private IP Google Access': 'access_config',
    # 'Flow logs':'',
    # 'Aggregation Interval':'',
    'Additional fields (Include Metadata)': 'metadata',
    # 'Sample rate (%)':''

    }

instance_fields = {

    'Project': 'project',
    'Region': 'region',
    'Zone': 'zone',
    'Instance Name': 'name',
    'Machine Type': 'machine_type',
    'Source Image': 'sourceimage',
    'Subnetwork': 'subnet',
    'SubnetworkProject': 'subnetproject',
    # 'OS Disk Size (GB)': '',
    'Network Tags': 'tag',
    # 'Private IP': '',
    # 'Private IP Range': '',
    # 'Public IP': '',
    # 'Public Name': '',
    # 'Boot Disk (Auto Delete)': '',
    # 'Enable Deletion Protection': '',
    # 'Data Disk Count': '',
    # 'Data Disk Size(GB)': '',
    # 'Data Disk Type': ''
    }

firewall_fields = {
    'name': 'name',
    'network': 'network',
    'protocol': 'protocol',
    'ports': 'ports',
    'project': 'project'
    }

vpc_peering_fields = {
    'Project ID': 'project',
    'Region': 'region',
    'Zone': 'zone',
    'Name': 'name',
    'Network': 'network',
    'Peer Network': 'peernetwork',
    'Auto Create Routes': 'autocreateroutes'
    }

provider_fields = {
    'Project ID': 'project',
    'Region': 'gcp_region_1',
    'Zone': 'gcp_zone_1',
    'Authentication': 'gcp_auth_file'
    }

gke_cluster_node_fields = {
    'name': 'name',
    'network': 'network',
    'subnetwork': 'subnetwork',
    'location': 'location',
    'initial_node_count': 'initial_node_count',
    'project': 'project',
    'Node Name': 'name',
    'Node_project': 'project',
    'Node_initial_node_count': 'initial_node_count'
    }

sheetdictmap = {
    'VPC_Subnet': vpc_subnet_fields,
    'Instance': instance_fields,
    'VPC_Peering': vpc_peering_fields,
    'Provider': provider_fields,
    'Firewall': firewall_fields,
    'GKE_Cluster_Node': gke_cluster_node_fields
    }

boolfields = ['delete_default_routes_on_create', 'access_config']
strfields = ['auto_create_subnetworks', 'project', 'gcp_region_1', 'gcp_zone_1', 'gcp_auth_file', 'autocreateroutes']
listfields = ['tag', 'ports']
digitfields = ['initial_node_count']

getboolval = {
    'Custom': False,
    'Default': True
    }

deployment_execution_order = {1: 'Provider',
                              2: 'VPC_Subnet',
                              3: 'Instance',
                              4: 'Firewall',
                              5: 'VPC_Peering',
                              6: 'GKE_Cluster_Node'
                              }

testresourceflag = {deployment_execution_order[2]: testflagssubnet,
                    deployment_execution_order[6]: testflagcluster,
                    'isdeploy': 'Deployment'

                    }
