# Universal Subject Resolver (USR)

The Universal Subject Resolver (USR) maintains associations between **Subjects**
and one or many **Principals**. A **Principal**, such as an email address or username,
uniquely resolves to a **Subject** through a unique **Global Subject Identifier (GSID)**,
simplifying the identification, authentication and maintenance of users in
a single system.

## Table of Contents

- [Features](#features)
- [Security considerations](#security-considerations)
- [Installation](#installation)
- [Developing](#developing)

## Features
- Resolve **Principals** to **Subjects** (represented by a *Global Subject Identifier*
  (GSID)) through an easy-to-use HTTP interface.
- Supports Username, RFC822 (email address), X.509 certificate.

## Security considerations
- This service is deployed in the `citadel` environment. Clients are assumed
  to be *internal* and authorized at the network level.


## Installation & Environment

### Environment variables

The **Universal Subject Resolver** runtime is configured through environment
variables. The table below provides an overview of the possible values:

| Type  |       Name       |                             Default                              |
|-------|------------------|------------------------------------------------------------------|
|literal|`USR_RUNTIME`     |`service`                                                         |
|switch |`USR_DEBUG`       |`1`                                                               |
|literal|`USR_HTTP_ADDR`   |`0.0.0.0`                                                         |
|literal|`USR_HTTP_PORT`   |`8443`                                                            |
|literal|`USR_IOC_DEFAULTS`|`/etc/usr/ioc.conf`                                               |
|literal|`USR_IOC_DIR`     |`/etc/usr/ioc.conf.d/`                                            |
|literal|`USR_RDBMS_DSN`   |`postgresql+psycopg2://usr:usr@rdbms:5432/usr`                    |
|literal|`USR_SECRET_KEY`  |`30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460`|



For more information on these variables, refer to the `environ` section of
the projects' `Quantumfile`.

The configured environment is loaded in the `usr.environ` module.
Environment variables of type `switch` are normalized into `bool` objects; all other
variables are assumed `literal` and parsed as-is.

### Docker
The **Universal Subject Resolver** is a containerized application. The Docker image may be pulled
by issueing the following command in your terminal:

`docker pull wizardsofindustry/quantum-usr`

Alternatively, you may follow the steps described in the next section.
### Python
The **Universal Subject Resolver** application can be installed as a Python package by
running the following command in your terminal:

`pip3 install -r requirements.txt && python3 setup.py install`


## Developing


### Branching strategy

The **Universal Subject Resolver** project uses the *Gitflow Workflow* as its
branching strategy. The image below provides a schematic overview of this
workflow:

![alt text](https://nvie.com/img/git-model@2x.png "Gitflow Workflow")

[Detailed explanation of the Gitflow Workflow](https://nvie.com/posts/a-successful-git-branching-model)
