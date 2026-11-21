"""AWS SigV4A signing tests.

Vectors come from the ``v4a`` directory of the aws-c-auth signing test suite
(AKID ``AKIDEXAMPLE`` / secret ``wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY``,
date ``20150830``, region set ``us-east-1``, service ``service``) and from
RFC 6979 appendix A.2.5.

A signature carries fresh randomness, so it cannot be compared to the
vector's. Instead it is verified, with the public key the suite publishes for
these credentials, against the string to sign the suite expects. The verifier
below is textbook ECDSA on affine coordinates: it shares the curve constants
with the signer and none of its arithmetic.

Requests are signed by ``cryptography`` when it is installed and by the
package's own ECDSA when it is not. The ``ecdsa`` fixture runs a test once
with each.
"""

from __future__ import annotations

import asyncio
import hashlib
import importlib.util
import random
import sys
from collections.abc import Iterator

import pytest
from capo_cloudfront_keyvaluestore._auth import _sigv4a
from capo_cloudfront_keyvaluestore._auth._providers import StaticAwsCredentialsProvider
from capo_cloudfront_keyvaluestore._auth._signers import SigV4ASigner
from capo_cloudfront_keyvaluestore._auth._sigv4a import (
    _INFINITY,
    _P256_B,
    _P256_GENERATOR,
    _P256_ORDER,
    _P256_PRIME,
    SigV4AAuthContext,
    _add,
    _der_integer,
    _derive_signing_key,
    _ecdsa_sign,
    _generator_table,
    _multiply_generator,
    _nonces,
    build_sigv4a_auth_scheme,
    sign_sigv4a,
)
from pywhatwgurl import URL
from zapros import Request

_ACCESS_KEY = "AKIDEXAMPLE"
_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY"
_PROVIDER = StaticAwsCredentialsProvider(
    {"access_key": _ACCESS_KEY, "secret_key": _SECRET_KEY}
)

# public-key.json of the test suite.
_PUBLIC_KEY = (
    0xB6618F6A65740A99E650B33B6B4B5BD0D43B176D721A3EDFEA7E7D2D56D936B1,
    0x865ED22A7EADC9C5CB9D2CBACA1B3699139FEDC5043DC6661864218330C8E518,
)

# The P-256 key pair of RFC 6979 A.2.5.
_RFC6979_PRIVATE_KEY = (
    0xC9AFA9D845BA75166B5C215767B1D6934E50C3DB36E89B127B8A622B120F6721
)
_RFC6979_PUBLIC_KEY = (
    0x60FED4BA255A9D31C961EB74C6356D68C049B8923B61FA6CE669622E60F29FB6,
    0x7903FE1008B8BC99A41AE9E95628BC64F2F1B20C2D7E9F5177A3C294D4462299,
)

_TEST_SUITE_CTX: SigV4AAuthContext = {
    "type": "sig_v4a",
    "access_key_id": _ACCESS_KEY,
    "secret_access_key": _SECRET_KEY,
    "session_token": None,
    "signing_region_set": ["us-east-1"],
    "signing_name": "service",
    "disable_double_encoding": False,
    "disable_normalize_path": False,
}

_MRAP_SCHEME = {
    "name": "sigv4a",
    "signingName": "s3",
    "signingRegionSet": ["*"],
    "disableDoubleEncoding": True,
}
_SIGV4_SCHEME = {
    "name": "sigv4",
    "signingName": "s3-outposts",
    "signingRegion": "us-west-2",
    "disableDoubleEncoding": True,
}


def _make_request(
    method: str,
    url: str,
    headers: dict[str, str],
    body: bytes | Iterator[bytes] | None = None,
) -> Request:
    """Build a Request and strip headers Request adds by default that the
    AWS test suite does not include (Accept, User-Agent, Accept-Encoding).
    """
    req = Request(URL(url), method, headers=headers, body=body)
    for h in ("accept", "user-agent", "accept-encoding"):
        if h in req.headers:
            del req.headers[h]
    return req


def _signature(request: Request) -> bytes:
    return bytes.fromhex(request.headers["Authorization"].split("Signature=")[1])


