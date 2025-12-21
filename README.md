NumPy CSV Data Processing – AWS CI Pipeline

📌 Overview

This repository demonstrates a cloud-native Continuous Integration (CI) pipeline that builds, validates, and publishes a Docker image for a NumPy/Pandas-based CSV data processing application using AWS CodePipeline, AWS CodeBuild, and Amazon ECR.

Every commit to the repository automatically triggers the pipeline, ensuring the container image is built, tested, and stored as a reusable artifact.



🧱 Architecture
GitHub Repository
        │
        ▼
AWS CodePipeline
 (Source + Orchestration)
        │
        ▼
AWS CodeBuild
 (Docker build + runtime validation)
        │
        ▼
Amazon ECR
 (Versioned container image)



***🛠 Technologies Used***

Python 3.10

2. NumPy

3. Pandas

4. Docker

5. AWS CodeBuild

6. AWS CodePipeline

7. Amazon Elastic Container Registry (ECR)

8. GitHub



***⚙️ Application Logic***

The Python application:

Reads sales_data.csv

2. Selects numeric columns

3. Computes summary statistics using NumPy:

4. Row and column count

5. Mean, max, and min values

6. Prints the results to standard output

This execution is used as build-time validation inside the CI pipeline.


***🐳 Docker Workflow***

The Docker image packages:

Application code

2. Dataset

3. All required dependencies

4. The container is executed during the build to ensure correctness

5. Only validated images are pushed to Amazon ECR


***🚀 CI Pipeline Workflow***

Source Stage

2. CodePipeline pulls the latest commit from GitHub

3. Build Stage

4. CodeBuild authenticates to Amazon ECR using IAM

5. Builds the Docker image

6. Runs the container to validate data processing

7. Pushes the image to ECR on success

8. Artifact

9. A Docker image stored in Amazon ECR (numpy-data-processor:latest)


***✅ Success Criteria***

A successful pipeline run results in:

*Green Source and Build stages in CodePipeline

*2. Successful execution logs in CodeBuild

*A Docker image available in Amazon ECR

🔍 Verifying the Output

1. Check CodeBuild Logs

You should see output similar to:

Data Summary:
rows: ...
columns: ...
mean: ...
max: ...
min: ...


2. Check Amazon ECR

Repository: numpy-data-processor

Tag: latest

Image pushed during the pipeline run


3. Run the Image Locally (Optional)
docker run --rm <AWS_ACCOUNT_ID>.dkr.ecr.<region>.amazonaws.com/numpy-data-processor:latest

🔐 Security & Best Practices

No hard-coded credentials

IAM-based authentication for ECR

Build-time runtime validation

Clear separation between orchestration (CodePipeline) and execution (CodeBuild)

📈 Possible Extensions

Commit-hash–based image versioning

Security scanning (Amazon Inspector / Trivy)

Deployment to ECS or AWS Batch

Automated CD pipeline

📄 License

This project is for educational and demonstration purposes.
