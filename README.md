# Universal Subject Resolver (USR)

The Universal Subject Resolver (USR) maintains associations between **Subjects**
and one or many **Principals**. A **Principal**, such as an email address or username,
uniquely resolves to a **Subject**, simplifying the identification, authentication
and maintenance of users in a single system.

## Table of Contents

- [Features](#features)
- [Security considerations](#security-considerations)

## Features
- Resolve Principals to Subjects (represented by a *Global Subject Identifier* (GSID))
  through an easy-to-use HTTP interface.
- Supports Username, RFC822 (email address), X.509 certificate.

## Security considerations
- This service is deployed in the `citadel` environment. Clients are assumed
  to be *internal* and authorized at the network level.
