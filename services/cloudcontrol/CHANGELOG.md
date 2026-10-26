# aws-sdk-cloudcontrol

## 0.11.0

### Minor Changes

- 36f7363: docs: better pypi description for the packages

## 0.10.0

### Minor Changes

- 15fc422: feat(client): fill missing required members on deserialization
- 2a6dc74: feat: add UnknownUnionMember and UnknownEvent for forward compatibility

## 0.9.0

### Minor Changes

- 742ae0b: feat: resolve credentials from credential_process profiles

## 0.8.0

### Minor Changes

- e18bb0f: feat: attach the HTTP response to all service errors
- 8ff4d5f: feat: add basic logging
- d635b50: feat: add support for retry quotas
- eee4b04: fix: retry well-known AWS throttling and transient error codes

## 0.7.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.6.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.5.0

### Minor Changes

- f3c2061: fix: links in operation and type docs rendering as relative URLs because of escaped quotes in docstrings

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
