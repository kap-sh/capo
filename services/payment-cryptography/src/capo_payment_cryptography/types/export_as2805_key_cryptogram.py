"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportAs2805KeyCryptogram``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.as2805_key_variant
    import capo_payment_cryptography.types.key_arn_or_key_alias_type


class ExportAs2805KeyCryptogram(TypedDict, closed=True):
    wrapping_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    as2805_key_variant: (
        "capo_payment_cryptography.types.as2805_key_variant.As2805KeyVariant"
    )
    """<p>The cryptographic usage of the key under export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportAs2805KeyCryptogram) -> dict:
    out: dict = {}
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    import capo_payment_cryptography.types.as2805_key_variant

    out["As2805KeyVariant"] = (
        capo_payment_cryptography.types.as2805_key_variant.serialize_aws_json_1_0(
            value["as2805_key_variant"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportAs2805KeyCryptogram:
    out: ExportAs2805KeyCryptogram = {}  # type: ignore[typeddict-item]
    if data.get("WrappingKeyIdentifier") is not None:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        out["wrapping_key_identifier"] = ""
    if data.get("As2805KeyVariant") is not None:
        import capo_payment_cryptography.types.as2805_key_variant

        out["as2805_key_variant"] = (
            capo_payment_cryptography.types.as2805_key_variant.deserialize_aws_json_1_0(
                data["As2805KeyVariant"]
            )
        )
    else:
        import typing

        out["as2805_key_variant"] = typing.cast(
            "capo_payment_cryptography.types.as2805_key_variant.As2805KeyVariant", ""
        )
    return out
