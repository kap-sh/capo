# aws-sdk-bedrock-agentcore

## 0.12.0

### Minor Changes

- 742ae0b: feat: resolve credentials from credential_process profiles
- fc67135: regenerate services

## 0.11.0

### Minor Changes

- e18bb0f: feat: attach the HTTP response to all service errors
- 8ff4d5f: feat: add basic logging
- d635b50: feat: add support for retry quotas
- eee4b04: fix: retry well-known AWS throttling and transient error codes

## 0.10.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.9.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.8.0

### Minor Changes

- f3c2061: fix: links in operation and type docs rendering as relative URLs because of escaped quotes in docstrings

## 0.7.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.6.0

### Minor Changes

- d14a26b: update the smithy spec

## 0.5.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests
- 30428e8: fix(eventstream): dispatch modelled errors on :exception-type
- d8d1219: feat(eventstream): full event headers and implicit payloads

## 0.4.0

### Minor Changes

- 4ddb736: add Body helper back

## 0.3.0

### Minor Changes

- fce8b82: regenerate services

## 0.2.0

### Minor Changes

- 50a001f: honor disableDoubleEncoding and sign all S3-family services as S3
- a330d6a: do not decompress streaming blob responses
- 74bb9ab: add Body, a replayable streaming request body that survives retries
- 0ff41e5: overlay endpoint authSchemes on the default sigv4 scheme
