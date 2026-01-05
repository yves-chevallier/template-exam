FROM nowox/latex:2.0
RUN pip3 install pyyaml
RUN pip3 install tikzplotlib
RUN pip3 install gitpython
RUN apt-get update && apt-get install -y qpdf libc6
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN apt-get update && apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8