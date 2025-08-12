# Candidate Matching RAG Agent with ADK

This repository contains a Google Agent Development Kit (ADK) implementation of a specialized Candidate Matching agent using Google Cloud Vertex AI's Retrieval Augmented Generation (RAG) capabilities.

## Overview

The Candidate Matching RAG Agent helps recruiters and hiring managers find the best candidates for job openings by:

- Matching job descriptions with candidate profiles from document corpora
- Analyzing resumes, CVs, and candidate profiles to find the best matches
- Ranking candidates based on skills, experience, and qualifications
- Identifying skills gaps and highlighting candidate strengths
- Managing candidate document collections efficiently

## Prerequisites

- A Google Cloud account with billing enabled
- A Google Cloud project with the Vertex AI API enabled
- Appropriate access to create and manage Vertex AI resources
- Python 3.9+ environment

## Setting Up Google Cloud Authentication

Before running the agent, you need to set up authentication with Google Cloud:

1. **Install Google Cloud CLI**:
   - Visit [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) for installation instructions for your OS

2. **Initialize the Google Cloud CLI**:
   ```bash
   gcloud init
   ```
   This will guide you through logging in and selecting your project.

3. **Set up Application Default Credentials**:
   ```bash
   gcloud auth application-default login
   ```
   This will open a browser window for authentication and store credentials in:
   `~/.config/gcloud/application_default_credentials.json`

4. **Verify Authentication**:
   ```bash
   gcloud auth list
   gcloud config list
   ```

5. **Enable Required APIs** (if not already enabled):
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```

## Installation

1. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Using the Candidate Matching Agent

The agent provides the following recruitment-focused functionality:

### 1. Match Candidates to Jobs
Find the best candidates for specific job requirements:
- Submit job descriptions to search candidate corpora
- Get ranked lists of matching candidates
- See detailed match quality assessments
- Identify skills gaps and candidate strengths

### 2. List Candidate Corpora
View all available candidate collections:
- See corpus names and basic information
- Understand what candidate pools are available

### 3. Create Candidate Corpus
Set up new candidate collections for specific roles or departments:
- Create specialized candidate pools (e.g., "engineering_candidates")
- Organize candidates by department, role type, or other criteria
- Prepare for candidate document ingestion

### 4. Add Candidate Profiles
Import candidate documents to existing corpora:
- Add resumes, CVs, and candidate profiles
- Support for Google Drive URLs and GCS paths
- Automatically create new candidate corpora if needed

### 5. Get Corpus Information
View detailed information about candidate collections:
- See candidate count, document metadata, and creation time
- Understand corpus contents and candidate pool composition

### 6. Delete Candidate Document
Remove outdated or irrelevant candidate profiles:
- Delete specific candidate documents when no longer needed
- Maintain up-to-date candidate pools

### 7. Delete Candidate Corpus
Remove entire candidate collections when no longer needed:
- Requires confirmation to prevent accidental deletion
- Permanently removes the corpus and all associated files

## Effective Candidate Matching

The agent uses several strategies to match candidates to job descriptions:

1. **Skill-Based Matching**: Identifies technical skills, tools, and technologies mentioned in both job descriptions and candidate profiles.

2. **Experience-Level Alignment**: Matches years of experience and seniority requirements with candidate backgrounds.

3. **Domain Knowledge**: Recognizes industry-specific experience and domain expertise.

4. **Project Relevance**: Finds candidates who have worked on similar projects or solved similar problems.

5. **Education and Certification Matching**: Matches required degrees, certifications, and specialized training.

## Troubleshooting

If you encounter issues:

- **Authentication Problems**:
  - Run `gcloud auth application-default login` again
  - Check if your service account has the necessary permissions

- **API Errors**:
  - Ensure the Vertex AI API is enabled: `gcloud services enable aiplatform.googleapis.com`
  - Verify your project has billing enabled

- **Quota Issues**:
  - Check your Google Cloud Console for any quota limitations
  - Request quota increases if needed

- **Missing Dependencies**:
  - Ensure all requirements are installed: `pip install -r requirements.txt`

## Additional Resources

- [Vertex AI RAG Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview)
- [Google Agent Development Kit (ADK) Documentation](https://github.com/google/agents-framework)
- [Google Cloud Authentication Guide](https://cloud.google.com/docs/authentication)
