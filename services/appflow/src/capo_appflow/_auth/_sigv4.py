"""AWS Signature Version 4 — single-chunk signing.

Reference:
    https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html

Verified byte-for-byte against ``botocore.auth.S3SigV4Auth`` / ``SigV4Auth``
across S3 GET/PUT/POST, query-string, session-token, and non-S3 (IAM)
canonicalization paths.
"""

from __future__ import annotations

import datetime as _dt
import functools
import hashlib
import hmac
import re
from typing import Any, Literal, TypedDict
from urllib.parse import quote, unquote

import zapros
from pywhatwgurl import URLSearchParams
from zapros import Headers, Request
from zapros._utils import get_host_header_value


def build_sigv4_auth_scheme(
    signing_name: str, region: str | None, endpoint_scheme: dict[str, Any] | None = None
) -> dict[str, Any] | None:
    """Return the sigv4 auth scheme for ``signing_name``/``region``, with the
    endpoint rule set's matching ``authSchemes`` entry overlaid on top.

    The rule set only *modifies* signing properties of the resolved scheme
    (Smithy rules engine, ``authSchemes``): keys it carries win, keys it omits
    keep the operation defaults — IAM's global endpoint names only
    ``signingRegion``, for instance. Returns None when no signing region is
    known from either source.
    """
    scheme: dict[str, Any] = {
        "name": "sigv4",
        "signingName": signing_name,
        "signingRegion": region,
        "disableDoubleEncoding": False,
        "disableNormalizePath": False,
    }
    if endpoint_scheme:
        scheme.update(endpoint_scheme)
    if scheme.get("signingRegion") is None:
        return None
    return scheme


class SigV4AuthContext(TypedDict):
    type: Literal["sig_v4"]
    access_key_id: str
    secret_access_key: str
    session_token: str | None
    signing_region: str
    signing_name: str
    # Rules-engine sigv4 auth-scheme flags (False = standard SigV4: normalize
    # dot segments, double-encode the path). S3-family endpoint rulesets set
    # ``disableDoubleEncoding`` so the path is signed exactly as sent.
    disable_double_encoding: bool
    disable_normalize_path: bool


_SIGV4_ALGORITHM = "AWS4-HMAC-SHA256"
_EMPTY_PAYLOAD_SHA256 = hashlib.sha256(b"").hexdigest()

# Headers excluded from the signed-headers set. Mirrors botocore's denylist:
# these are hop-by-hop / mutable in transit, so signing them would break
# proxies or duplicate values already added by the transport layer.
_UNSIGNED_HEADERS = frozenset(
    {
        "authorization",
        "cache-control",
        "connection",
        "expect",
        "from",
        "keep-alive",
        "max-forwards",
        "pragma",
        "referer",
        "te",
        "trailer",
        "transfer-encoding",
        "upgrade",
        "user-agent",
        "x-amzn-trace-id",
        "content-length",
        "accept",
        "accept-encoding",
    }
)

_MULTI_SPACE = re.compile(r" +")

# Services that require the payload hash to travel in ``x-amz-content-sha256``
# on every request, and that accept ``UNSIGNED-PAYLOAD`` for any operation.
# Other services sign the hash into the canonical request without sending it,
# and only see the header when the payload is left unsigned.
S3_SIGNING_NAMES = frozenset({"s3", "s3express", "s3-outposts", "s3-object-lambda"})


def _uri_encode(value: str) -> str:
    """RFC 3986 percent-encoding using only the unreserved set as safe."""
    return quote(value, safe="-_.~")


def _remove_dot_segments(path: str) -> str:
    """RFC 3986 §5.2.4 dot-segment removal (mirrors botocore's normalize_url_path)."""
    segments: list[str] = []
    for seg in path.split("/"):
        if not seg or seg == ".":
            continue
        if seg == "..":
            if segments:
                segments.pop()
        else:
            segments.append(seg)
    first = "/" if path.startswith("/") else ""
    last = "/" if path.endswith("/") and segments else ""
    return first + "/".join(segments) + last


def _canonical_path(path: str, *, double_encode: bool, normalize: bool) -> str:
    """Build CanonicalURI.

    Per the SigV4 spec, every segment is URI-encoded; standard services
    normalize dot segments and URI-encode each segment **twice**. The
    rules-engine ``disableNormalizePath`` / ``disableDoubleEncoding`` flags
    turn those steps off — S3-family services set both, so the path is
    signed exactly as provided.
    """
    if not path:
        return "/"
    if not path.startswith("/"):
        path = "/" + path
    if normalize:
        path = _remove_dot_segments(path)
    if not double_encode:
        return path
    decoded = unquote(path)
    first = quote(decoded, safe="/~")
    return quote(first, safe="/~")


def _canonical_query(query: str) -> str:
    """Build CanonicalQueryString from a raw query string (with or without ``?``)."""
    if not query:
        return ""
    if query.startswith("?"):
        query = query[1:]
    if not query:
        return ""
    sp = URLSearchParams(query)
    encoded = sorted((_uri_encode(k), _uri_encode(v)) for k, v in sp.entries())
    return "&".join(f"{k}={v}" for k, v in encoded)


