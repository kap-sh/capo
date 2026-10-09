# aws-sdk-cloudformation

## 0.7.0

### Minor Changes

- 64d5d1a: fix: fail waiters on unmatched errors and add jitter to polling delay
- 3f69a13: feat add anonymous option to send unsigned requests
- 998a58e: feat: sync smithy models for 25 services with upstream (2026-10-08) and regenerate the 18 with API changes

## 0.6.0

### Minor Changes

- f3c2061: fix: links in operation and type docs rendering as relative URLs because of escaped quotes in docstrings

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
