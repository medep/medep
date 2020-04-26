# MPG

## Get up and running
```
docker-compose up -d --build
```

Go to http://localhost:8080/ for MeDEP application

Data access portal of University Medical Centre Maribor is serving data on: http://localhost:8090/data


# Case studies

The folder ./frontend/public/case_studies includes examples of how various methods could be used for knowledge prioritization and potential learning across hospitals.

# Document embeddings

The folder ./frontend/public/case_studies/case2/document_embeddings includes CORD19 data set, embedded first into 256D with doc2vec (distributed memory), followed by UMAP projection to 2D.