@pytest.fixture(params=["cryptography", "python"])
def ecdsa(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch) -> str:
    """Sign with ``cryptography``, then as if it were not installed."""
    if request.param == "python":
        monkeypatch.setattr(_sigv4a, "ec", None)
    elif _sigv4a.ec is None:
        pytest.skip("cryptography is not installed")
    return request.param


# ---------------------------------------------------------------------------
# Reference arithmetic — textbook formulas on affine points, where None is the
# point at infinity
# ---------------------------------------------------------------------------

_AffinePoint = tuple[int, int] | None
_G = _P256_GENERATOR[:2]


def _affine_add(p: _AffinePoint, q: _AffinePoint) -> _AffinePoint:
    if p is None:
        return q
    if q is None:
        return p
    (x1, y1), (x2, y2) = p, q
    if x1 == x2:
        if (y1 + y2) % _P256_PRIME == 0:
            return None
        slope = (3 * x1 * x1 - 3) * pow(2 * y1, -1, _P256_PRIME)
    else:
        slope = (y2 - y1) * pow(x2 - x1, -1, _P256_PRIME)
    x3 = (slope * slope - x1 - x2) % _P256_PRIME
    return x3, (slope * (x1 - x3) - y1) % _P256_PRIME


def _affine_multiply(scalar: int, point: _AffinePoint) -> _AffinePoint:
    result: _AffinePoint = None
    while scalar:
        if scalar & 1:
            result = _affine_add(result, point)
        point = _affine_add(point, point)
        scalar >>= 1
    return result


def _to_affine(point: tuple[int, int, int]) -> _AffinePoint:
    x, y, z = point
    if z == 0:
        # the one shape the point at infinity may take
        assert x == 0 and y != 0
        return None
    z_inverse = pow(z, -1, _P256_PRIME)
    return x * z_inverse % _P256_PRIME, y * z_inverse % _P256_PRIME


def _decode_der(signature: bytes) -> tuple[int, int]:
    """Return ``(r, s)`` of a DER ECDSA signature, accepting only the one
    encoding DER allows.
    """
    assert signature[0] == 0x30 and signature[1] == len(signature) - 2
    numbers: list[int] = []
    position = 2
    while position < len(signature):
        assert signature[position] == 0x02
        length = signature[position + 1]
        content = signature[position + 2 : position + 2 + length]
        assert len(content) == length > 0
        # positive, and no longer than it has to be
        assert content[0] < 0x80
        assert length == 1 or content[0] != 0 or content[1] >= 0x80
        numbers.append(int.from_bytes(content, "big"))
        position += 2 + length
    r, s = numbers
    return r, s


def _verifies(public_key: tuple[int, int], signature: bytes, message: bytes) -> bool:
    """ECDSA verification (FIPS 186-4, 6.4.2)."""
    r, s = _decode_der(signature)
    if not (0 < r < _P256_ORDER and 0 < s < _P256_ORDER):
        return False
    z = int.from_bytes(hashlib.sha256(message).digest(), "big")
    s_inverse = pow(s, -1, _P256_ORDER)
    point = _affine_add(
        _affine_multiply(z * s_inverse % _P256_ORDER, _G),
        _affine_multiply(r * s_inverse % _P256_ORDER, public_key),
    )
    return point is not None and point[0] % _P256_ORDER == r


# ---------------------------------------------------------------------------
# Curve arithmetic
# ---------------------------------------------------------------------------


def test_generator_is_on_the_curve_and_has_the_group_order():
    x, y = _G
    assert (y * y - (x**3 - 3 * x + _P256_B)) % _P256_PRIME == 0
    assert _affine_multiply(_P256_ORDER - 1, _G) == (x, _P256_PRIME - y)
    assert _affine_multiply(_P256_ORDER, _G) is None


def test_add_has_no_special_cases():
    g = _P256_GENERATOR
    minus_g = (g[0], _P256_PRIME - g[1], 1)
    assert _to_affine(_add(g, g)) == _affine_add(_G, _G)
    assert _to_affine(_add(g, minus_g)) is None
    assert _to_affine(_add(g, _INFINITY)) == _G
    assert _to_affine(_add(_INFINITY, g)) == _G
    assert _to_affine(_add(_INFINITY, _INFINITY)) is None


