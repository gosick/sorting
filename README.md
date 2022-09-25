# sorting

### Env build from Dockfile

- build image `docker build -t python3-10 .`
- docker run `docker run -itd --name python310 -v YourProjectPath:/var/www/html/ --platform linux/amd64 python3-10`
- to container `docker exec -it python310 bash`
- install packages and create virtualenv at the first time using `poetry install`

### Run

In container
- `poetry run python -m unittest` or `poetry run python -m unittest test/test_heapsort.py`