def _trim_header_value(value: str) -> str:
    """Trim leading/trailing whitespace and collapse internal whitespace runs.

    Spec note: the canonical form treats sequential whitespace inside an
    unquoted value as a single space. We do not parse quoted-string syntax;
    the conservative collapse is correct for every header AWS actually signs.
    """
    return _MULTI_SPACE.sub(" ", value.strip())


def _canonical_headers(headers: Headers) -> tuple[str, str]:
    """Return ``(canonical_headers, signed_headers)``."""
    grouped: dict[str, list[str]] = {}
    for name in headers:
        lname = name.lower()
        if lname in _UNSIGNED_HEADERS:
            continue
        grouped[lname] = [_trim_header_value(v) for v in headers.getall(name)]

    signed = sorted(grouped)
    canonical = "".join(f"{name}:{','.join(grouped[name])}\n" for name in signed)
    return canonical, ";".join(signed)


def _build_canonical_request(
    *,
    method: str,
    path: str,
    query: str,
    headers: Headers,
    payload_hash: str,
    double_encode: bool,
    normalize: bool,
) -> tuple[str, str]:
    canonical_uri = _canonical_path(
        path, double_encode=double_encode, normalize=normalize
    )
    canonical_query = _canonical_query(query)
    canonical_headers, signed_headers = _canonical_headers(headers)
    canonical_request = (
        f"{method}\n"
        f"{canonical_uri}\n"
        f"{canonical_query}\n"
        f"{canonical_headers}\n"
        f"{signed_headers}\n"
        f"{payload_hash}"
    )
    return canonical_request, signed_headers


@functools.lru_cache(maxsize=8)
def _derive_signing_key(secret: str, date: str, region: str, service: str) -> bytes:
    # The key depends only on the UTC date stamp (not the full timestamp),
    # so it is reused for every request in the same day/region/service.
    k_date = hmac.new(
        b"AWS4" + secret.encode("utf-8"), date.encode("ascii"), hashlib.sha256
    ).digest()
    k_region = hmac.new(k_date, region.encode("utf-8"), hashlib.sha256).digest()
    k_service = hmac.new(k_region, service.encode("utf-8"), hashlib.sha256).digest()
    return hmac.new(k_service, b"aws4_request", hashlib.sha256).digest()


def _amz_now() -> _dt.datetime:
    return _dt.datetime.now(_dt.timezone.utc)


def _canonical_query_from_pairs(pairs: list[tuple[str, str]]) -> str:
    """CanonicalQueryString from raw (unencoded) key/value pairs."""
    encoded = sorted((_uri_encode(k), _uri_encode(v)) for k, v in pairs)
    return "&".join(f"{k}={v}" for k, v in encoded)


