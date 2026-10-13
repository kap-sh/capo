"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SymmetricEncryptionAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.encryption_mode
    import capo_payment_cryptography_data.types.initialization_vector_type
    import capo_payment_cryptography_data.types.padding_type


class SymmetricEncryptionAttributes(TypedDict, closed=True):
    mode: "capo_payment_cryptography_data.types.encryption_mode.EncryptionMode"
    """<p>The block cipher method to use for encryption.</p>"""
    initialization_vector: NotRequired[
        "capo_payment_cryptography_data.types.initialization_vector_type.InitializationVectorType"
    ]
    """<p>An input used to provide the intial state. If no value is provided, Amazon Web Services Payment Cryptography defaults it to zero.</p>"""
    padding_type: NotRequired[
        "capo_payment_cryptography_data.types.padding_type.PaddingType"
    ]
    """<p>The padding to be included with the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SymmetricEncryptionAttributes) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.encryption_mode

    out["Mode"] = capo_payment_cryptography_data.types.encryption_mode.serialize_json(
        value["mode"]
    )
    if "initialization_vector" in value:
        out["InitializationVector"] = value["initialization_vector"]
    if "padding_type" in value:
        import capo_payment_cryptography_data.types.padding_type

        out["PaddingType"] = (
            capo_payment_cryptography_data.types.padding_type.serialize_json(
                value["padding_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SymmetricEncryptionAttributes:
    out: SymmetricEncryptionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_payment_cryptography_data.types.encryption_mode

        out["mode"] = (
            capo_payment_cryptography_data.types.encryption_mode.deserialize_json(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("SymmetricEncryptionAttributes.mode required")
    if data.get("InitializationVector") is not None:
        out["initialization_vector"] = data["InitializationVector"]
    if data.get("PaddingType") is not None:
        import capo_payment_cryptography_data.types.padding_type

        out["padding_type"] = (
            capo_payment_cryptography_data.types.padding_type.deserialize_json(
                data["PaddingType"]
            )
        )
    return out


def redact_sensitive(value: SymmetricEncryptionAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "initialization_vector" in value:
        out["initialization_vector"] = "*** Sensitive Data Redacted ***"
    return out
