
# Generative AI SDR Agent - Powered By GCP Vertex AI 

Search personas, scrape social media presence, draft custom emails on specified topic

![Alt Text](https://github.com/g-emarco/llm-agnets/blob/main/static/demo.gif)


## Tech Stack


**Client:** Streamlit

**Server Side:** LangChain  🦜🔗

**LLM:** PaLM 2

**Runtime:** Cloud Run  

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`STREAMLIT_SERVER_PORT`


## Run Locally


Clone the project

```bash
  git clone https://github.com/emarco177/llm-agnets.git
```

Go to the project directory

```bash
  cd llm-agnets
```

Install dependencies

```bash
  pipenv install
```

Start the Streamlit server

```bash
  streamlit run app.py
```

NOTE: When running locally make sure `GOOGLE_APPLICATION_CREDENTIALS` is set to a service account with permissions to use VertexAI


## Deployment to cloud run

CI/CD via Cloud build is available in ```cloudbuild.yaml```

Please replace $PROJECT_ID with your actual Google Cloud project ID.

To deploy manually:

0. Export PROJECT_ID environment variable:
```bash
export PROJECT_ID=$(gcloud config get-value project)
```

1. Make sure you enable GCP APIs:

```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable secretmanager.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable aiplatform.googleapis.com


```

2. Create a service account `vertex-ai-consumer` with the following roles:




```bash
gcloud iam service-accounts create vertex-ai-consumer \
    --display-name="Vertex AI Consumer"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.invoker"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/serviceusage.serviceUsageConsumer"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/ml.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.admin"

```


3. Build Image
```bash
docker build . -t us-east1-docker.pkg.dev/$PROJECT_ID/app/palm2-app:latest
```

4. Push to Artifact Registry
```bash
docker push us-east1-docker.pkg.dev/$PROJECT_ID/app/palm2-app:latest
```

6. Deploy to cloud run
```gcloud run deploy $PROJECT_ID \
    --image=us-east1-docker.pkg.dev/PROJECT_ID/app/palm2-app:latest \
    --region=us-east1 \
    --service-account=vertex-ai-consumer@$PROJECT_ID.iam.gserviceaccount.com \
    --allow-unauthenticated \
    --set-env-vars="STREAMLIT_SERVER_PORT=8080 \
```



## 🚀 About Me
Eden Marco, Customer Engineer @ Google Cloud, Tel Aviv🇮🇱

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/) 

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/EdenEmarco177)

