# aws-sdk-abuse-signal

## 0.2.0

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

## 0.1.0

### Minor Changes

- 28169de: feat: add six new services
