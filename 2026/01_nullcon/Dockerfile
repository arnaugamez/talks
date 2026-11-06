FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update
RUN apt-get install -y git python3-pip python3-venv graphviz
RUN git config --global advice.detachedHead false

ENV VIRTUAL_ENV=/opt/nc-env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install jupyterlab sympy numpy showast networkx matplotlib setuptools

# Install msynth, miasm, and dependencies
RUN mkdir /opt/tools
WORKDIR /opt/tools
RUN git clone https://github.com/mrphrazer/msynth.git
RUN cd msynth && \
    git checkout d719a58e44703adcb347aae0b3c61a327e041fd7 && \
    python3 -m pip install -r requirements.txt && \
    python3 -m pip install .

RUN mkdir /opt/workshop
WORKDIR /opt/workshop
EXPOSE 8888
ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0","--allow-root"]
