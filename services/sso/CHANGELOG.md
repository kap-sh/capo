# aws-sdk-sso

## 0.10.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests

## 0.9.0

### Minor Changes

- 4ddb736: add Body helper back

## 0.8.0

### Minor Changes

- 50a001f: honor disableDoubleEncoding and sign all S3-family services as S3
- a330d6a: do not decompress streaming blob responses
- 74bb9ab: add Body, a replayable streaming request body that survives retries
- 0ff41e5: overlay endpoint authSchemes on the default sigv4 scheme

## 0.7.0

### Minor Changes

- aa2cb1f: cache signing key calculation

## 0.6.0

### Minor Changes

- c397a47: get rid of some type ignores, improve typing

## 0.5.0

### Minor Changes

- 454ecc9: fix the memory leak

## 0.4.0

### Minor Changes

- 5d8c6ad: fix XML deserialization of namespace-prefixed @xmlName
- 9e68753: treat explicit JSON nulls as absent in deserializers
- 70a7337: properly handle timezones

## 0.3.0

### Minor Changes

- 314162f: fix error handling

## 0.2.0

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

### Patch Changes

- a716c38: Regenerate SDK services
