FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/usr
RUN mkdir /var/spool/aorta

COPY . /app
COPY etc/ /etc/usr/

WORKDIR /app
RUN SQ_TESTING_PHASE=lint ./bin/run-tests
RUN python3 setup.py install

ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV USR_SECRET_KEY 30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460
ENV USR_RDBMS_DSN postgresql+psycopg2://usr:usr@rdbms:5432/usr
ENV USR_RUNTIME service

ENTRYPOINT ["./bin/docker-entrypoint"]