def test_add_matches_textbook_arithmetic():
    rng = random.Random(1)
    for _ in range(32):
        a = rng.randrange(1, _P256_ORDER)
        b = rng.randrange(1, _P256_ORDER)
        p = _affine_multiply(a, _G)
        q = _affine_multiply(b, _G)
        assert p is not None and q is not None
        # any multiple of the coordinates is the same point
        scale_p = rng.randrange(1, _P256_PRIME)
        scale_q = rng.randrange(1, _P256_PRIME)
        projective_p = (
            p[0] * scale_p % _P256_PRIME,
            p[1] * scale_p % _P256_PRIME,
            scale_p,
        )
        projective_q = (
            q[0] * scale_q % _P256_PRIME,
            q[1] * scale_q % _P256_PRIME,
            scale_q,
        )
        assert _to_affine(_add(projective_p, projective_q)) == _affine_add(p, q)
        assert _to_affine(_add(projective_p, projective_p)) == _affine_add(p, p)


def test_generator_table_holds_every_multiple():
    rows, start = _generator_table()
    base: _AffinePoint = _G
    surplus: _AffinePoint = None
    for row in reversed(rows):
        expected: _AffinePoint = None
        for entry in row:
            expected = _affine_add(expected, base)
            assert _to_affine(entry) == expected
        surplus = _affine_add(surplus, base)
        # sixteen times the base: the base of the next hex digit
        base = expected
    assert surplus is not None
    assert _to_affine(start) == (surplus[0], _P256_PRIME - surplus[1])


def test_generator_table_has_no_point_that_is_quick_to_add():
    """A multiplication must take the same time whatever the scalar's digits
    are. The point at infinity or a coordinate of 1 would be quicker to add
    than the rest: every coordinate here fills as many machine words as the
    prime does.
    """
    rows, start = _generator_table()
    points = [start, *(entry for row in rows for entry in row)]
    assert len(points) == 1 + 64 * 16
    assert min(c.bit_length() for point in points for c in point) > 240


def test_multiply_generator_matches_textbook_arithmetic():
    rng = random.Random(2)
    scalars = [1, 2, 15, 16, 17, 2**255, _P256_ORDER - 2, _P256_ORDER - 1]
    scalars += [rng.randrange(1, _P256_ORDER) for _ in range(16)]
    for scalar in scalars:
        assert _multiply_generator(scalar) == _affine_multiply(scalar, _G), hex(scalar)


# ---------------------------------------------------------------------------
# ECDSA
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("message", "nonce", "r", "s"),
    [
        (
            b"sample",
            0xA6E3C57DD01ABE90086538398355DD4C3B17AA873382B0F24D6129493D8AAD60,
            0xEFD48B2AACB6A8FD1140DD9CD45E81D69D2C877B56AAF991C34D0EA84EAF3716,
            0xF7CB1C942D657C41D436C7A1B6E29F65F3E900DBB9AFF4064DC4AB2F843ACDA8,
        ),
        (
            b"test",
            0xD16B6AE827F17175E040871A1C7EC3500192C4C92677336EC2537ACAEE0008E0,
            0xF1ABB023518351CD71D881567B1EA663ED3EFCF6C5132B354F28D3B0B7D38367,
            0x019F4113742A2B14BD25926B49C649155F267E60D3814B4C0CC84250E46F0083,
        ),
    ],
    ids=["sample", "test"],
)
def test_rfc6979_vectors(message: bytes, nonce: int, r: int, s: int):
    """RFC 6979 A.2.5, P-256 with SHA-256: without entropy the nonce and the
    signature are the RFC's.
    """
    digest = hashlib.sha256(message).digest()
    assert _multiply_generator(_RFC6979_PRIVATE_KEY) == _RFC6979_PUBLIC_KEY
    assert next(_nonces(_RFC6979_PRIVATE_KEY, digest, b"")) == nonce
    signature = _ecdsa_sign(_RFC6979_PRIVATE_KEY, digest, b"")
    assert _decode_der(signature) == (r, s)
    assert _verifies(_RFC6979_PUBLIC_KEY, signature, message)


