# Authentification is required by exporting the credentials contained in the json file
# The line below needs to be executed in the Terminal before runing the python file: 
# export GOOGLE_APPLICATION_CREDENTIALS= "/Users/nhathiep/Python_Projects/SQL connectors/proud-outrider-337507-319bec3fd79c.json"

# In terminal, change directory (cd) to '/Users/nhathiep/Python_Projects/SQL connectors/'
# Then execute this py file: python3 bigquery_test.py

from google.cloud import bigquery
client = bigquery.Client()

#Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 10')
query_job = client.query(QUERY)  # API request
#rows = query_job.result()  # Waits for query to finish

#for row in rows:
#    print(row.name)

dataframe = (
    query_job
    .result()
    .to_dataframe(
        # Optionally, explicitly request to use the BigQuery Storage API. As of
        # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
        # API is used by default.
        create_bqstorage_client=True,
    )
)
print(dataframe.head())