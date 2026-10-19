"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DerivationMethodAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.amex_attributes
    import capo_payment_cryptography_data.types.emv2000_attributes
    import capo_payment_cryptography_data.types.emv_common_attributes
    import capo_payment_cryptography_data.types.master_card_attributes
    import capo_payment_cryptography_data.types.visa_attributes


class _DerivationMethodAttributes_EmvCommon(TypedDict, closed=True):
    EmvCommon: (
        "capo_payment_cryptography_data.types.emv_common_attributes.EmvCommonAttributes"
    )


class _DerivationMethodAttributes_Amex(TypedDict, closed=True):
    Amex: "capo_payment_cryptography_data.types.amex_attributes.AmexAttributes"


class _DerivationMethodAttributes_Visa(TypedDict, closed=True):
    Visa: "capo_payment_cryptography_data.types.visa_attributes.VisaAttributes"


class _DerivationMethodAttributes_Emv2000(TypedDict, closed=True):
    Emv2000: "capo_payment_cryptography_data.types.emv2000_attributes.Emv2000Attributes"


class _DerivationMethodAttributes_Mastercard(TypedDict, closed=True):
    Mastercard: "capo_payment_cryptography_data.types.master_card_attributes.MasterCardAttributes"


DerivationMethodAttributes: TypeAlias = (
    _DerivationMethodAttributes_EmvCommon
    | _DerivationMethodAttributes_Amex
    | _DerivationMethodAttributes_Visa
    | _DerivationMethodAttributes_Emv2000
    | _DerivationMethodAttributes_Mastercard
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DerivationMethodAttributes) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DerivationMethodAttributes: cannot serialize unknown variant {value.name!r}"
        )
    elif "EmvCommon" in value:
        import capo_payment_cryptography_data.types.emv_common_attributes

        return {
            "EmvCommon": capo_payment_cryptography_data.types.emv_common_attributes.serialize_json(
                value["EmvCommon"]
            )
        }
    elif "Amex" in value:
        import capo_payment_cryptography_data.types.amex_attributes

        return {
            "Amex": capo_payment_cryptography_data.types.amex_attributes.serialize_json(
                value["Amex"]
            )
        }
    elif "Visa" in value:
        import capo_payment_cryptography_data.types.visa_attributes

        return {
            "Visa": capo_payment_cryptography_data.types.visa_attributes.serialize_json(
                value["Visa"]
            )
        }
    elif "Emv2000" in value:
        import capo_payment_cryptography_data.types.emv2000_attributes

        return {
            "Emv2000": capo_payment_cryptography_data.types.emv2000_attributes.serialize_json(
                value["Emv2000"]
            )
        }
    elif "Mastercard" in value:
        import capo_payment_cryptography_data.types.master_card_attributes

        return {
            "Mastercard": capo_payment_cryptography_data.types.master_card_attributes.serialize_json(
                value["Mastercard"]
            )
        }
    else:
        raise SerializationError("DerivationMethodAttributes: no variant present")


def deserialize_json(data: dict) -> DerivationMethodAttributes:
    if data.get("EmvCommon") is not None:
        import capo_payment_cryptography_data.types.emv_common_attributes

        return {
            "EmvCommon": capo_payment_cryptography_data.types.emv_common_attributes.deserialize_json(
                data["EmvCommon"]
            )
        }
    elif data.get("Amex") is not None:
        import capo_payment_cryptography_data.types.amex_attributes

        return {
            "Amex": capo_payment_cryptography_data.types.amex_attributes.deserialize_json(
                data["Amex"]
            )
        }
    elif data.get("Visa") is not None:
        import capo_payment_cryptography_data.types.visa_attributes

        return {
            "Visa": capo_payment_cryptography_data.types.visa_attributes.deserialize_json(
                data["Visa"]
            )
        }
    elif data.get("Emv2000") is not None:
        import capo_payment_cryptography_data.types.emv2000_attributes

        return {
            "Emv2000": capo_payment_cryptography_data.types.emv2000_attributes.deserialize_json(
                data["Emv2000"]
            )
        }
    elif data.get("Mastercard") is not None:
        import capo_payment_cryptography_data.types.master_card_attributes

        return {
            "Mastercard": capo_payment_cryptography_data.types.master_card_attributes.deserialize_json(
                data["Mastercard"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DerivationMethodAttributes: no recognized variant key"
        )


def redact_sensitive(
    value: DerivationMethodAttributes,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "EmvCommon" in value:
        import capo_payment_cryptography_data.types.emv_common_attributes

        out["EmvCommon"] = (
            capo_payment_cryptography_data.types.emv_common_attributes.redact_sensitive(
                value["EmvCommon"]
            )
        )
    if "Amex" in value:
        import capo_payment_cryptography_data.types.amex_attributes

        out["Amex"] = (
            capo_payment_cryptography_data.types.amex_attributes.redact_sensitive(
                value["Amex"]
            )
        )
    if "Visa" in value:
        import capo_payment_cryptography_data.types.visa_attributes

        out["Visa"] = (
            capo_payment_cryptography_data.types.visa_attributes.redact_sensitive(
                value["Visa"]
            )
        )
    if "Emv2000" in value:
        import capo_payment_cryptography_data.types.emv2000_attributes

        out["Emv2000"] = (
            capo_payment_cryptography_data.types.emv2000_attributes.redact_sensitive(
                value["Emv2000"]
            )
        )
    if "Mastercard" in value:
        import capo_payment_cryptography_data.types.master_card_attributes

        out["Mastercard"] = (
            capo_payment_cryptography_data.types.master_card_attributes.redact_sensitive(
                value["Mastercard"]
            )
        )
    return out