def sign_sigv4(
    request: Request,
    ctx: SigV4AuthContext,
    body: bytes | None,
) -> Request:
    """Return a new ``Request`` carrying SigV4 single-chunk auth headers.

    Pass ``body=None`` to sign with ``UNSIGNED-PAYLOAD`` (streaming S3 requests
    and operations carrying ``aws.auth#unsignedPayload``). The original
    ``request.body`` is forwarded unchanged in that case.
    """
    service = ctx["signing_name"]
    region = ctx["signing_region"]

    headers = request.headers.copy()

    # X-Amz-Date — honor caller-supplied value (allows deterministic tests).
    existing_date = headers.get("X-Amz-Date")
    if existing_date:
        amz_date = existing_date
        date_stamp = amz_date[:8]
    else:
        now = _amz_now()
        amz_date = now.strftime("%Y%m%dT%H%M%SZ")
        date_stamp = now.strftime("%Y%m%d")
        headers["X-Amz-Date"] = amz_date

    # Payload hash. For S3-family services, x-amz-content-sha256 is mandatory;
    # for every service it is the only way to announce an unsigned payload.
    # Either way it must be set BEFORE computing the canonical request (it
    # gets signed).
    payload_hash = headers.get("X-Amz-Content-SHA256")
    if payload_hash is None:
        if body is None:
            payload_hash = "UNSIGNED-PAYLOAD"
        else:
            payload_hash = (
                hashlib.sha256(body).hexdigest() if body else _EMPTY_PAYLOAD_SHA256
            )
    if service in S3_SIGNING_NAMES or body is None:
        headers["X-Amz-Content-SHA256"] = payload_hash

    # Session token (STS / assumed-role credentials).
    session_token = ctx.get("session_token")
    if session_token:
        headers["X-Amz-Security-Token"] = session_token

    # Host header is added by Request.__init__ from the URL; defensive fallback.
    if "host" not in headers and request.url.hostname:
        headers["Host"] = get_host_header_value(request.url)

    canonical_request, signed_headers = _build_canonical_request(
        method=request.method.upper(),
        path=request.url.pathname,
        query=request.url.search,
        headers=headers,
        payload_hash=payload_hash,
        double_encode=not ctx["disable_double_encoding"],
        normalize=not ctx["disable_normalize_path"],
    )

    credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
    string_to_sign = (
        f"{_SIGV4_ALGORITHM}\n"
        f"{amz_date}\n"
        f"{credential_scope}\n"
        f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
    )

    signing_key = _derive_signing_key(
        ctx["secret_access_key"], date_stamp, region, service
    )
    signature = hmac.new(
        signing_key, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    headers["Authorization"] = (
        f"{_SIGV4_ALGORITHM} "
        f"Credential={ctx['access_key_id']}/{credential_scope},"
        f"SignedHeaders={signed_headers},"
        f"Signature={signature}"
    )

    effective_body = body if body is not None else request.body
    if effective_body is not None:
        return Request(
            request.url,
            request.method,
            headers,
            body=effective_body,
            context=request.context,
        )
    return Request(request.url, request.method, headers, context=request.context)


def presign_sigv4(
    request: Request,
    ctx: SigV4AuthContext,
    *,
    expires_in: int = 3600,
    now: _dt.datetime | None = None,
) -> Request:
    """Return a new ``Request`` whose URL carries SigV4 query-string auth.

    The signature travels in the URL (``X-Amz-*`` query params), so the result
    is usable standalone (browser, curl). Payload is signed as
    ``UNSIGNED-PAYLOAD``, so the body is not bound by the signature.

    ``expires_in`` is the validity window in seconds; range 1..604800 (7 days),
    bounded by the max lifetime of the derived signing key.
    """
    if not 1 <= expires_in <= 604800:
        raise ValueError(f"expires_in must be in [1, 604800], got {expires_in}")

    sign_time = now or _amz_now()
    if sign_time.tzinfo is None:
        raise ValueError("now must be timezone-aware (UTC)")

    service = ctx["signing_name"]
    region = ctx["signing_region"]

    amz_date = sign_time.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = sign_time.strftime("%Y%m%d")
    credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"

    # Canonical headers: host is mandatory; anything else already on the request
    # is signed too (and must then be sent alongside the URL). Strip the headers
    # that belong in the query string to avoid header/query value conflicts
    # (which AWS rejects as InvalidRequest).
    headers = request.headers.copy()
    for h in (
        "Authorization",
        "X-Amz-Date",
        "X-Amz-Content-SHA256",
        "X-Amz-Security-Token",
    ):
        if h in headers:
            del headers[h]
    if "host" not in headers and request.url.hostname:
        headers["Host"] = get_host_header_value(request.url)

    canonical_headers, signed_headers = _canonical_headers(headers)

    # Signed query params (raw values). X-Amz-Signature is appended afterwards.
    amz_params: list[tuple[str, str]] = [
        ("X-Amz-Algorithm", _SIGV4_ALGORITHM),
        ("X-Amz-Credential", f"{ctx['access_key_id']}/{credential_scope}"),
        ("X-Amz-Date", amz_date),
        ("X-Amz-Expires", str(expires_in)),
        ("X-Amz-SignedHeaders", signed_headers),
    ]
    session_token = ctx.get("session_token")
    if session_token:
        # S3 and most services require the token inside the canonical query.
        # (A few — e.g. iotdevicegateway — want it appended post-signature
        # instead; handle those as a special case if you ever target them.)
        amz_params.append(("X-Amz-Security-Token", session_token))

    existing = list(URLSearchParams(request.url.search).entries())
    canonical_query = _canonical_query_from_pairs(existing + amz_params)

    canonical_uri = _canonical_path(
        request.url.pathname,
        double_encode=not ctx["disable_double_encoding"],
        normalize=not ctx["disable_normalize_path"],
    )
    canonical_request = (
        f"{request.method.upper()}\n"
        f"{canonical_uri}\n"
        f"{canonical_query}\n"
        f"{canonical_headers}\n"
        f"{signed_headers}\n"
        f"UNSIGNED-PAYLOAD"
    )

    string_to_sign = (
        f"{_SIGV4_ALGORITHM}\n"
        f"{amz_date}\n"
        f"{credential_scope}\n"
        f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
    )
    signing_key = _derive_signing_key(
        ctx["secret_access_key"], date_stamp, region, service
    )
    signature = hmac.new(
        signing_key, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    # X-Amz-Signature is hex (no encoding needed) and is NOT part of the
    # canonical query. The sorted canonical query doubles as the URL query.
    final_query = f"{canonical_query}&X-Amz-Signature={signature}"

    url = request.url
    fragment = url.hash or ""
    presigned_href = zapros.URL(
        f"{url.protocol}//{url.host}{url.pathname}?{final_query}{fragment}"
    )

    if request.body is not None:
        return Request(
            presigned_href,
            request.method,
            headers,
            body=request.body,
            context=request.context,
        )
    return Request(presigned_href, request.method, headers, context=request.context)
