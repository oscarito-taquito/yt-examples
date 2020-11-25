# modules
import pandas as pd
from google.cloud import bigquery

# variables
gcp_project = 'osk-demo-277900'
bq_dataset = 'osk'

# connections
client = bigquery.Client(project=gcp_project)
dataset_ref = client.dataset(bq_dataset)

# results to dataframe function
def gcp2df(sql):
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe() 

query = """select unique_key
, complaint_type
, owning_department
, source
, status
, created_date
, street_number
, street_name
, incident_zip
from `bigquery-public-data.austin_311.311_request`
limit 100"""

df = gcp2df(query)

print(df.head())