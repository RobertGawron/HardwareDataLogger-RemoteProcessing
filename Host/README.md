# Purpose

Set up a working environment on a local machine.

# Needed software

Only Docker Compose is needed; all tools are installed in the Docker container.

Note: for Windows users, WSL needs to be installed to run the Docker engine.

# Build and run the image

In the directory where this file is located, build the Docker image (only once at the start):

```
docker-compose build hwlogger-arm-builder
```

Start the Docker image:

```
docker-compose up -d hwlogger-arm-builder 
```

Log into the Docker image:

```
docker-compose exec hwlogger-arm-builder bash
```

That's it - now we are on a Linux machine that has all the software we need to start building and deploying.

When finished, shut down the Docker container:

```
docker-compose down --remove-orphans
```

Here is a one-liner to build, start, and connect:

```
docker-compose build hwlogger-arm-builder && docker-compose up -d hwlogger-arm-builder && docker-compose exec hwlogger-arm-builder bash
```

#### Troubleshooting

To view logs for the Docker container:

```
docker logs hwlogger-arm-builder
```

# Generate SSH Keys

To deploy the Docker images to a remote host, we need to configure an SSH key so that we can connect to that host without being prompted for a password. This should be done inside the container that we built.

Inside the Docker container, generate your keys:

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

The .ssh folder in the container is mapped to a Docker Compose volume, so the SSH keys will be persistent (no need to regenerate them after rebuilding the builder image).

Use ssh-copy-id to copy the key to the remote machine. Change the username and IP address according to your configuration (your username and your address of your Raspberry Pi).

```
ssh-copy-id -i ~/.ssh/id_rsa.pub robert@192.168.1.44
```

Test if SSH key-based login works:

```
ssh robert@192.168.1.44
```

You should be able to log in without entering a password.
