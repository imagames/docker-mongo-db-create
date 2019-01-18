# docker-mongo-db-create

Docker image that connects to a specified mongo instance, creates a database, and an user with owner role for that database.

## How to

This image requires the following environment variables, all of which are mandatory:

| Variable           | Example         | Description                                           |
|--------------------|-----------------|-------------------------------------------------------|
| `MONGO_URL`        | `foo.bar:27027` | URL of the mongoDB instance, including port          |
| `MONGO_ADMIN_USER` | `admin`         | Admin username (with user and db creation privileges) |
| `MONGO_ADMIN_PASS` | `foo`           | Admin password                                        |
| `MONGO_DB_NAME`    | `admin`         | Name of the database to create                        |
| `MONGO_USER`       | `user`          | Name of the new user to create                        |
| `MONGO_PASS`       | `pass`          | Password for the new user                             |