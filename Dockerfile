ARG PYTHON_VERSION=3.10.11

# -----------------------------
# Frontend
# -------------------------------
FROM node:16 as frontend

WORKDIR /static

COPY ./static/package.json .

RUN npm install

# -------------------------------
# Backend
# -------------------------------
FROM python:${PYTHON_VERSION} as backend

LABEL maintainer = '2023 MyHomeworks, { }'

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/static

RUN rm -rf node_modules && mkdir node_modules

COPY --from=frontend /static/node_modules /app/static/node_modules

WORKDIR /app
