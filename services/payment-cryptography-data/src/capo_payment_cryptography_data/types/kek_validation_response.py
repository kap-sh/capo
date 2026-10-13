"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#KekValidationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.as2805_random_key_material


class KekValidationResponse(TypedDict, closed=True):
    random_key_send: "capo_payment_cryptography_data.types.as2805_random_key_material.As2805RandomKeyMaterial"
    """<p>The random key send value received from the initiating node to generate a KEK validation response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KekValidationResponse) -> dict:
    out: dict = {}
    out["RandomKeySend"] = value["random_key_send"]
    return out


def deserialize_json(data: dict) -> KekValidationResponse:
    out: KekValidationResponse = {}  # type: ignore[typeddict-item]
    if data.get("RandomKeySend") is not None:
        out["random_key_send"] = data["RandomKeySend"]
    else:
        raise DeserializationError("KekValidationResponse.random_key_send required")
    return out


def redact_sensitive(value: KekValidationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "random_key_send" in value:
        out["random_key_send"] = "*** Sensitive Data Redacted ***"
    return out
