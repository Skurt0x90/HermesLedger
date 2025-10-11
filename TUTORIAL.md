Quick Test Tutorial
===================

Local Python test:
------------------
1. Ensure you have Python 3.11+ installed.
2. From the project root run: python src/run_demo.py
3. You should see 3 simulated nodes adding logs and the chain printed.

Docker Compose test:
--------------------
1. Ensure Docker and docker-compose are installed.
2. cd docker
3. docker-compose up --build
4. The three containers will run and print the demo to docker logs.

Notes:
- This POC uses shared in-memory chain for simplicity. In a real setup each node
  would run independently and sync over HTTP/p2p. The docker setup here simply
  demonstrates how to run the same code in three containers.
