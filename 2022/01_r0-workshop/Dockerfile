FROM ubuntu:22.04

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y git python3-pip python3-venv

ENV VIRTUAL_ENV=/opt/r0workshop
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install jupyterlab astunparse

COPY src /opt/src

WORKDIR /opt
RUN git config --global advice.detachedHead false
RUN git clone https://github.com/mrphrazer/msynth.git

WORKDIR /opt/msynth
RUN git checkout 1418accdc106926bedc8f5a6ae406e9f6c029d74
RUN git submodule update --init --rebase
RUN pip3 install -r requirements.txt
RUN pip3 install .

WORKDIR /opt/src
EXPOSE 8888
ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0","--allow-root"]
