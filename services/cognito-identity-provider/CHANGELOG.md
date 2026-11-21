# aws-sdk-cognito-identity-provider

## 0.16.0

### Minor Changes

- 6beed3f: fix: send operations that take no credentials unsigned

  Some operations take no AWS credentials: the caller proves who they are with a token in the request, as in `assume_role_with_web_identity`, the Cognito sign-in calls and the IAM Identity Center device flow. They were still signed whenever the client had a credentials provider, so they failed on a machine where no credentials could be found. They are now always sent unsigned, and no credentials are resolved for them.

  ```python
  from capo_sts import AsyncSTSClient

  # No AWS credentials on this machine, only the OIDC token
  async with AsyncSTSClient(region="us-east-1") as sts:
      response = await sts.assume_role_with_web_identity(
          "arn:aws:iam::123456789012:role/app", "session", token
      )
      credentials = response["credentials"]
  ```

  Passing `anonymous=True` to the client for these calls is no longer needed.

- 802a66a: chore: regenerate services, no API changes

## 0.15.0

### Minor Changes

- 685d0f9: feat: sync smithy models for 106 services

## 0.14.0

### Minor Changes

- 862d88b: feat: add adaptive retry mode

## 0.13.0

### Minor Changes

- 741133f: feat!: represent unknown union variants and events as "$unknown" dicts

## 0.12.0

### Minor Changes

- 36f7363: docs: better pypi description for the packages

## 0.11.0

### Minor Changes

- 15fc422: feat(client): fill missing required members on deserialization
- f8933b0: fix: don't send @default values the caller didn't set
- 2a6dc74: feat: add UnknownUnionMember and UnknownEvent for forward compatibility

## 0.10.0

### Minor Changes

- 742ae0b: feat: resolve credentials from credential_process profiles

## 0.9.0

### Minor Changes

- e18bb0f: feat: attach the HTTP response to all service errors
- 8ff4d5f: feat: add basic logging
- d635b50: feat: add support for retry quotas
- eee4b04: fix: retry well-known AWS throttling and transient error codes

## 0.8.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.7.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.6.0

### Minor Changes

- f3c2061: fix: links in operation and type docs rendering as relative URLs because of escaped quotes in docstrings
- 5f29843: feat: add two more services, update smithy for 44 services

## 0.5.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.4.0

### Minor Changes

- d14a26b: update the smithy spec

## 0.3.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests

## 0.2.0

### Minor Changes

- 4ddb736: add Body helper back
