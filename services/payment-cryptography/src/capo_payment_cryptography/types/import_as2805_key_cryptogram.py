"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportAs2805KeyCryptogram``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.as2805_key_variant
    import capo_payment_cryptography.types.key_algorithm
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.key_modes_of_use
    import capo_payment_cryptography.types.wrapped_key_cryptogram


class ImportAs2805KeyCryptogram(TypedDict, closed=True):
    as2805_key_variant: (
        "capo_payment_cryptography.types.as2805_key_variant.As2805KeyVariant"
    )
    """<p>The cryptographic usage of the key under import.</p>"""
    key_modes_of_use: "capo_payment_cryptography.types.key_modes_of_use.KeyModesOfUse"
    key_algorithm: "capo_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    """<p>The key algorithm of the key under import.</p>"""
    exportable: "bool"
    """<p>Specified whether the key is exportable. This data is immutable after the key is imported.</p>"""
    wrapping_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    wrapped_key_cryptogram: (
        "capo_payment_cryptography.types.wrapped_key_cryptogram.WrappedKeyCryptogram"
    )
    """<p>The wrapped key cryptogram under import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportAs2805KeyCryptogram) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.as2805_key_variant

    out["As2805KeyVariant"] = (
        capo_payment_cryptography.types.as2805_key_variant.serialize_aws_json_1_0(
            value["as2805_key_variant"]
        )
    )
    import capo_payment_cryptography.types.key_modes_of_use

    out["KeyModesOfUse"] = (
        capo_payment_cryptography.types.key_modes_of_use.serialize_aws_json_1_0(
            value["key_modes_of_use"]
        )
    )
    out["KeyAlgorithm"] = value["key_algorithm"]
    out["Exportable"] = value["exportable"]
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    out["WrappedKeyCryptogram"] = value["wrapped_key_cryptogram"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportAs2805KeyCryptogram:
    out: ImportAs2805KeyCryptogram = {}  # type: ignore[typeddict-item]
    if data.get("As2805KeyVariant") is not None:
        import capo_payment_cryptography.types.as2805_key_variant

        out["as2805_key_variant"] = (
            capo_payment_cryptography.types.as2805_key_variant.deserialize_aws_json_1_0(
                data["As2805KeyVariant"]
            )
        )
    else:
        raise DeserializationError(
            "ImportAs2805KeyCryptogram.as2805_key_variant required"
        )
    if data.get("KeyModesOfUse") is not None:
        import capo_payment_cryptography.types.key_modes_of_use

        out["key_modes_of_use"] = (
            capo_payment_cryptography.types.key_modes_of_use.deserialize_aws_json_1_0(
                data["KeyModesOfUse"]
            )
        )
    else:
        raise DeserializationError(
            "ImportAs2805KeyCryptogram.key_modes_of_use required"
        )
    if data.get("KeyAlgorithm") is not None:
        out["key_algorithm"] = data["KeyAlgorithm"]
    else:
        raise DeserializationError("ImportAs2805KeyCryptogram.key_algorithm required")
    if data.get("Exportable") is not None:
        out["exportable"] = data["Exportable"]
    else:
        raise DeserializationError("ImportAs2805KeyCryptogram.exportable required")
    if data.get("WrappingKeyIdentifier") is not None:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        raise DeserializationError(
            "ImportAs2805KeyCryptogram.wrapping_key_identifier required"
        )
    if data.get("WrappedKeyCryptogram") is not None:
        out["wrapped_key_cryptogram"] = data["WrappedKeyCryptogram"]
    else:
        raise DeserializationError(
            "ImportAs2805KeyCryptogram.wrapped_key_cryptogram required"
        )
    return out


def redact_sensitive(value: ImportAs2805KeyCryptogram) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_cryptogram" in value:
        out["wrapped_key_cryptogram"] = "*** Sensitive Data Redacted ***"
    return out