def test_digest_above_the_group_order():
    """A digest is reduced modulo the order before it seeds the nonce (RFC 6979
    section 2.3.4). The expected signature is the one OpenSSL makes.
    """
    signature = _ecdsa_sign(_RFC6979_PRIVATE_KEY, b"\xff" * 32, b"")
    assert signature.hex() == (
        "304502201f2adbc54b88764c279f689fc9505959fc9e73e80dc20889a4e0be91865de75b"
        "0221009d109b65e2fbfc0ae42ba0b2e5f03670cd458cff4882df6783f3d93d607d1755"
    )


def test_entropy_changes_the_signature_and_it_still_verifies():
    digest = hashlib.sha256(b"sample").digest()
    plain = _ecdsa_sign(_RFC6979_PRIVATE_KEY, digest, b"")
    hedged = _ecdsa_sign(_RFC6979_PRIVATE_KEY, digest, b"\x01" * 32)
    assert hedged != plain
    assert _verifies(_RFC6979_PUBLIC_KEY, hedged, b"sample")


def test_signatures_of_many_keys_verify():
    rng = random.Random(3)
    keys = [1, _P256_ORDER - 1]
    keys += [rng.randrange(1, _P256_ORDER) for _ in range(6)]
    for key in keys:
        message = rng.randbytes(rng.randrange(64))
        signature = _ecdsa_sign(
            key, hashlib.sha256(message).digest(), rng.randbytes(32)
        )
        assert _verifies(_multiply_generator(key), signature, message), hex(key)


def test_verifier_rejects_what_was_not_signed():
    signature = _ecdsa_sign(
        _RFC6979_PRIVATE_KEY, hashlib.sha256(b"sample").digest(), b""
    )
    assert not _verifies(_RFC6979_PUBLIC_KEY, signature, b"test")
    assert not _verifies(_PUBLIC_KEY, signature, b"sample")


@pytest.mark.parametrize(
    ("value", "encoded"),
    [
        (1, "020101"),
        (0x7F, "02017f"),
        (0x80, "02020080"),
        (0xFF, "020200ff"),
        (0x100, "02020100"),
        (0x7FFF, "02027fff"),
        (0x8000, "0203008000"),
        (2**255 - 1, "02207f" + "ff" * 31),
        (2**255, "02210080" + "00" * 31),
    ],
)
def test_der_integer_is_minimal_and_positive(value: int, encoded: str):
    assert _der_integer(value).hex() == encoded


# ---------------------------------------------------------------------------
# Key derivation
# ---------------------------------------------------------------------------


def test_derived_key_matches_test_suite_public_key():
    key = _derive_signing_key(_ACCESS_KEY, _SECRET_KEY)
    assert _multiply_generator(key) == _PUBLIC_KEY


