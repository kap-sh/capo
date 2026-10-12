# aws-sdk-mpa

## 0.6.0

### Minor Changes

- 66c56b4: fix: sign requests whose path contains an ARN or a literal "@"/"$"
- 3445285: chore: bump minimal zapros version to 0.21.0
- 5facfed: fix: reuse the client's handler for the default credentials chain

## 0.5.0

### Minor Changes

- 3f69a13: feat add anonymous option to send unsigned requests

## 0.4.0

### Minor Changes

- f3c2061: fix: links in operation and type docs rendering as relative URLs because of escaped quotes in docstrings

## 0.3.0

### Minor Changes

- f6fe1c8: fix: 429, transient 5xx and responses not being retried unless the error is marked

## 0.2.0

### Minor Changes

- d14a26b: update the smithy spec
