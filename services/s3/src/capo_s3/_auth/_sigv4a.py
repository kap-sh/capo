"""AWS Signature Version 4A — asymmetric, multi-region request signing.

SigV4A signs the same canonical request as SigV4, with three differences:

* the signature is ECDSA P-256 over the string to sign, hex-encoded DER,
  made with a private key derived from the secret access key;
* the credential scope has no region: the regions the signature is valid in
  travel in the signed ``X-Amz-Region-Set`` header instead;
* the algorithm name is ``AWS4-ECDSA-P256-SHA256``.

ECDSA comes from the ``cryptography`` package when it is installed. When it
is not, the implementation in this module signs instead, so that signing
never needs a compiled dependency. Python integers do not run in constant
time, so that implementation is built to keep the nonce from deciding how
much work a signature takes:

* the nonce is derived from the private key and the message as RFC 6979
  does, mixed with fresh randomness (its section 3.6). A weak random source
  can neither repeat nor bias a nonce, and no two signatures share one;
* the nonce never decides a branch or a loop count. Multiplying the generator
  is 64 table lookups and 64 additions of full-size points whatever the
  nonce, the addition formulas have no special cases, and both modular
  inversions are exponentiations by a public exponent.

What is left is the time of single operations on integers, which CPython
makes depend on their size in machine words and not on their value.

Reference:
    https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-signing-elements.html

Verified against the ``v4a`` vectors of the aws-c-auth signing test suite and
the P-256 vectors of RFC 6979.
"""

from __future__ import annotations

import functools
import hashlib
import hmac
import os
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Literal, TypedDict

from zapros import Request
from zapros._utils import get_host_header_value

from capo_s3._auth._sigv4 import (
    _AMZ_DATE_FORMAT,
    _EMPTY_PAYLOAD_SHA256,
    S3_SIGNING_NAMES,
    _amz_now,
    _build_canonical_request,
)

# ``cryptography`` is optional: without it ``ec`` stays ``None`` and the
# implementation below signs.
if TYPE_CHECKING:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import ec
else:
    try:
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import ec
    except ImportError:
        hashes = None
        ec = None

_SIGV4A_ALGORITHM = "AWS4-ECDSA-P256-SHA256"

# NIST P-256 (secp256r1, FIPS 186-4 D.1.2.3): the curve y^2 = x^3 - 3x + b over
# the integers modulo a prime, and the generator of its group of prime order.
_P256_PRIME = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
_P256_B = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
_P256_3B = 3 * _P256_B % _P256_PRIME
# A private key is an integer in [1, order - 1].
_P256_ORDER = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551

# A point (X : Y : Z) in projective coordinates is the point (X / Z, Y / Z) of
# the curve, or the point at infinity when Z is 0.
_Point = tuple[int, int, int]
_P256_GENERATOR: _Point = (
    0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
    0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5,
    1,
)
_INFINITY: _Point = (0, 1, 0)


def build_sigv4a_auth_scheme(
    signing_name: str, auth_schemes: list[dict[str, Any]] | None
) -> dict[str, Any] | None:
    """Return the sigv4a auth scheme to sign with, or None when the endpoint
    does not offer sigv4a.

    ``auth_schemes`` is the endpoint rule set's ``authSchemes`` list. SigV4A has
    no defaults to fall back on: the regions a signature is valid in come from
    the endpoint's ``sigv4a`` entry, so without one the answer is None.
    """
    for scheme in auth_schemes or []:
        if scheme["name"] == "sigv4a":
            return {"signingName": signing_name, **scheme}
    return None


class SigV4AAuthContext(TypedDict):
    type: Literal["sig_v4a"]
    access_key_id: str
    secret_access_key: str
    session_token: str | None
    # Regions the signature is valid in; ``["*"]`` means every region.
    signing_region_set: list[str]
    signing_name: str
    disable_double_encoding: bool
    disable_normalize_path: bool


def _derive_signing_key(access_key_id: str, secret_access_key: str) -> int:
    """Derive the ECDSA P-256 private key of a pair of AWS credentials.

    NIST SP 800-108 KDF in counter mode over HMAC-SHA256, keyed with
    ``"AWS4A" + secret``. The 256-bit output ``c`` becomes the private key
    ``c + 1`` when ``c <= order - 2``; otherwise the counter byte is bumped
    and the derivation repeated (about one time in 2**32).
    """
    secret = b"AWS4A" + secret_access_key.encode("utf-8")
    for counter in range(1, 255):
        fixed_input = (
            b"\x00\x00\x00\x01"  # KDF block index
            + _SIGV4A_ALGORITHM.encode("ascii")  # label
            + b"\x00"
            + access_key_id.encode("utf-8")  # context
            + bytes([counter])
            + b"\x00\x00\x01\x00"  # output length in bits
        )
        candidate = int.from_bytes(
            hmac.new(secret, fixed_input, hashlib.sha256).digest(), "big"
        )
        if candidate <= _P256_ORDER - 2:
            return candidate + 1
    raise RuntimeError("Could not derive a SigV4A signing key from the credentials")


