import pandas as pd

from gcpautoutil.flagconstants import deployment_execution_order
from gcpautoutil.mapwithterraform import mapwithterraform
from gcpautoutil.readInputExcel import readGCPInput

if __name__ == '__main__':
    for i in range(1,7):
        sheetname = deployment_execution_order[i]

        df = pd.read_excel(r'C:\ShelnaGCP\dynamicterrform\vmdynamic\Reference_GCP_foundation.xlsx', index_col=0,
                           sheet_name=sheetname)
        columns = list(df.columns)

        for index in range(len(columns)):
            # reading fields from excel to dict
            vardict = readGCPInput(df, sheetname, index)

            # mapping fields to terraform fields
            print vardict
            if vardict is not None:
                mapwithterraform(vardict,sheetname)
