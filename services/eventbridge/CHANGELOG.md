# aws-sdk-eventbridge

## 0.20.0

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

## 0.19.0

### Minor Changes

- 862d88b: feat: add adaptive retry mode

## 0.18.0

### Minor Changes

- 741133f: feat!: represent unknown union variants and events as "$unknown" dicts

## 0.17.0

### Minor Changes

- 36f7363: docs: better pypi description for the packages

## 0.16.0

### Minor Changes

- 15fc422: feat(client): fill missing required members on deserialization
- f8933b0: fix: don't send @default values the caller didn't set
- 2a6dc74: feat: add UnknownUnionMember and UnknownEvent for forward compatibility

## 0.15.0

### Minor Changes

- 742ae0b: feat: resolve credentials from credential_process profiles

## 0.14.0

### Minor Changes

- e18bb0f: feat: attach the HTTP response to all service errors
- 8ff4d5f: feat: add basic logging
- d635b50: feat: add support for retry quotas
- eee4b04: fix: retry well-known AWS throttling and transient error codes

## 0.13.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.12.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.11.0

### Minor Changes

- f3c2061: fix: links in operation and type docs rendering as relative URLs because of escaped quotes in docstrings

## 0.10.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.9.0

### Minor Changes

- d14a26b: update the smithy spec

## 0.8.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests

## 0.7.0

### Minor Changes

- 4ddb736: add Body helper back

## 0.6.0

### Minor Changes

- 50a001f: honor disableDoubleEncoding and sign all S3-family services as S3
- a330d6a: do not decompress streaming blob responses
- 74bb9ab: add Body, a replayable streaming request body that survives retries
- 0ff41e5: overlay endpoint authSchemes on the default sigv4 scheme

## 0.5.0

### Minor Changes

- aa2cb1f: cache signing key calculation

## 0.4.0

### Minor Changes

- c397a47: get rid of some type ignores, improve typing

## 0.3.0

### Minor Changes

- 454ecc9: fix the memory leak

## 0.2.0

### Minor Changes

- 5d8c6ad: fix XML deserialization of namespace-prefixed @xmlName
- 1f67d41: handle NaN, infinities per spec
- 9e68753: treat explicit JSON nulls as absent in deserializers
- 70a7337: properly handle timezones
