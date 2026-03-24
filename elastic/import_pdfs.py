import os
import base64
from elasticsearch import Elasticsearch

# Verbindung zu Elasticsearch
es = Elasticsearch("http://localhost:9200")

# >>> DEIN PDF ORDNER <<< (RAW STRING verwenden!)
folder = r"C:\Users\egoumlepoue\OneDrive - United Internet Group\Desktop\elastic\Dokumente"

for file in os.listdir(folder):
    if file.lower().endswith(".pdf"):
        path = os.path.join(folder, file)
        print(f"Importing: {file}")

        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()

        es.index(
            index="pdf_index",
            pipeline="pdf_ingest",
            document={
                "file_name": file,
                "data": data
            }
        )

print("Alle PDFs wurden erfolgreich importiert!")