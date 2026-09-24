# aws-sdk-transcribe-streaming

## 0.2.0

### Minor Changes

- be3f0d5: fix: use STREAMING-AWS4-HMAC-SHA256-EVENTS for signing event stream requests
- 906c76f: fix(auth): sign request event streams per event (`:date` + `:chunk-signature` frames chained from the request signature, plus the empty end frame); `sign_sigv4` now takes `unsigned_payload` instead of a `body` argument
- 30428e8: fix(eventstream): dispatch modelled errors on :exception-type
- d8d1219: feat(eventstream): full event headers and implicit payloads
