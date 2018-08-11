FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/usr
RUN mkdir /var/spool/aorta

COPY . /app
COPY etc/ /etc/usr/

WORKDIR /app
RUN python3 setup.py install

ENV QUANTUM_DEPLOYMENT_ENV development
ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV USR_SECRET_KEY 30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460
ENV USR_DEBUG 1
ENV USR_IOC_DEFAULTS /etc/usr/ioc.conf
ENV USR_IOC_DIR /etc/usr/ioc.conf.d/
ENV USR_RDBMS_DSN postgresql+psycopg2://usr:usr@rdbms:5432/usr
ENV USR_HTTP_ADDR 0.0.0.0
ENV USR_HTTP_PORT 8443
ENV USR_RUNTIME service

ENV SQ_TESTING_PHASE lint
RUN ./bin/run-tests

ENTRYPOINT ["./bin/docker-entrypoint"]
