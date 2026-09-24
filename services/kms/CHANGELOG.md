# aws-sdk-kms

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
