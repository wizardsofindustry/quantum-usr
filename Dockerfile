FROM alpine:latest AS builder

RUN apk update && apk upgrade && \
    apk add --no-cache bash git
COPY .git .
RUN git rev-parse HEAD > .commit
RUN git tag -l --points-at HEAD | tail -1 > .version
RUN git log -1 --format='%ae' HEAD > .author-email
RUN git log -1 --format='%an' HEAD > .author-name

# Construction of the final Docker image starts here.
FROM wizardsofindustry/quantum:latest
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /srv/usr
RUN mkdir /var/lib/usr
RUN mkdir /var/spool/aorta

COPY bin/ /app/bin/
COPY ./bin/docker-entrypoint /app/bin/docker-entrypoint
ENV QUANTUM_DEPLOYMENT_ENV dev
ENV QUANTUM_DEPLOYMENT_NAME dev
ENV AORTA_SPOOL_DIR /var/spool/aorta

COPY .coveragerc /app
COPY .pylintrc /app

COPY setup.py .
COPY etc/ etc/
COPY etc/ /etc/usr
COPY usr /app/usr

COPY alembic.ini alembic.ini
COPY migrations/ migrations/
COPY --from=builder .author-email .
COPY --from=builder .author-name .
COPY --from=builder .version .
COPY --from=builder .commit .

RUN python3 setup.py install


ENTRYPOINT ["./bin/docker-entrypoint"]
