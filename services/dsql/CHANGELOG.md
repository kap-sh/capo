# aws-sdk-dsql

## 0.14.0

### Minor Changes

- f352830: feat(dsql): generate IAM authentication tokens for cluster connections

  The password of an Aurora DSQL connection is an IAM authentication token. `generate_db_connect_admin_auth_token` returns one for the `admin` role, and `generate_db_connect_auth_token` one for any other database role. Both are signed locally with the client's credentials and region, so nothing is sent to AWS.

  ```python
  import asyncpg
  from capo_dsql import AsyncDSQLClient

  HOST = "abc123.dsql.us-east-1.on.aws"

  async with AsyncDSQLClient(region="us-east-1") as dsql:
      token = await dsql.generate_db_connect_admin_auth_token(hostname=HOST)

      # A role of your own takes a DbConnect token, here valid for an hour
      app_token = await dsql.generate_db_connect_auth_token(hostname=HOST, expires_in=3600)

  # The token is the password
  conn = await asyncpg.connect(
      host=HOST, user="admin", password=token, database="postgres", ssl="require"
  )
  ```

  A token is valid for 15 minutes unless `expires_in` says otherwise, up to a week. The sync `DSQLClient` has the same methods.

## 0.13.0

### Minor Changes

- 685d0f9: feat: sync smithy models for 106 services

## 0.12.0

### Minor Changes

- 862d88b: feat: add adaptive retry mode

## 0.11.0

### Minor Changes

- f2b74de: feat: public union variant types (`<Union><Variant>Member`)

## 0.10.0

### Minor Changes

- 741133f: feat!: represent unknown union variants and events as "$unknown" dicts

## 0.9.0

### Minor Changes

- 36f7363: docs: better pypi description for the packages

## 0.8.0

### Minor Changes

- 15fc422: feat(client): fill missing required members on deserialization
- f8933b0: fix: don't send @default values the caller didn't set
- 2a6dc74: feat: add UnknownUnionMember and UnknownEvent for forward compatibility

## 0.7.0

### Minor Changes

- 742ae0b: feat: resolve credentials from credential_process profiles

## 0.6.0

### Minor Changes

- e18bb0f: feat: attach the HTTP response to all service errors
- 8ff4d5f: feat: add basic logging
- d635b50: feat: add support for retry quotas
- eee4b04: fix: retry well-known AWS throttling and transient error codes

## 0.5.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.4.0

### Minor Changes

- 64d5d1a: fix: fail waiters on unmatched errors and add jitter to polling delay
- 3f69a13: feat add anonymous option to send unsigned requests

## 0.3.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.2.0

### Minor Changes

- d14a26b: update the smithy spec
- ea077db: regenerate services
