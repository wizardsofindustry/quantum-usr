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

## Features
- Resolve **Principals** to **Subjects** (represented by a *Global Subject Identifier*
  (GSID)) through an easy-to-use HTTP interface.
- Supports Username, RFC822 (email address), X.509 certificate.

## Security considerations
- This service is deployed in the `citadel` environment. Clients are assumed
  to be *internal* and authorized at the network level.


## Installation

### Docker
The **Universal Subject Resolver** is a containerized application. The Docker image may be pulled
by issueing the following command in your terminal:

`docker pull wizardsofindustry/quantum-usr`

Alternatively, you may follow the steps described in the next section.
### Python
The **Universal Subject Resolver** application can be installed as a Python package by
running the following command in your terminal:

`pip3 install -r requirements.txt && python3 setup.py install`


