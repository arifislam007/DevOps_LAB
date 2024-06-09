# Microservice Deployment with Message Broker 

Create an application with 2 microservices that communicate via message bus.
	•	Service "users" has an endpoint POST /users and on request with body {"email","firstName","lastName"}, stores the submitted data in a database or in a log file.
	•	When the submitted data is saved, an event is generated and it is sent through a message broker to the "notifications" service. In "notifications" service the event is consumed and the sent data is saved in a log file.
	•	The code must be covered with tests - unit, integration and functional tests.
	•	Prepare needed containers in docker.
	•	both services should run with one nginx server
