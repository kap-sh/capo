# aws-sdk-lambda-web

## 0.4.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.3.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests
- 998a58e: feat: sync smithy models for 25 services with upstream (2026-10-08) and regenerate the 18 with API changes

## 0.2.0

### Minor Changes

- 5f29843: feat: add two more services, update smithy for 44 services
