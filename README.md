# Comparaonline-coding-test

This test's requirements specs are available in the following repository:
[https://github.com/comparaonline/interview-coding-test](https://github.com/comparaonline/interview-coding-test)

## This test's goal is to refactor the old code.

For my convenience I decided to write this project in Python.

### *Requirements*:
1. Install [Docker client](https://www.docker.com/)
2. Installl [Docker Compose](https://docs.docker.com/compose/)
3. `cd path/to/project`
4. `docker-compose build`
5. `docker-compose up`

### *How to run the project*:

1. Enter to the container with `docker exec -it comparaonline-coding-test_web_1 /bin/bash`
2. Once inside the container, run `python after_30_days.py`
3. It should create a `products_after_30_days.txt` file with all the requested data.

## *How to test the project*: 

1. Inside the container, run `python -m pytest --cov`
2. It should run `test_after_30_days` and show a coverage report on screen.
3. As the function to test is using all the classes in the project, it should get 100% coverage.

## *What if I want to add a new type of product?*

- Just add a new class to `products/` that inherits from `Product`. 
- Override the desired method according to the product type specs.