# ---------------------------------------------------------------------------
# ECDSA P-256 in Python, for when ``cryptography`` is not installed
# ---------------------------------------------------------------------------


def _add(p: _Point, q: _Point) -> _Point:
    """Add two points of the curve.

    The complete addition formulas of Renes, Costello and Batina
    (https://eprint.iacr.org/2015/1060) with a = -3. The same arithmetic is
    right for every pair of points, be they equal, opposite or at infinity,
    so nothing here branches on its inputs.
    """
    x1, y1, z1 = p
    x2, y2, z2 = q
    xx = x1 * x2 % _P256_PRIME
    yy = y1 * y2 % _P256_PRIME
    zz = z1 * z2 % _P256_PRIME
    xy = (x1 * y2 + x2 * y1) % _P256_PRIME
    xz = (x1 * z2 + x2 * z1) % _P256_PRIME
    yz = (y1 * z2 + y2 * z1) % _P256_PRIME
    b_zz = _P256_3B * zz % _P256_PRIME
    b_xz = _P256_3B * xz % _P256_PRIME
    t = 3 * (xx - zz)
    u = yy - 3 * xz + b_zz
    v = yy + 3 * xz - b_zz
    w = b_xz - 3 * xx - 9 * zz
    return (
        (xy * v - yz * w) % _P256_PRIME,
        (t * w + u * v) % _P256_PRIME,
        (yz * u + xy * t) % _P256_PRIME,
    )


@functools.cache
def _generator_table() -> tuple[tuple[tuple[_Point, ...], ...], _Point]:
    """Return what multiplying the generator takes: a table of its multiples
    and the point to add them to.

    Entry ``[i][d]`` of the table is ``(d + 1) * 16**(63 - i) * G``: what hex
    digit ``i`` of a 256-bit scalar contributes to ``scalar * G`` when that
    digit is ``d``, and ``16**(63 - i) * G`` on top. The point to start from
    is minus the sum of those 64 surpluses, so they cancel out.

    The surplus keeps the point at infinity out of the table. Arithmetic on
    that point is quicker than on any other, and a multiplication that added
    it for every zero digit would take the less time the shorter the scalar.
    """
    rows: list[tuple[_Point, ...]] = []
    surplus = _INFINITY
    base = _P256_GENERATOR
    for _ in range(64):
        # Adding to the point at infinity gives the same point with three
        # coordinates of full size: a Z of 1, as the generator has, would
        # be quick to multiply by as well.
        row = [_add(_INFINITY, base)]
        for _ in range(15):
            row.append(_add(row[-1], base))
        rows.append(tuple(row))
        surplus = _add(surplus, row[0])
        base = row[-1]
    x, y, z = surplus
    return tuple(reversed(rows)), (x, _P256_PRIME - y, z)


def _multiply_generator(scalar: int) -> tuple[int, int]:
    """Return the coordinates ``(x, y)`` of ``scalar * G``, for a scalar in
    [1, order - 1].

    One table lookup and one addition for each of the 64 hex digits of the
    scalar. Neither the entry looked up nor the running sum is ever the
    point at infinity, so the work is the same for every scalar.
    """
    rows, point = _generator_table()
    for row, digit in zip(rows, scalar.to_bytes(32, "big").hex()):
        point = _add(point, row[int(digit, 16)])
    x, y, z = point
    z_inverse = pow(z, _P256_PRIME - 2, _P256_PRIME)
    return x * z_inverse % _P256_PRIME, y * z_inverse % _P256_PRIME


