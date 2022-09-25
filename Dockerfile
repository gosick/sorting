FROM --platform=linux/amd64 python:3.10

ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    
RUN pip install --upgrade pip

RUN apt update -y && apt install libgl1-mesa-glx sudo -y

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3.10 -

ENV PATH=/root/.local/bin:$PATH

WORKDIR /var/www/html
