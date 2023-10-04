# Feshesblog-FlaskAPI

Feshesblog-FlaskAPI is an easy to use web API for creating blogs. It is an ideal project to use when learning a front end framework, as it provides a fully implemented back end that you can integrate against.

Feshesblog-FlaskAPI provides all the base features required to implement a blog web app:

User registration, login and logout
Password recovery flow with reset emails
Post creation and deletion
Follow and unfollow users
Feed with posts from followed users
Pagination
Option to disable authentication during development

## Deploy to Heroku

Click the button below to deploy the application directly to your Heroku
account.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/festusmwambu/feshesblog-api/tree/heroku)

## Deploy on your Computer

### Setup

Follow these steps if you want to run this application on your computer, either
in a Docker container or as a standalone Python application.

```bash
git clone https://github.com/festusmwambu/feshesblog-api
cd feshesblog-api
cp .env.example .env
```

Open the new `.env` file and enter values for the configuration variables.

### Run with Docker

To start:

```bash
docker-compose up -d
```

The application runs on port 5000 on your Docker host. You can access the API
documentation on the `/docs` URL (i.e. `http://localhost:5000/docs` if you are
running Docker locally).

To populate the database with some randomly generated data:

```bash
docker-compose run --rm feshesblog-api bash -c "flask fake users 10 && flask fake posts 100"
```

To stop the application:

```bash
docker-compose down
```

### Run locally

Set up a Python 3 virtualenv and install the dependencies on it:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create the database and populate it with some randomly generated data:

```bash
flask db upgrade
flask fake users 10
flask fake posts 100
```

Run the application with the Flask development web server:

```bash
flask run
```

The application runs on `localhost:5000`. You can access the API documentation
at `http://localhost:5000/docs`.

## Troubleshooting

On macOS Monterey and newer, Apple decided to use port 5000 for its AirPlay
service, which means that the Feshesblog API server will not be able to run on
this port. There are two possible ways to solve this problem:

1. Disable the AirPlay Receiver service. To do this, open the System
Preferences, go to "Sharing" and uncheck "AirPlay Receiver".
2. Move Feshesblog API to another port:
    - If you are running Feshesblog API with Docker, add a
    `FESHESBLOG_API_PORT=4000` line to your *.env* file. Change the 4000 to your
    desired port number.
    - If you are running Feshesblog API with Python, start the server with the
    command `flask run --port=4000`.
