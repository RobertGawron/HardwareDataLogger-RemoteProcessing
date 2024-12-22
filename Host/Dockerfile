FROM docker:dind

# Install QEMU for ARM cross-platform builds
RUN apk add --no-cache \
    qemu qemu-system-x86_64 qemu-system-arm \
    bash curl git python3 py3-pip \
    rsync \
    dos2unix

WORKDIR /workspace

CMD ["/bin/bash"]
