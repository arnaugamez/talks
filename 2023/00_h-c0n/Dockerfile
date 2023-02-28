FROM ubuntu:22.04

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y git python3-pip python3-venv
RUN apt-get install -y graphviz

ENV VIRTUAL_ENV=/opt/hc0n-env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install jupyterlab sympy numpy showast networkx matplotlib

RUN mkdir /opt/tools
RUN git config --global advice.detachedHead false

# Install msynth, miasm, and dependencies
WORKDIR /opt/tools
RUN git clone https://github.com/mrphrazer/msynth.git
WORKDIR /opt/tools/msynth
RUN git checkout 1418accdc106926bedc8f5a6ae406e9f6c029d74
RUN git submodule update --init --rebase
RUN pip3 install -r requirements.txt
RUN pip3 install .

# Install MBA-Solver
WORKDIR /opt/tools
RUN git clone https://github.com/softsec-unh/MBA-Solver.git
WORKDIR /opt/tools/MBA-Solver
RUN git checkout c76231aadb8b033d9e8e6be2baa05ff1464f247e
RUN sed -i 's/np.int/int/g' ./tools/mba_string_operation.py # Fix deprecated

# Install sagemath
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y sagemath sagemath-jupyter

RUN mkdir /opt/demo
# COPY demo /opt/demo
WORKDIR /opt/demo
EXPOSE 8888
ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0","--allow-root"]
