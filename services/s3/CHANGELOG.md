# aws-sdk-s3

## 0.17.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests
- 30428e8: fix(eventstream): dispatch modelled errors on :exception-type
- d8d1219: feat(eventstream): full event headers and implicit payloads

## 0.16.0

### Minor Changes

- 4ddb736: add Body helper back

## 0.15.0

### Minor Changes

- 0f1b0c8: detect errors in 200 responses of CopyObject, UploadPartCopy and CompleteMultipartUpload
- 50a001f: honor disableDoubleEncoding and sign all S3-family services as S3
- a330d6a: do not decompress streaming blob responses
- 6f6c8ee: add iter_list_objects_v2
- 2e3d7fb: declare xmlns:xsi on Grantee so ACL/logging/restore bodies are well-formed XML
- 74bb9ab: add Body, a replayable streaming request body that survives retries
- 0b4bd53: set the trailing chunk with the checksum for streaming requests
- 0ff41e5: overlay endpoint authSchemes on the default sigv4 scheme
- 7ea0e66: more robust pagination termination

### Patch Changes

- 3b57055: fix: respect `aws.customizations#s3UnwrappedXmlOutput` so `get_bucket_location` returns `location_constraint` instead of `{}`

## 0.14.0

### Minor Changes

- aa2cb1f: cache signing key calculation

## 0.13.0

### Minor Changes

- 65c88ab: raise typed NotFound for S3 HeadObject/HeadBucket empty-body 404s
- 4849b09: respect smithy checksum trait

## 0.12.0

### Minor Changes

- ae570f9: resolve errors from status code when response has no body
- c397a47: get rid of some type ignores, improve typing

## 0.11.0

### Minor Changes

- 454ecc9: fix the memory leak

## 0.10.0

### Minor Changes

- 5d8c6ad: fix XML deserialization of namespace-prefixed @xmlName
- 70a7337: properly handle timezones

## 0.9.0

### Minor Changes

- efc5cc0: regenerate with new smithy files
- cef709a: respect idempotency token trait

## 0.8.0

### Minor Changes

- 314162f: fix error handling

## 0.7.0

### Minor Changes

- 80d1393: regenerate services
- 2784007: add IAM Identity Center (SSO), assume-role and web-identity support to the default credentials chain

## 0.6.0

### Minor Changes

- f64f8a4: fix streaming blob requests with static body
- 6f43445: load the client config from the providers chain
- ab1d012: expose interceptor related classes
- de1a15c: feat: add ecs and ec2 credential providers to the default chain
- 8e3f19a: list possible errors in the operation's docstring
- 1d8a08c: regenerate all the services
- 02d9689: regenerate all the services
- d06898d: fix: import Never type from typing_extensions for older versions compat
- cb488d3: migrate from pyright to ty
- 283fe68: relax enum validation
- f8da526: change the waiter prefix to wait_until
- e666883: Move ensure_async_iterator to \_iter helper file
- 96aafd6: get rid of redundant imports

### Patch Changes

- a716c38: Regenerate SDK services
