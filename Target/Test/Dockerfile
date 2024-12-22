FROM ubuntu:20.04

# Non-interactive for apt commands
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for Python and venv
RUN apt-get update && apt-get install -y \
    python3 python3-venv python3-pip mosquitto-clients\
    && rm -rf /var/lib/apt/lists/*

# Create workspace directory
RUN mkdir -p /workspace
WORKDIR /workspace

# Create a virtual environment and install the package
RUN python3 -m venv /workspace/build/venv && \
    /workspace/build/venv/bin/pip install --upgrade pip && \
    /workspace/build/venv/bin/pip install paho-mqtt==1.6.1


# Activate virtual environment by default
CMD ["/bin/bash"]
