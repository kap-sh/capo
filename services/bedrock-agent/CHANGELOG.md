# aws-sdk-bedrock-agent

## 0.5.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests

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
