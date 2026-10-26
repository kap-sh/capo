"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#ReEncryptionAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.asymmetric_encryption_attributes
    import capo_payment_cryptography_data.types.dukpt_encryption_attributes
    import capo_payment_cryptography_data.types.symmetric_encryption_attributes


class _ReEncryptionAttributes_Symmetric(TypedDict, closed=True):
    Symmetric: "capo_payment_cryptography_data.types.symmetric_encryption_attributes.SymmetricEncryptionAttributes"


class _ReEncryptionAttributes_Asymmetric(TypedDict, closed=True):
    Asymmetric: "capo_payment_cryptography_data.types.asymmetric_encryption_attributes.AsymmetricEncryptionAttributes"


class _ReEncryptionAttributes_Dukpt(TypedDict, closed=True):
    Dukpt: "capo_payment_cryptography_data.types.dukpt_encryption_attributes.DukptEncryptionAttributes"


ReEncryptionAttributes: TypeAlias = (
    _ReEncryptionAttributes_Symmetric
    | _ReEncryptionAttributes_Asymmetric
    | _ReEncryptionAttributes_Dukpt
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReEncryptionAttributes) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReEncryptionAttributes: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Symmetric" in value:
        import capo_payment_cryptography_data.types.symmetric_encryption_attributes

        return {
            "Symmetric": capo_payment_cryptography_data.types.symmetric_encryption_attributes.serialize_json(
                value["Symmetric"]
            )
        }
    elif "Asymmetric" in value:
        import capo_payment_cryptography_data.types.asymmetric_encryption_attributes

        return {
            "Asymmetric": capo_payment_cryptography_data.types.asymmetric_encryption_attributes.serialize_json(
                value["Asymmetric"]
            )
        }
    elif "Dukpt" in value:
        import capo_payment_cryptography_data.types.dukpt_encryption_attributes

        return {
            "Dukpt": capo_payment_cryptography_data.types.dukpt_encryption_attributes.serialize_json(
                value["Dukpt"]
            )
        }
    else:
        raise SerializationError("ReEncryptionAttributes: no variant present")


def deserialize_json(data: dict) -> ReEncryptionAttributes:
    if data.get("Symmetric") is not None:
        import capo_payment_cryptography_data.types.symmetric_encryption_attributes

        return {
            "Symmetric": capo_payment_cryptography_data.types.symmetric_encryption_attributes.deserialize_json(
                data["Symmetric"]
            )
        }
    elif data.get("Asymmetric") is not None:
        import capo_payment_cryptography_data.types.asymmetric_encryption_attributes

        return {
            "Asymmetric": capo_payment_cryptography_data.types.asymmetric_encryption_attributes.deserialize_json(
                data["Asymmetric"]
            )
        }
    elif data.get("Dukpt") is not None:
        import capo_payment_cryptography_data.types.dukpt_encryption_attributes

        return {
            "Dukpt": capo_payment_cryptography_data.types.dukpt_encryption_attributes.deserialize_json(
                data["Dukpt"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ReEncryptionAttributes: no recognized variant key")


def redact_sensitive(value: ReEncryptionAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Symmetric" in value:
        import capo_payment_cryptography_data.types.symmetric_encryption_attributes

        out["Symmetric"] = (
            capo_payment_cryptography_data.types.symmetric_encryption_attributes.redact_sensitive(
                value["Symmetric"]
            )
        )
    if "Dukpt" in value:
        import capo_payment_cryptography_data.types.dukpt_encryption_attributes

        out["Dukpt"] = (
            capo_payment_cryptography_data.types.dukpt_encryption_attributes.redact_sensitive(
                value["Dukpt"]
            )
        )
    return out
