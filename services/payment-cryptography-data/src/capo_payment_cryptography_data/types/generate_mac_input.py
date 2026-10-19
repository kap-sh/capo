"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateMacInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.integer_range_between4_and32
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.mac_attributes
    import capo_payment_cryptography_data.types.message_data_type


class GenerateMacInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the MAC generation encryption key.</p>"""
    message_data: (
        "capo_payment_cryptography_data.types.message_data_type.MessageDataType"
    )
    """<p>The data for which a MAC is under generation. This value must be hexBinary.</p>"""
    generation_attributes: (
        "capo_payment_cryptography_data.types.mac_attributes.MacAttributes"
    )
    """<p>The attributes and data values to use for MAC generation within Amazon Web Services Payment Cryptography.</p>"""
    mac_length: NotRequired[
        "capo_payment_cryptography_data.types.integer_range_between4_and32.IntegerRangeBetween4And32"
    ]
    """<p>The length of a MAC under generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMacInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["MessageData"] = value["message_data"]
    import capo_payment_cryptography_data.types.mac_attributes

    out["GenerationAttributes"] = (
        capo_payment_cryptography_data.types.mac_attributes.serialize_json(
            value["generation_attributes"]
        )
    )
    if "mac_length" in value:
        out["MacLength"] = value["mac_length"]
    return out


def deserialize_json(data: dict) -> GenerateMacInput:
    out: GenerateMacInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        out["key_identifier"] = ""
    if data.get("MessageData") is not None:
        out["message_data"] = data["MessageData"]
    else:
        out["message_data"] = ""
    if data.get("GenerationAttributes") is not None:
        import capo_payment_cryptography_data.types.mac_attributes

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types.mac_attributes.deserialize_json(
                data["GenerationAttributes"]
            )
        )
    else:
        import capo_payment_cryptography_data.types._unknown

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types._unknown.UnknownUnionMember("")
        )
    if data.get("MacLength") is not None:
        out["mac_length"] = data["MacLength"]
    return out


def redact_sensitive(value: GenerateMacInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message_data" in value:
        out["message_data"] = "*** Sensitive Data Redacted ***"
    if "generation_attributes" in value:
        import capo_payment_cryptography_data.types.mac_attributes

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types.mac_attributes.redact_sensitive(
                value["generation_attributes"]
            )
        )
    return out
