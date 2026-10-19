"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#OutgoingTr31KeyBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type


class OutgoingTr31KeyBlock(TypedDict, closed=True):
    wrapping_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the KEK used to wrap the transaction key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutgoingTr31KeyBlock) -> dict:
    out: dict = {}
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    return out


def deserialize_json(data: dict) -> OutgoingTr31KeyBlock:
    out: OutgoingTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("WrappingKeyIdentifier") is not None:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        out["wrapping_key_identifier"] = ""
    return out
