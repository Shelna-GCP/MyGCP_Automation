from gcpautoutil.flagconstants import  getboolval, deployment_execution_order, testresourceflag


#
# def readforclusternodes(df,vardict,index,submaindict,fielddict,moresubnets):
#     subcount, givensubcount = 0, 0
#     for fid, row in df.iterrows():
#
#         if fid == testflags['isdeploy'] and str(row[index]).capitalize() == 'No':
#             vardict.clear()
#             return
#         if fid == testflags['noofnodes']:
#             givensubcount = row[index]
#
#         print fid
#         if testflags['isnodename'] in fid and row[index] != '':
#
#             if subcount == givensubcount:
#                 break
#             subcount = subcount + 1
#             name = fid
#             fid = 'Node Name'
#             moresubnets = True
#             dictsub = dict()
#             submaindict[name] = dictsub
#             vardict['NODE'] = submaindict
#
#         if moresubnets:
#             dictsub[fid] = row[index]
#
#         else:
#             fielddict[fid] = row[index]
#     print vardict
#
#
# def readGCPInput(df, sheet_name, index):
#     submaindict, vardict, fielddict = dict(), dict(), dict()
#     subcount, givensubcount = 0, 0
#     moresubnets = False
#
#     vardict[sheet_name] = fielddict
#
#     if sheet_name == deployment_execution_order[6]:
#         print 'inside'
#         readforclusternodes(df,vardict,index,submaindict,fielddict,moresubnets)
#
#     else:
#
#         for fid, row in df.iterrows():
#
#             if fid == testflags['isdeploy'] and str(row[index]).capitalize() == 'No':
#                 vardict.clear()
#                 return
#
#             if fid == testflags['noofsubnets']:
#                 givensubcount = row[index]
#
#             if fid == testflags['iscustomsubnet']:
#                 row[index] = getboolval[row[index]]
#
#             if testflags['issubnetname'] in fid and row[index] != '':
#                 if subcount == givensubcount:
#                     break
#                 subcount = subcount + 1
#                 name = fid
#                 fid = 'Subnet Name'
#                 moresubnets = True
#                 dictsub = dict()
#                 submaindict[name] = dictsub
#                 vardict['SUBNET'] = submaindict
#
#             if moresubnets:
#                 dictsub[fid] = row[index]
#
#             else:
#                 fielddict[fid] = row[index]
#
#     #print vardict
#     print('------------------------------------------------------------------------------------------------------')
#     return vardict


def readGCPInput(df, sheet_name, index):
    submaindict, vardict, fielddict = dict(), dict(), dict()
    subcount, givensubcount = 0, 0
    moresubnets,checkflag = False, False
    vardict[sheet_name] = fielddict

    if sheet_name in [deployment_execution_order[2],deployment_execution_order[6]]:
        checkflag = True
    for fid, row in df.iterrows():

        if fid == testresourceflag['isdeploy'] and str(row[index]).capitalize() == 'No':
            vardict.clear()
            return

        if checkflag:
            if fid == testresourceflag[sheet_name]['noofresources']:
                givensubcount = row[index]

            if sheet_name == deployment_execution_order[2]:
                if fid == testresourceflag[sheet_name]['iscustomsubnet']:
                    row[index] = getboolval[row[index]]

            if testresourceflag[sheet_name]['isresourcename'] in fid and row[index] != '':
                if subcount == givensubcount:
                    break
                subcount = subcount + 1
                name = fid
                fid = testresourceflag[sheet_name]['fid']
                moresubnets = True
                dictsub = dict()
                submaindict[name] = dictsub
                vardict[testresourceflag[sheet_name]['resid']] = submaindict

        if moresubnets:
            dictsub[fid] = row[index]

        else:
            fielddict[fid] = row[index]

    # print vardict
    print('------------------------------------------------------------------------------------------------------')
    return vardict
