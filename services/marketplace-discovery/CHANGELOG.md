# aws-sdk-marketplace-discovery

## 0.13.0

### Minor Changes

- 5a3e5cb: feat: sign requests with SigV4A

  Some AWS endpoints are signed with Signature Version 4A, where one signature is valid in several regions: S3 Multi-Region Access Points, EventBridge global endpoints, SES multi-region endpoints, CloudFront KeyValueStore, and the Sustainability and Partner Central APIs. Calls to them used to fail before anything was sent, with "Endpoint requires an unsupported auth scheme: sigv4a" or `NotImplementedError`. The client now signs them with SigV4A on its own, with the same credentials it uses everywhere else.

  ```python
  from capo_s3 import AsyncS3Client

  MRAP = "arn:aws:s3::123456789012:accesspoint/mfzwi23gnjvgw.mrap"

  async with AsyncS3Client(region="us-east-1") as s3:
      # A Multi-Region Access Point takes the place of the bucket name
      await s3.put_object(MRAP, "report.csv", body=b"id,total\n1,42\n")
  ```

  Nothing new has to be installed: the signature is computed in pure Python, and the `cryptography` package is used instead when it is installed.

## 0.12.0

### Minor Changes

- 862d88b: feat: add adaptive retry mode
- 8b32b6d: feat: sync smithy models for 19 services

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

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.3.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.2.0

### Minor Changes

- d14a26b: update the smithy spec
