# ESG Company Search

# Summary

## Scenario/Use Case
Financial analysts want to understand how a company is performing ESG(Environmental, Social, and Governance)-wise to help determine its potentials risks and opportunities.

## Goal
Provide an evaluation of certain ESG metrics based on a company's annualy published ESG report using AI/Machine Learning LLM.

## Parameters
- **Input:** Pdf file containing company ESG report.
- **Output:** Text (evaluation).

# App Setup

## Docker Setup *(recommended)*
Make sure you have [Docker](https://www.docker.com/) installed.
Run the following command in a terminal to build and run a new container:
```
bash scripts/run_app_in_docker.sh
```
This script creates a new image and container every time it's run, 
so you might want to `docker prune` after having run it a couple of times.

*Note: I recommend this setup to ensure that none of your current local dependencies
gets changed/updated inadvertently. A docker container ensures isolation and makes it easy to 
deploy apps regardless of the current machine's setup.*


## Run Tests
To run the testsuite, first run the app in the container as explained above,
then run the following in the terminal inside the container:
```
pytest
```