"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateAs2805KekValidationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.as2805_random_key_material
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value


class GenerateAs2805KekValidationOutput(TypedDict, closed=True):
    key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of sending KEK that Amazon Web Services Payment Cryptography validates for node-to-node initialization</p>"""
    key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the sending KEK that Amazon Web Services Payment Cryptography validates for node-to-node initialization.</p>"""
    random_key_send: "capo_payment_cryptography_data.types.as2805_random_key_material.As2805RandomKeyMaterial"
    """<p>The random key generated for sending KEK validation.</p>"""
    random_key_receive: "capo_payment_cryptography_data.types.as2805_random_key_material.As2805RandomKeyMaterial"
    """<p>The random key generated for receiving KEK validation. The initiating node sends this key to its partner node for validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAs2805KekValidationOutput) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["RandomKeySend"] = value["random_key_send"]
    out["RandomKeyReceive"] = value["random_key_receive"]
    return out


def deserialize_json(data: dict) -> GenerateAs2805KekValidationOutput:
    out: GenerateAs2805KekValidationOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        out["key_arn"] = ""
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        out["key_check_value"] = ""
    if data.get("RandomKeySend") is not None:
        out["random_key_send"] = data["RandomKeySend"]
    else:
        out["random_key_send"] = ""
    if data.get("RandomKeyReceive") is not None:
        out["random_key_receive"] = data["RandomKeyReceive"]
    else:
        out["random_key_receive"] = ""
    return out


def redact_sensitive(value: GenerateAs2805KekValidationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "random_key_send" in value:
        out["random_key_send"] = "*** Sensitive Data Redacted ***"
    if "random_key_receive" in value:
        out["random_key_receive"] = "*** Sensitive Data Redacted ***"
    return out