# ---------------------------------------------------------------------------
# End-to-end signing — aws-c-auth v4a vectors
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("method", "canonical_request_hash", "suite_signature"),
    [
        (
            "GET",
            "cf59db423e841c8b7e3444158185aa261b724a5c27cbe762676f3eed19f4dc02",
            "3045022018b4e277d0281864beb51d3600e23f88510ea5031d68ddfbb68614b82a5eb7d2"
            "022100effb9c5f22ed9ef3ae0ab243d21f06bce82365bbb79529a07b6888c343ae5f8c",
        ),
        (
            "POST",
            "806a9b01b76472cc6b66fff02630726d55f8b4ada6d2fd9b36eb0d710e215861",
            "3044022051fe398025aafbfc21d054bc78e5edfb96c9acb7fd272795565181d757815e47"
            "02202e7b8d2b92324290b1d95f8b0fc5e333bb8b5e333f6160bcab39d7258156d224",
        ),
    ],
    ids=["get-vanilla", "post-vanilla"],
)
@pytest.mark.usefixtures("ecdsa")
def test_vanilla(method: str, canonical_request_hash: str, suite_signature: str):
    """v4a/get-vanilla and v4a/post-vanilla."""
    string_to_sign = (
        "AWS4-ECDSA-P256-SHA256\n"
        "20150830T123600Z\n"
        "20150830/service/aws4_request\n"
        f"{canonical_request_hash}"
    ).encode()
    # The suite's own signature verifies, so the vector is transcribed right
    # and the verifier agrees with the implementation that made it.
    assert _verifies(_PUBLIC_KEY, bytes.fromhex(suite_signature), string_to_sign)

    req = _make_request(
        method,
        "https://example.amazonaws.com/",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4a(req, _TEST_SUITE_CTX)

    assert signed.headers["X-Amz-Region-Set"] == "us-east-1"
    assert signed.headers["Authorization"].startswith(
        "AWS4-ECDSA-P256-SHA256 "
        "Credential=AKIDEXAMPLE/20150830/service/aws4_request,"
        "SignedHeaders=host;x-amz-date;x-amz-region-set,"
        "Signature="
    )
    assert _verifies(_PUBLIC_KEY, _signature(signed), string_to_sign)


# ---------------------------------------------------------------------------
# Where ECDSA comes from
# ---------------------------------------------------------------------------


def test_cryptography_signs_when_it_is_installed(monkeypatch: pytest.MonkeyPatch):
    pytest.importorskip("cryptography")

    def python_signer(private_key: int, digest: bytes, entropy: bytes) -> bytes:
        raise AssertionError("the Python implementation signed")

    monkeypatch.setattr(_sigv4a, "_ecdsa_sign", python_signer)
    req = _make_request("GET", "https://example.amazonaws.com/", {})
    assert _signature(sign_sigv4a(req, _TEST_SUITE_CTX))


def test_python_signs_when_cryptography_is_not_installed(
    monkeypatch: pytest.MonkeyPatch,
):
    """A second copy of the module, imported where ``cryptography`` cannot be."""
    spec = importlib.util.spec_from_file_location(
        "sigv4a_without_cryptography", _sigv4a.__file__
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    with monkeypatch.context() as patch:
        # None in sys.modules makes the import raise ImportError
        patch.setitem(sys.modules, "cryptography", None)
        for name in list(sys.modules):
            if name.startswith("cryptography."):
                patch.setitem(sys.modules, name, None)
        spec.loader.exec_module(module)
    assert module.ec is None

    entropy_sizes: list[int] = []

    def python_signer(private_key: int, digest: bytes, entropy: bytes) -> bytes:
        entropy_sizes.append(len(entropy))
        return _ecdsa_sign(private_key, digest, entropy)

    monkeypatch.setattr(module, "_ecdsa_sign", python_signer)
    req = _make_request("GET", "https://example.amazonaws.com/", {})
    assert _signature(module.sign_sigv4a(req, _TEST_SUITE_CTX))
    # one signature, with 32 fresh random bytes in its nonce
    assert entropy_sizes == [32]


def test_python_and_cryptography_agree():
    """Each implementation accepts what the other one signs."""
    pytest.importorskip("cryptography")
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import ec

    rng = random.Random(5)
    private_keys = [1, _P256_ORDER - 1]
    private_keys += [rng.randrange(1, _P256_ORDER) for _ in range(8)]
    for private_key in private_keys:
        key = ec.derive_private_key(private_key, ec.SECP256R1())
        public = key.public_key().public_numbers()
        assert _multiply_generator(private_key) == (public.x, public.y)

        message = rng.randbytes(rng.randrange(64))
        ours = _ecdsa_sign(
            private_key, hashlib.sha256(message).digest(), rng.randbytes(32)
        )
        # raises InvalidSignature unless OpenSSL accepts it
        key.public_key().verify(ours, message, ec.ECDSA(hashes.SHA256()))
        theirs = key.sign(message, ec.ECDSA(hashes.SHA256()))
        assert _verifies((public.x, public.y), theirs, message)


# ---------------------------------------------------------------------------
# Behavioral tests
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("ecdsa")
def test_signing_twice_gives_two_signatures():
    headers = {"X-Amz-Date": "20150830T123600Z"}
    first = sign_sigv4a(
        _make_request("GET", "https://example.amazonaws.com/", headers),
        _TEST_SUITE_CTX,
    )
    second = sign_sigv4a(
        _make_request("GET", "https://example.amazonaws.com/", headers),
        _TEST_SUITE_CTX,
    )
    assert _signature(first) != _signature(second)


def test_region_set_is_comma_joined():
    ctx: SigV4AAuthContext = {
        **_TEST_SUITE_CTX,
        "signing_region_set": ["us-east-1", "us-west-2"],
    }
    req = _make_request("GET", "https://example.amazonaws.com/", {})
    assert sign_sigv4a(req, ctx).headers["X-Amz-Region-Set"] == "us-east-1,us-west-2"


def test_session_token_added_and_signed():
    ctx: SigV4AAuthContext = {**_TEST_SUITE_CTX, "session_token": "TOKEN123"}
    req = _make_request("GET", "https://example.amazonaws.com/", {})
    signed = sign_sigv4a(req, ctx)
    assert signed.headers["X-Amz-Security-Token"] == "TOKEN123"
    assert "x-amz-security-token" in signed.headers["Authorization"]


def test_s3_sets_payload_hash_for_body():
    ctx: SigV4AAuthContext = {**_TEST_SUITE_CTX, "signing_name": "s3"}
    req = _make_request("PUT", "https://example.amazonaws.com/key", {}, body=b"hello")
    signed = sign_sigv4a(req, ctx)
    assert signed.headers["X-Amz-Content-SHA256"] == (
        "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )
    assert "x-amz-content-sha256" in signed.headers["Authorization"]
    assert signed.body == b"hello"


def test_streamed_body_rejected_without_unsigned_payload():
    req = _make_request(
        "PUT", "https://example.amazonaws.com/", {}, body=iter([b"chunk"])
    )
    with pytest.raises(TypeError):
        sign_sigv4a(req, _TEST_SUITE_CTX)


@pytest.mark.usefixtures("ecdsa")
def test_signer_sends_streamed_s3_body_unsigned():
    signer = SigV4ASigner(_PROVIDER, auth_scheme=_MRAP_SCHEME)
    body = iter([b"chunk"])
    req = _make_request("PUT", "https://example.amazonaws.com/key", {}, body=body)
    signed = signer.sign(req)
    assert signed.headers["X-Amz-Content-SHA256"] == "UNSIGNED-PAYLOAD"
    assert signed.headers["X-Amz-Region-Set"] == "*"
    assert signed.body is body


def test_signer_unsigned_payload_leaves_bytes_body_out_of_the_signature():
    signer = SigV4ASigner(_PROVIDER, auth_scheme=_MRAP_SCHEME, unsigned_payload=True)
    req = _make_request("PUT", "https://example.amazonaws.com/key", {}, body=b"hello")
    signed = signer.sign(req)
    assert signed.headers["X-Amz-Content-SHA256"] == "UNSIGNED-PAYLOAD"
    assert signed.body == b"hello"


@pytest.mark.usefixtures("ecdsa")
def test_signer_async_matches_sync_headers():
    signer = SigV4ASigner(_PROVIDER, auth_scheme=_MRAP_SCHEME)
    headers = {"X-Amz-Date": "20150830T123600Z"}
    sync = signer.sign(_make_request("GET", "https://example.amazonaws.com/", headers))
    signed = asyncio.run(
        signer.asign(_make_request("GET", "https://example.amazonaws.com/", headers))
    )
    # Signatures differ (each carries fresh randomness); everything before them matches.
    assert (
        signed.headers["Authorization"].split("Signature=")[0]
        == sync.headers["Authorization"].split("Signature=")[0]
    )


# ---------------------------------------------------------------------------
# Auth scheme selection
# ---------------------------------------------------------------------------


def test_scheme_is_the_endpoint_sigv4a_entry():
    assert build_sigv4a_auth_scheme("s3", [_MRAP_SCHEME]) == _MRAP_SCHEME
    assert build_sigv4a_auth_scheme("s3", [_SIGV4_SCHEME, _MRAP_SCHEME]) == _MRAP_SCHEME


def test_scheme_none_when_endpoint_does_not_offer_sigv4a():
    assert build_sigv4a_auth_scheme("s3", None) is None
    assert build_sigv4a_auth_scheme("s3", [_SIGV4_SCHEME]) is None


def test_scheme_signing_name_defaults_to_the_service():
    scheme = build_sigv4a_auth_scheme(
        "s3", [{"name": "sigv4a", "signingRegionSet": ["*"]}]
    )
    assert scheme == {"name": "sigv4a", "signingName": "s3", "signingRegionSet": ["*"]}
