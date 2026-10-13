"""Generated from Smithy shape ``com.amazonaws.iot#KeyPair``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.private_key
    import capo_iot.types.public_key


class KeyPair(TypedDict, closed=True):
    public_key: NotRequired["capo_iot.types.public_key.PublicKey"]
    """<p>The public key.</p>"""
    private_key: NotRequired["capo_iot.types.private_key.PrivateKey"]
    """<p>The private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPair) -> dict:
    out: dict = {}
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    if "private_key" in value:
        out["PrivateKey"] = value["private_key"]
    return out


def deserialize_json(data: dict) -> KeyPair:
    out: KeyPair = {}  # type: ignore[typeddict-item]
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    if data.get("PrivateKey") is not None:
        out["private_key"] = data["PrivateKey"]
    return out


def redact_sensitive(value: KeyPair) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_key" in value:
        out["private_key"] = "*** Sensitive Data Redacted ***"
    return out
