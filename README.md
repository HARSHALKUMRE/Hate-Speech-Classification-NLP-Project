# Hate-Speech-Classification-NLP-Project

#### Language and Libraries

<p>
<a><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="python"/></a>
<a><img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"/></a>
<a><img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy"/></a>
<a><img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="matplotlib"/></a>
<a><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)" alt="docker"/></a>
<a><img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white" alt="gcp"/></a>
<a><img src="https://img.shields.io/badge/circle%20ci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white" alt="circleci"/></a>
<a><img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="tensorflow"/></a>
<a><img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white" alt="keras"/></a>
<a><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"/></a>


## Problem statement
In the Internet age where the information flow has grown rapidly, there is an increase in digital communication. The spread of hatred that was previously limited to verbal communications has quickly moved over the Internet. Social media and community forums that allows people to discuss and express their opinions are becoming platforms for the dissemination of hate messages.

The goal of this project is to develop a Hate Speech Classification system that can accurately identify the hate speech on the data.

## How to run?

### Step 1: Clone the repository
```bash
git clone "https://github.com/HARSHALKUMRE/Hate-Speech-Classification-NLP-Project" repository
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n hate python=3.9 -y
```

```bash
conda activate hate
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the  environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

```
Before running server application make sure your `s3` bucket is available and empty

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train
```

### Step 7. Prediction application
```bash
http://localhost:8080
```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build -t langapp .

```

3. Run the Docker image

```
docker run -d -p 8080:8080 <IMAGEID>
```

👨‍💻 Tech Stack Used
1. Python
2. FastApi
3. Tensorflow
4. Keras
5. Docker

🌐 Infrastructure Required.
1. Goggle Cloud Storage S3
2. GAR (Google Artifact repository)
3. GCE (Google Compute Engine)
4. CircleCI

## `src` is the main package folder which contains 

**Artifacts** : Stores all artifacts created from running the application

**Components** : Contains all components of Machine Learning Project
- DataIngestion
- DataTransformation
- ModelTrainer
- ModelEvaluation
- ModelPusher

**Custom Logger and Exceptions** are used in the project for better debugging purposes.
