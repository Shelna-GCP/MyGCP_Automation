from gcpautoutil.executeTerraform import executedeployment
from gcpautoutil.flagconstants import sheetdictmap, boolfields, strfields, deployment_execution_order, listfields


def writetoterraform(fieldvaldict, resource):
    """
    Function to generate a .tfvars file for resources
    :param fieldvaldict: dictionary of values
    :param resource: resource getting deployed
    :return:
    """
    with open('terraform/' + resource + '/terraform.tfvars', 'w+') as f:
        for i in fieldvaldict:
            if i in boolfields:
                strf = i + ' = ' + str(fieldvaldict[i]) + '\n'
            elif i in strfields:
                strf = i + ' = ' + '"' + str(fieldvaldict[i]).lower() + '"\n'
            elif i in listfields:
                strf = i + ' = ' + '[' + str(fieldvaldict[i]).lower() + ']\n'
            else:
                strf = i + ' = ' + '"' + str(fieldvaldict[i]) + '"\n'

            f.write(strf)
            f.flush()


def mapwithvalues(sheetname, fielddict):
    """
    The function is to map with the values
    :param sheetname: sheetname from excel
    :param fielddict: dictionary of values
    :return: dictionary
    """
    fieldvaldict = dict()
    print fielddict.keys()
    for field in fielddict.keys():
        try:
            print str(field).strip()
            fieldvaldict[sheetdictmap[sheetname][str(field).strip()]] = fielddict[field]
        except KeyError as ke:
            continue
    return fieldvaldict


def mapwithterraform(vardict, sheetname):
    """

    :param vardict:
    :param sheetname:
    :return:
    """
    if sheetname == deployment_execution_order[2]:
        subdict = vardict['SUBNET']
        vpcdict = vardict[sheetname]

        # mapping for vpc
        fieldvaldict = mapwithvalues(sheetname, vpcdict)
        print fieldvaldict

        writetoterraform(fieldvaldict, 'vpc')
        networkname = fieldvaldict['name']
        project = fieldvaldict['project']
        region = fieldvaldict['region']

        executedeployment('vpc')
        # mapping for subnet
        for subnum in subdict:
            fieldvaldict = mapwithvalues(sheetname, subdict[subnum])

            if 'network' not in fieldvaldict.keys():
                fieldvaldict['network'] = networkname
                fieldvaldict['project'] = project
                fieldvaldict['region'] = region
            writetoterraform(fieldvaldict, 'subnet')
            executedeployment('subnet')

    if sheetname == deployment_execution_order[1]:
        providerdict = vardict[sheetname]
        # mapping for provider
        fieldvaldict = mapwithvalues(sheetname, providerdict)
        print fieldvaldict
        writetoterraform(fieldvaldict, 'provider')
        executedeployment('provider')

    if sheetname == deployment_execution_order[3]:
        instancedict = vardict[sheetname]
        # mapping for instance
        fieldvaldict = mapwithvalues(sheetname, instancedict)
        writetoterraform(fieldvaldict, 'instance')
        executedeployment('instance')

    if sheetname == deployment_execution_order[4]:
        firewalldict = vardict[sheetname]
        # mapping for firewall
        fieldvaldict = mapwithvalues(sheetname, firewalldict)
        writetoterraform(fieldvaldict, 'firewall')
        executedeployment('firewall')

    if sheetname == deployment_execution_order[5]:
        peerdict = vardict[sheetname]
        # mapping for peering
        fieldvaldict = mapwithvalues(sheetname, peerdict)
        resourcepath = r'projects/'+fieldvaldict['project']+'/global/networks/'
        network = fieldvaldict['network']
        peernet = fieldvaldict['peernetwork']
        projectid = fieldvaldict['project']
        newnet = resourcepath+network
        newpeernet = resourcepath + peernet
        fieldvaldict['network'] = newnet
        fieldvaldict['peernetwork'] = newpeernet
        writetoterraform(fieldvaldict, 'vpc-peering')
        executedeployment('vpc-peering')

    if sheetname == deployment_execution_order[6]:
        nodedict = vardict['NODE']
        clusterdict = vardict[sheetname]

        # mapping for vpc
        fieldvaldict = mapwithvalues(sheetname, clusterdict)

        writetoterraform(fieldvaldict, 'gke_cluster')
        clustername = fieldvaldict['name']

        executedeployment('gke_cluster')
        # mapping for subnet
        for subnum in nodedict:
            fieldvaldict = mapwithvalues(sheetname, nodedict[subnum])

            if 'cluster' not in fieldvaldict.keys():
                fieldvaldict['cluster'] = clustername
            writetoterraform(fieldvaldict, 'gke_node')
            executedeployment('gke_node')
