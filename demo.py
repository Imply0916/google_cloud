import os
from google.cloud import storage
os.environ['GOOGLE_APPLICATTION_CREDENTIALS']='google_cloud.json'
storage_client=storage.Client()