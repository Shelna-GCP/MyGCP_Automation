import xlrd


# ----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    # print number of sheets
    #print book.nsheets

    # print sheet names
    #print book.sheet_names()
    print '-----------------------------------'
    dicmain ={}
    nodedic = {}
    b = book.sheet_by_name('GKE_Cluster_Node')
    for i in range(1,9):
         dicmain[b.cell_value(i,0)] = b.cell_value(i,1)

    countofnodes = dicmain['initial_node_count']

    for i in range():
         nodedic[b.cell_value(i,0)] = b.cell_value(i,1)


    print dicmain
    print nodedic
    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    #print first_sheet.row_values(0)

    # read a cell
    cell = first_sheet.cell(0, 0)
    #print cell
    #print cell.value

    # read a row slice
    # #print first_sheet.row_slice(rowx=0,
    #                             start_colx=0,
    #                             end_colx=2)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    path = r'C:\ShelnaGCP\dynamicterrform\vmdynamic\Reference_GCP_foundation.xlsx'
    open_file(path)