def _nonces(private_key: int, digest: bytes, entropy: bytes) -> Iterator[int]:
    """Yield the candidate nonces of RFC 6979 section 3.2 for a private key and
    a SHA-256 digest, each one in [1, order - 1].

    ``entropy`` is the additional input ``k'`` of section 3.6; when it is
    empty the nonces are the deterministic ones of the RFC.
    """
    seed = (
        private_key.to_bytes(32, "big")
        + (int.from_bytes(digest, "big") % _P256_ORDER).to_bytes(32, "big")
        + entropy
    )
    v = b"\x01" * 32
    k = b"\x00" * 32
    k = hmac.digest(k, v + b"\x00" + seed, "sha256")
    v = hmac.digest(k, v, "sha256")
    k = hmac.digest(k, v + b"\x01" + seed, "sha256")
    v = hmac.digest(k, v, "sha256")
    while True:
        v = hmac.digest(k, v, "sha256")
        candidate = int.from_bytes(v, "big")
        if 0 < candidate < _P256_ORDER:
            yield candidate
        k = hmac.digest(k, v + b"\x00", "sha256")
        v = hmac.digest(k, v, "sha256")


def _der_integer(value: int) -> bytes:
    # The extra byte is the zero that keeps a number with its top bit set positive.
    content = value.to_bytes(value.bit_length() // 8 + 1, "big")
    return b"\x02" + bytes([len(content)]) + content


def _ecdsa_sign(private_key: int, digest: bytes, entropy: bytes) -> bytes:
    """Sign a SHA-256 digest with ECDSA P-256 and return the DER signature.

    ``entropy`` is mixed into the nonce, see :func:`_nonces`.
    """
    z = int.from_bytes(digest, "big")
    nonces = _nonces(private_key, digest, entropy)
    while True:
        k = next(nonces)
        r = _multiply_generator(k)[0] % _P256_ORDER
        k_inverse = pow(k, _P256_ORDER - 2, _P256_ORDER)
        s = k_inverse * (z + r * private_key) % _P256_ORDER
        # Zero is not a valid half of a signature (FIPS 186-4, 6.4.1).
        if r and s:
            content = _der_integer(r) + _der_integer(s)
            return b"\x30" + bytes([len(content)]) + content


def sign_sigv4a(
    request: Request,
    ctx: SigV4AAuthContext,
    *,
    unsigned_payload: bool = False,
) -> Request:
    """Return a new ``Request`` carrying SigV4A auth headers.

    The payload hash covers ``request.body``, which must be ``bytes`` or
    ``None``. ``unsigned_payload`` signs ``UNSIGNED-PAYLOAD`` instead and
    forwards any body unchanged (streaming S3 requests).
    """
    service = ctx["signing_name"]

    headers = request.headers.copy()

    # X-Amz-Date — honor caller-supplied value (allows deterministic tests).
    existing_date = headers.get("X-Amz-Date")
    if existing_date:
        amz_date = existing_date
    else:
        amz_date = _amz_now().strftime(_AMZ_DATE_FORMAT)
        headers["X-Amz-Date"] = amz_date
    date_stamp = amz_date[:8]

    headers["X-Amz-Region-Set"] = ",".join(ctx["signing_region_set"])

    # Same payload-hash rules as SigV4 (see sign_sigv4).
    payload_hash = headers.get("X-Amz-Content-SHA256")
    if payload_hash is None:
        if unsigned_payload:
            payload_hash = "UNSIGNED-PAYLOAD"
        elif request.body is None:
            payload_hash = _EMPTY_PAYLOAD_SHA256
        elif isinstance(request.body, bytes):
            payload_hash = hashlib.sha256(request.body).hexdigest()
        else:
            raise TypeError(
                "sign_sigv4a hashes a bytes body only; pass unsigned_payload=True "
                "to send a streamed body without a payload hash"
            )
    if service in S3_SIGNING_NAMES or unsigned_payload:
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

    credential_scope = f"{date_stamp}/{service}/aws4_request"
    string_to_sign = (
        f"{_SIGV4A_ALGORITHM}\n"
        f"{amz_date}\n"
        f"{credential_scope}\n"
        f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
    )

    signing_key = _derive_signing_key(ctx["access_key_id"], ctx["secret_access_key"])
    message = string_to_sign.encode("utf-8")
    if ec is not None:
        signature = ec.derive_private_key(signing_key, ec.SECP256R1()).sign(
            message, ec.ECDSA(hashes.SHA256())
        )
    else:
        signature = _ecdsa_sign(
            signing_key, hashlib.sha256(message).digest(), os.urandom(32)
        )

    headers["Authorization"] = (
        f"{_SIGV4A_ALGORITHM} "
        f"Credential={ctx['access_key_id']}/{credential_scope},"
        f"SignedHeaders={signed_headers},"
        f"Signature={signature.hex()}"
    )

    if request.body is not None:
        return Request(
            request.url,
            request.method,
            headers,
            body=request.body,
            context=request.context,
        )
    return Request(request.url, request.method, headers, context=request.context)
