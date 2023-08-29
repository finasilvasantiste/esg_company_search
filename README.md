# ESG Company Search

# Index
- [TLDR](#tldr)
- [Writeup](#writeup)
- [How it works](#how-it-works)
- [App Setup](#app-setup)

# TL;DR
Proof-of-concept: this app uses a LLM (openai api) to answer given questions to a given text. The input are pdf files with company annual sustainability reports and the output are answers to a handful of ESG metrics. Currently, the questions to ask and the text to use as context are hardcoded. 
At this stage, I'd connect with stakeholders to understand if this meets their needs,
which improvements to make and functionality to add. 

# Writeup

## Scenario/Use Case
Financial analysts want to understand how a company is performing ESG(Environmental, Social, and Governance)-wise to help determine its potentials risks and opportunities.

## Goal
Provide an evaluation of certain ESG metrics based on a company's annualy published ESG report using AI/Machine Learning LLM.

# How it works

## Parameters
- **Input:** Pdf file containing company ESG report uploaded in folder.
- **Output:** Text (question topic and LLM's answer) printed out in console.

## Examples
- **Input:** [Airbnb's 2021 ESG report](https://s26.q4cdn.com/656283129/files/doc_downloads/governance_doc_updated/Airbnb-ESG-Factsheet-(Final).pdf).
- **Output:**
  
| Question Topic        | LLM's Answer |
| ------------- |:-------------:| 
| Diversity and Inclusion     | Airbnb is "deeply committed to making Airbnb a place where people of all backgrounds, identities, and experiences can succeed and thrive." They have "established a Diversity Council comprising senior leaders" to further embed their plans into their organizations, as well as offer "training on allyship, unconscious bias, and disability inclusion" for all employees. They also have implemented policies such as "requiring women and underrepresented minorities in the US to be presented on candidate slates when we hire for open roles," as well as "increasing our investment in professional development, mentorship, and sponsorship for women and underrepresented minorities." Airbnb is also supporting "19 employee resource groups (ERGs)" to foster a sense of belonging at work.      |
| Executive Compensation     | In the factsheet, Airbnb mentioned their commitment to "supporting our employees" which includes a principle of "pay equity". They describe taking "deliberate actions to make our recruiting, promotion, and retention practices more inclusive" and investing in "mentorship, and sponsorship for women and underrepresented minorities", and they offer "leadership development courses for members of our employee resource groups". Although the factsheet does not provide details on executive compensation specifically, it is clear that Airbnb is dedicated to promoting diversity and gender and racial equality in their salary policies.  |


## Note on technology used
The business logic is wrapped in a lightweight **data workflow orchestration tool** [(Prefect)](https://www.prefect.io/opensource) to more easily provide observabililty, scheduling, deployment on the cloud, etc. To deploy the app on the cloud you need a server running an instance of the Prefect dashboard (or alternatively use an instance hosted by Prefect themselves, which they call Prefect Cloud) and some AWS infra (or any other cloud provider supported by Prefect). The Prefect api can use the `docker-compose.yml` file inside this repo to create an image that gets pushed into an AWS ECS repo, and using an ECS task definition that image can then be run in an ECS container. Once the workflow ran the ECS container gets shut down and the AWS resources released.


# App Setup

## Requirements
- Latest [Docker](https://www.docker.com/) version (this app uses `Docker version 24.0.5`).
- An [OpenAI](https://platform.openai.com/) account with some balance on it to be able to use their LLM.

***That's it.*** The rest of the setup is being taken care of by the Docker container/image.


## Docker Setup *(recommended)*
Run the following command in a terminal to build and run a new container:
```
bash scripts/run_app_in_docker.sh
```
This script creates a new image and container every time it's run, 
so you might want to `docker prune` after having run it a couple of times.

*Note: I recommend this setup to ensure that none of your current local dependencies
gets changed/updated inadvertently. A docker container ensures isolation and makes it easy to 
deploy apps regardless of the current machine's setup. (That also makes it easier to deploy on the cloud.)*

## Run App
To run the application, first run the app in the container as explained above, 
then run the following in the terminal inside the container:
```
python main.py
```

## Run Tests
To run the testsuite, first run the app in the container as explained above,
then run the following in the terminal inside the container:
```
pytest
```
