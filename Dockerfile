# source: https://bitbucketp.duke-energy.com/projects/go/repos/guide/browse/example-configs/Dockerfile.simple
# syntax = docker/dockerfile:1.4

FROM nexus-docker-cne.ci.duke-energy.app/duke/cicd/base-image:1-ubuntu as cicd-base
WORKDIR /build

# override this from Concourse with the "BUILD_ARG_PYTHON_VERSION" parameter.
# versions here: https://nexus.ci.duke-energy.app/#browse/browse:duke-cne-raw-python
ARG PYTHON_VERSION=3.11
RUN duke-install python.ubuntu=${PYTHON_VERSION}

# This line takes too long currently
# RUN DEBUG=true duke-install python-src-std=${PYTHON_VERSION}
RUN apt-get install -y -qq python3.11 python3.11-venv
RUN python3.11 -m venv .
RUN curl -sSL https://install.python-poetry.org | python3.11 - --version 1.2.0
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
ENV PATH="/root/.local/bin:$PATH"
COPY src/shared/ /build/
RUN poetry build
RUN python3.11 -m pip install dist/shared-0.1.0-py3-none-any.whl

# fetch dependencies in a separate layer so they can be cached.
COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt 

# install duke certs into the runtime image, and configure apk, if you need to install packages.
# COPY --from=cicd-base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
# RUN sed -ri 's!https://dl-cdn.alpinelinux.org!https://nexus.ci.duke-energy.app/repository/duke-common-python-repositories!g' /etc/apk/repositories

ENTRYPOINT []
