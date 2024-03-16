import tabula as tab
import pandas as pd
pages_patient = "1-160"
pages_diabetes = "161-320"
pages_risks = "321-480"
pages_age = "481-640"
dfs = tab.read_pdf('ObesityAnalysis.pdf', pages = pages_patient, stream = True, guess = False, columns = (100, 149, 280, 350, 422, 480), pandas_options = {'header' : None})
tb_patient = pd.DataFrame([]);
for df in dfs:
    tb_patient = pd.concat([tb_patient, df], ignore_index = True)
tb_patient = tb_patient.iloc[1:]
tb_patient.columns = ["PatientId", "Zone", "State", "District", "Age", "Gender", "Waist"]
tb_patient