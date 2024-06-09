# Create custom containerized env by combining several open source projects into a production app

**Goal: launch several popular open source libs/projects onto production services.**
**Projects:**
- FastAPI app (already includes multiple app orchestrations): https://github.com/tiangolo/full-stack-fastapi-template
- - add dependency and example-file implementation: https://github.com/aurelio-labs/semantic-router
- - add haystack and a demo Hayhook: https://docs.haystack.deepset.ai/v2.0/docs/hayhooks
- gateway ('Local Deployment', so no need for a Portkey API Key): https://github.com/Portkey-AI/gateway/blob/main/docs/installation-deployments.md#deploy-using-docker-compose
- Infinity: https://github.com/michaelfeil/infinity (run as python service)
- dify: https://github.com/langgenius/dify?tab=readme-ov-file#quick-start


### Each of these projects includes a guide for how to self host. I just need someone to pull them together into one configuration/orchestration.
