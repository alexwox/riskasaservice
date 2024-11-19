# riskasaservice





When making changes to the code, run the following commands:

To build and run the container:
bash docker buildx build --platform linux/amd64 -t <id>.dkr.ecr.eu-north-1.amazonaws.com/riskasaservice:§latest --push .

Add subnet ports to allow traffic to the container from the VPC on AWS.

Make sure the correct container is in ECR

Connect container to the Task Definition.

Run task definition with cluster.


To do (no order)

Parsing:
- [ ] Build the ability to, using OmniParse, extract portfolio from screenshot, maybe separate service using AWS lambda?

Data Retrieval:
- [ ] Investigate API data sources
   - [ ] StockPriceData?
   - [ ] Annual reports?

Risk analysis:
- [ ] Build out the financial metrics, to use VaR with Copulas

Report generation:
- [ ] Build out agentic report generation using CRAG? (RAG) with llamaindex, using quantitative analysis + qualitative analysis from annual reports.

API infra:
- [ ] Build an API gateway on AWS to handle the traffic and manage the endpoints.
- [ ] Set up a CI/CD pipeline with github actions to deploy the new container to Fargate
- [ ] Set up monitoring and logging with CloudWatch and CloudWatch Logs
- [ ] Set up API keys for usage tracking and rate limits
- [ ] Add endpoints for creating API keys and managing them

The goal is to build the API in a way so that it can be hit by a ConvexAction after Stripe confirmation to:
1. Generate a user Specific API key that is then returned and stored in Convex
2. Allow ConvextAction to hit the service to generate a risk analysis and report.
    - UserEmail, UserId, Portfolio (or PortfolioImage, maybe separate service)?
3. Send the Report to email

Still need to figure out:
- How to store annual reports and other information
- How to run the agents, where should the vector stores be?
- Should everything related to Analysis etc be handled by the API?
