FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update
RUN apt-get install -y git python3-pip python3-venv graphviz
RUN git config --global advice.detachedHead false

ENV VIRTUAL_ENV=/opt/eh-env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install jupyterlab sympy numpy showast networkx matplotlib

# Install msynth, miasm, and dependencies
RUN mkdir /opt/tools
WORKDIR /opt/tools
RUN git clone https://github.com/mrphrazer/msynth.git
WORKDIR /opt/tools/msynth
RUN git checkout 1418accdc106926bedc8f5a6ae406e9f6c029d74
RUN git submodule update --init --rebase
RUN pip3 install -r requirements.txt
RUN pip3 install .

RUN mkdir /opt/workshop
WORKDIR /opt/workshop
EXPOSE 8888
ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0","--allow-root"]
