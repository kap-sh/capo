# aws-sdk-codeconnections

## 0.5.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.4.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.3.0

### Minor Changes

- ee9fd83: fix(auth): honor aws.auth#unsignedPayload when signing
- 86ce12c: eventstream: include message CRC in total_length
- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests

## 0.2.0

### Minor Changes

- 4ddb736: add Body helper back
