"""
ML Model Deployment at Streamlit Server 
"""

### Import Libraries
import os
import boto3
import torch
import streamlit as st
from transformers import pipeline

### Settin the device
device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")

### Initializing s3 client
s3_client = boto3.client("s3")

### Function for downloading directory from AWS S3 bucket
local_path = "./sentiment-classifier-tinyBERT"
s3_prefix  = "ml-models/sentiment-classifier-tinyBERT/"

bucket_name = "bert-based-project" 

def download_s3_dir(local_path, s3_prefix):
    os.makedirs(local_path, exist_ok=True)

    paginator = s3_client.get_paginator("list_objects_v2")

    for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        print(page)
        if "Contents" in page:
            for object in page["Contents"]:
                s3_key = object["Key"]

                local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))
                os.makedirs(os.path.dirname(local_file), exist_ok=True)

                s3_client.download_file(bucket_name, s3_key, local_file)


st.title("Machine Learning Model Deployment at Server")

button = st.button("Download Model")
if button:
    with st.spinner("Please wait while we download the model!"):
        download_s3_dir(local_path, s3_prefix)


text = st.text_area("Enter your review", placeholder="Type here...")

sentiment_classifier = pipeline("text-classification", model="sentiment-classifier-tinyBERT", device=device)

predict_button = st.button("Predict Sentiment")
if predict_button:
    with st.spinner("Predicting the sentiment..."):
        output = sentiment_classifier(text)
        label = output[0]["label"]
        score = output[0]["score"]
        st.write(label, score)