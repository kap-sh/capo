"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyMacInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.integer_range_between4_and32
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.mac_attributes
    import capo_payment_cryptography_data.types.mac_type
    import capo_payment_cryptography_data.types.message_data_type


class VerifyMacInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses to verify MAC data.</p>"""
    message_data: (
        "capo_payment_cryptography_data.types.message_data_type.MessageDataType"
    )
    """<p>The data on for which MAC is under verification. This value must be hexBinary.</p>"""
    mac: "capo_payment_cryptography_data.types.mac_type.MacType"
    """<p>The MAC being verified.</p>"""
    verification_attributes: (
        "capo_payment_cryptography_data.types.mac_attributes.MacAttributes"
    )
    """<p>The attributes and data values to use for MAC verification within Amazon Web Services Payment Cryptography.</p>"""
    mac_length: NotRequired[
        "capo_payment_cryptography_data.types.integer_range_between4_and32.IntegerRangeBetween4And32"
    ]
    """<p>The length of the MAC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyMacInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["MessageData"] = value["message_data"]
    out["Mac"] = value["mac"]
    import capo_payment_cryptography_data.types.mac_attributes

    out["VerificationAttributes"] = (
        capo_payment_cryptography_data.types.mac_attributes.serialize_json(
            value["verification_attributes"]
        )
    )
    if "mac_length" in value:
        out["MacLength"] = value["mac_length"]
    return out


def deserialize_json(data: dict) -> VerifyMacInput:
    out: VerifyMacInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError("VerifyMacInput.key_identifier required")
    if data.get("MessageData") is not None:
        out["message_data"] = data["MessageData"]
    else:
        raise DeserializationError("VerifyMacInput.message_data required")
    if data.get("Mac") is not None:
        out["mac"] = data["Mac"]
    else:
        raise DeserializationError("VerifyMacInput.mac required")
    if data.get("VerificationAttributes") is not None:
        import capo_payment_cryptography_data.types.mac_attributes

        out["verification_attributes"] = (
            capo_payment_cryptography_data.types.mac_attributes.deserialize_json(
                data["VerificationAttributes"]
            )
        )
    else:
        raise DeserializationError("VerifyMacInput.verification_attributes required")
    if data.get("MacLength") is not None:
        out["mac_length"] = data["MacLength"]
    return out


def redact_sensitive(value: VerifyMacInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message_data" in value:
        out["message_data"] = "*** Sensitive Data Redacted ***"
    if "mac" in value:
        out["mac"] = "*** Sensitive Data Redacted ***"
    if "verification_attributes" in value:
        import capo_payment_cryptography_data.types.mac_attributes

        out["verification_attributes"] = (
            capo_payment_cryptography_data.types.mac_attributes.redact_sensitive(
                value["verification_attributes"]
            )
        )
    return out
