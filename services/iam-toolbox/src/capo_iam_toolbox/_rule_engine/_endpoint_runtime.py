"""Endpoint rule-set runtime — hand-written helpers shared by every generated
``_endpoint_rule_set.py``.  Pure, no third-party deps.

Functions mirror the Smithy rules-engine standard library:
https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, TypedDict
from urllib.parse import quote, urlsplit


@dataclass(frozen=True, slots=True)
class Endpoint:
    """Resolved endpoint returned by ``resolve()``.

    Mirrors the rules-engine *Endpoint object*: a ``url`` plus optional
    ``properties`` (arbitrary document values) and ``headers`` (multi-value
    map of header name to list of values).

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/specification.html#endpoint-object
    """

    url: str
    properties: dict[str, Any] = field(default_factory=dict)
    headers: dict[str, list[str]] = field(default_factory=dict)


class EndpointError(Exception):
    """Raised when no endpoint rule matches or an ``error`` rule fires.

    Corresponds to the rules-engine *error rule*: terminates evaluation
    with a diagnostic message produced by the rule set.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/specification.html#error-rule
    """


_PLACEHOLDER = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)(?:#([A-Za-z0-9_.\[\]]+))?\}")


def interpolate(template: str, params: object, locals_: dict[str, Any]) -> str:
    """Expand a rules-engine *template string*.

    Substitutes ``{Name}`` and ``{Name#path.subpath}`` references inside
    ``template``. Names resolve against ``locals_`` first (variables bound
    by ``assign`` conditions), then against ``params`` attributes (any
    object with attribute access — a dataclass, plain class, etc.; not a
    dict).
    ``#path`` segments walk the resolved value via :func:`get_attr`.

    Raises :class:`EndpointError` if a referenced name resolves to ``None``.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/specification.html#template-strings
    """

    def replace(match: re.Match[str]) -> str:
        name, path = match.group(1), match.group(2)

        if name in locals_:
            value = locals_[name]
        elif hasattr(params, name):
            value = getattr(params, name)
        else:
            raise EndpointError(f"interpolate: unknown reference '{name}'")

        if value is None:
            raise EndpointError(f"interpolate: '{name}' is None")

        if path:
            value = get_attr(value, path)

        if value is None:
            raise EndpointError(f"interpolate: '{name}#{path}' is None")

        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    return _PLACEHOLDER.sub(replace, template)


_SEGMENT_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*|\[-?\d+\])")


def get_attr(value: Mapping[str, object] | list[str], path: str) -> object:
    """Rules-engine ``getAttr`` — index into a value by a dotted/bracketed path.

    Walks segments like ``a.b[0].c`` against dicts (key lookup), objects
    (attribute lookup), and indexable sequences (integer index). Any missing
    key, missing attribute, out-of-range index, or non-indexable cursor
    short-circuits to ``None``.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html#getattr-function
    """
    cursor: object = value
    for segment in _SEGMENT_RE.findall(path):
        if cursor is None:
            return None

        if segment.startswith("["):
            # Array index
            idx = int(segment[1:-1])
            try:
                cursor = cursor[idx]  # type: ignore
            except IndexError:
                return None
            except TypeError:
                return None
            except KeyError:
                return None
        else:
            # Field access
            if isinstance(cursor, dict):
                cursor = cursor.get(segment)
            else:
                cursor = getattr(cursor, segment, None)

    return cursor


def string_equals(a: Any, b: Any) -> bool:
    """Rules-engine ``stringEquals`` — strict string equality.

    Both operands must be Python ``str``; any non-str comparand returns
    ``False``.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html#stringequals-function
    """
    return isinstance(a, str) and isinstance(b, str) and a == b


_HOST_LABEL = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")


def substring(value: Any, start: int, stop: int, reverse: bool) -> str | None:
    """Rules-engine ``substring`` — slice an ASCII string by ``[start, stop)``.

    Returns ``None`` when ``value`` is not a string, contains non-ASCII
    code points, or the ``start``/``stop`` indices are negative, equal,
    inverted, or past the end. When ``reverse`` is true, indices count
    from the end of the string toward the start.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html#substring-function
    """
    if not isinstance(value, str):
        return None
    if not value.isascii():
        return None
    if start < 0 or stop < 0 or start >= stop:
        return None
    if stop > len(value):
        return None
    if reverse:
        n = len(value)
        return value[n - stop : n - start]
    return value[start:stop]


def is_valid_host_label(value: Any, allow_subdomains: bool) -> bool:
    """Rules-engine ``isValidHostLabel`` — validate an RFC 1123 host label.

    A label is 1–63 chars of ``[A-Za-z0-9-]`` that does not start or end
    with a hyphen. When ``allow_subdomains`` is true, ``value`` may be a
    dot-separated sequence of such labels (every label must be valid).

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html#isvalidhostlabel-function
    """
    if not isinstance(value, str) or not value:
        return False
    if allow_subdomains:
        labels = value.split(".")
        return bool(labels) and all(_HOST_LABEL.match(label) for label in labels)
    return _HOST_LABEL.match(value) is not None


def uri_encode(value: str | None) -> str:
    """Rules-engine ``uriEncode`` — percent-encode per RFC 3986 §2.3.

    Every character outside the unreserved set ``A-Z a-z 0-9 - _ . ~`` is
    percent-encoded, including ``/``. Non-string input yields ``""``.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html#uriencode-function
    """
    if value is None:
        return ""
    return quote(value, safe="-_.~")


class ParsedUrl(TypedDict):
    scheme: str
    authority: str
    path: str
    normalizedPath: str
    isIp: bool


def parse_url(value: str) -> ParsedUrl | None:
    """Rules-engine ``parseUrl`` — split an HTTP(S) URL into components.

    Returns a :class:`ParsedUrl` with ``scheme``, ``authority`` (host plus
    optional ``:port``), ``path``, ``normalizedPath`` (``path`` guaranteed
    to end in ``/``), and ``isIp`` (true for IPv4 dotted-quad or IPv6
    hosts). Returns ``None`` when ``value`` is not a string, the scheme is
    not ``http``/``https``, or a query/fragment is present.

    Reference:
        https://smithy.io/2.0/additional-specs/rules-engine/standard-library.html#parseurl-function
    """

    try:
        parts = urlsplit(value)

        if parts.scheme not in ("http", "https"):
            return None

        # Smithy parseUrl rejects query strings and fragments.
        if parts.query or parts.fragment:
            return None

        # urlsplit preserves the raw/encoded path.
        path = parts.path

        normalized_path = path if path.endswith("/") else f"{path}/"

        return {
            "scheme": parts.scheme,
            "authority": parts.netloc,
            "path": path,
            "normalizedPath": normalized_path,
            "isIp": _looks_like_ip(parts.hostname or ""),
        }

    except Exception:
        return None


def _looks_like_ip(host: str) -> bool:
    if not host:
        return False
    if ":" in host:  # IPv6 (urlsplit strips brackets from hostname)
        return True
    parts = host.split(".")
    return len(parts) == 4 and all(p.isdigit() for p in parts)


class ParsedArn(TypedDict):
    partition: str
    service: str
    region: str
    accountId: str
    resourceId: list[str]


def aws_parse_arn(arn: Any) -> ParsedArn | None:
    """AWS rules-engine ``aws.parseArn`` — split an ARN into components.

    An ARN has the shape ``arn:<partition>:<service>:<region>:<account>:<resource>``.
    Returns a :class:`ParsedArn` with ``partition``, ``service``, ``region``,
    ``accountId``, and ``resourceId`` (the trailing resource section split
    on ``:`` and ``/``). Returns ``None`` when ``arn`` is not a string, has
    fewer than six ``:``-separated parts, does not begin with ``arn``, or
    has empty ``partition``/``service``/resource sections. ``region`` and
    ``accountId`` may be empty (e.g. IAM ARNs have no region).

    Reference:
        https://smithy.io/2.0/aws/rules-engine/standard-library.html#aws-parsearn-function
    """
    if not isinstance(arn, str):
        return None
    parts = arn.split(":", 5)
    if len(parts) != 6:
        return None
    prefix, partition, service, region, account_id, resource = parts
    if prefix != "arn" or not partition or not service or not resource:
        return None
    return {
        "partition": partition,
        "service": service,
        "region": region,
        "accountId": account_id,
        "resourceId": re.split(r"[:/]", resource),
    }


_S3_BUCKET_LABEL = re.compile(r"^[a-z0-9][a-z0-9\-]{1,61}[a-z0-9]$")
_IPV4 = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")


def aws_is_virtual_hostable_s3_bucket(value: Any, allow_subdomains: Any) -> bool:
    """AWS rules-engine ``aws.isVirtualHostableS3Bucket`` — validate an S3
    bucket name for virtual-hosted-style addressing.

    Returns ``True`` when ``value`` is a DNS-compliant S3 bucket name
    (3–63 chars, lowercase alphanumeric plus hyphens, no leading/trailing
    hyphen, no IPv4-address shape). When ``allow_subdomains`` is true,
    dotted bucket names are accepted and each dot-separated label must
    independently satisfy the same rules.

    Reference:
        https://smithy.io/2.0/aws/rules-engine/standard-library.html#aws-isvirtualhostables3bucket-function
    """
    if not isinstance(value, str):
        return False
    if allow_subdomains:
        labels = value.split(".")
        return all(aws_is_virtual_hostable_s3_bucket(label, False) for label in labels)
    if _IPV4.match(value):
        return False
    return _S3_BUCKET_LABEL.match(value) is not None


def apply_label(url: str, placeholder: str, value: str) -> str:
    """Substitute ``placeholder`` in ``url`` with ``value`` — except when the
    rule engine has already embedded ``value`` as a whole host label or path
    segment. In that case, strip the placeholder and collapse any resulting
    ``//`` or trailing ``/`` in the path.

    "Part" = host label (split on ``.``) or path segment (split on ``/``).
    Match is case-sensitive, whole-part only. An empty ``value`` always
    substitutes (never matches).
    """
    if placeholder not in url:
        return url

    if not value:
        return url.replace(placeholder, "")

    try:
        parsed = urlsplit(url)
        # urlsplit.hostname lowercases the value, which would break the
        # case-sensitive membership test below.  Extract from netloc manually
        # to preserve the original casing.
        netloc = parsed.netloc or ""
        host = (
            netloc.rsplit(":", 1)[0]
            if ":" in netloc and not netloc.startswith("[")
            else netloc
        )
        path = parsed.path or ""
    except Exception:
        # Parse failure -> fall back to substitution (defensive).
        return url.replace(placeholder, quote(value, safe=""))

    host_labels = host.split(".") if host and not host.startswith("[") else []
    path_segments = [seg for seg in path.split("/") if seg]

    # Guard: only strip when the placeholder is in the path portion. If the
    # placeholder appears only in a query string or fragment, a coincidental
    # host/path match must not trigger the strip branch.
    scheme_sep = url.find("://")
    head_end = url.find("/", scheme_sep + 3) if scheme_sep != -1 else -1
    path_portion = url[head_end:] if head_end != -1 else ""
    # Strip query and fragment off the path portion for the placeholder check.
    for sep in ("?", "#"):
        idx = path_portion.find(sep)
        if idx != -1:
            path_portion = path_portion[:idx]
    if placeholder not in path_portion:
        return url.replace(placeholder, quote(value, safe=""))

    if value in host_labels or value in path_segments:
        # Splice the placeholder out, then collapse the one seam slash our
        # removal may have created. Pre-existing slash duplicates in the
        # URI template are not our concern — we only fix what we caused.
        idx = url.find(placeholder)
        stripped = url[:idx] + url[idx + len(placeholder) :]
        before = stripped[idx - 1] if idx > 0 else ""
        after = stripped[idx] if idx < len(stripped) else ""
        if before == "/" and after == "/":
            stripped = stripped[:idx] + stripped[idx + 1 :]
        # Placeholder at the path's tail leaves a stray trailing ``/``.
        if stripped.endswith("/"):
            stripped = stripped[:-1]
        return stripped

    return url.replace(placeholder, quote(value, safe=""))
