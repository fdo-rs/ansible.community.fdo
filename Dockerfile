FROM ubuntu:22.04
# building quay.io/justinc1_github/temp-py3.10-ub2204:latest
RUN apt update && apt -y install python3 openssh-client
RUN ln -s /usr/bin/python3 /usr/bin/python
