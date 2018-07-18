FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/usr
RUN mkdir /var/spool/aorta

COPY . /app
COPY etc/ /etc/usr/

WORKDIR /app
RUN python3 setup.py install

ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV USR_SECRET_KEY 30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460
ENV USR_RDBMS_DSN postgresql+psycopg2://usr:usr@rdbms:5432/usr

# There is a bug in pycparser/plyparser.py", line 112, in _create_param_rules
# which prevents running with the -OO flag.
ENTRYPOINT ["python3","-O","-m","usr.runtime", "-c", "/etc/usr/usr.conf"]
