"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyDerivation``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.session_key_amex
    import capo_payment_cryptography_data.types.session_key_emv2000
    import capo_payment_cryptography_data.types.session_key_emv_common
    import capo_payment_cryptography_data.types.session_key_mastercard
    import capo_payment_cryptography_data.types.session_key_union_pay
    import capo_payment_cryptography_data.types.session_key_visa


class _SessionKeyDerivation_EmvCommon(TypedDict, closed=True):
    EmvCommon: "capo_payment_cryptography_data.types.session_key_emv_common.SessionKeyEmvCommon"


class _SessionKeyDerivation_Mastercard(TypedDict, closed=True):
    Mastercard: "capo_payment_cryptography_data.types.session_key_mastercard.SessionKeyMastercard"


class _SessionKeyDerivation_Emv2000(TypedDict, closed=True):
    Emv2000: (
        "capo_payment_cryptography_data.types.session_key_emv2000.SessionKeyEmv2000"
    )


class _SessionKeyDerivation_Amex(TypedDict, closed=True):
    Amex: "capo_payment_cryptography_data.types.session_key_amex.SessionKeyAmex"


class _SessionKeyDerivation_Visa(TypedDict, closed=True):
    Visa: "capo_payment_cryptography_data.types.session_key_visa.SessionKeyVisa"


class _SessionKeyDerivation_UnionPay(TypedDict, closed=True):
    UnionPay: (
        "capo_payment_cryptography_data.types.session_key_union_pay.SessionKeyUnionPay"
    )


SessionKeyDerivation: TypeAlias = (
    _SessionKeyDerivation_EmvCommon
    | _SessionKeyDerivation_Mastercard
    | _SessionKeyDerivation_Emv2000
    | _SessionKeyDerivation_Amex
    | _SessionKeyDerivation_Visa
    | _SessionKeyDerivation_UnionPay
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyDerivation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SessionKeyDerivation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "EmvCommon" in value:
        import capo_payment_cryptography_data.types.session_key_emv_common

        return {
            "EmvCommon": capo_payment_cryptography_data.types.session_key_emv_common.serialize_json(
                value["EmvCommon"]
            )
        }
    elif "Mastercard" in value:
        import capo_payment_cryptography_data.types.session_key_mastercard

        return {
            "Mastercard": capo_payment_cryptography_data.types.session_key_mastercard.serialize_json(
                value["Mastercard"]
            )
        }
    elif "Emv2000" in value:
        import capo_payment_cryptography_data.types.session_key_emv2000

        return {
            "Emv2000": capo_payment_cryptography_data.types.session_key_emv2000.serialize_json(
                value["Emv2000"]
            )
        }
    elif "Amex" in value:
        import capo_payment_cryptography_data.types.session_key_amex

        return {
            "Amex": capo_payment_cryptography_data.types.session_key_amex.serialize_json(
                value["Amex"]
            )
        }
    elif "Visa" in value:
        import capo_payment_cryptography_data.types.session_key_visa

        return {
            "Visa": capo_payment_cryptography_data.types.session_key_visa.serialize_json(
                value["Visa"]
            )
        }
    elif "UnionPay" in value:
        import capo_payment_cryptography_data.types.session_key_union_pay

        return {
            "UnionPay": capo_payment_cryptography_data.types.session_key_union_pay.serialize_json(
                value["UnionPay"]
            )
        }
    else:
        raise SerializationError("SessionKeyDerivation: no variant present")


def deserialize_json(data: dict) -> SessionKeyDerivation:
    if data.get("EmvCommon") is not None:
        import capo_payment_cryptography_data.types.session_key_emv_common

        return {
            "EmvCommon": capo_payment_cryptography_data.types.session_key_emv_common.deserialize_json(
                data["EmvCommon"]
            )
        }
    elif data.get("Mastercard") is not None:
        import capo_payment_cryptography_data.types.session_key_mastercard

        return {
            "Mastercard": capo_payment_cryptography_data.types.session_key_mastercard.deserialize_json(
                data["Mastercard"]
            )
        }
    elif data.get("Emv2000") is not None:
        import capo_payment_cryptography_data.types.session_key_emv2000

        return {
            "Emv2000": capo_payment_cryptography_data.types.session_key_emv2000.deserialize_json(
                data["Emv2000"]
            )
        }
    elif data.get("Amex") is not None:
        import capo_payment_cryptography_data.types.session_key_amex

        return {
            "Amex": capo_payment_cryptography_data.types.session_key_amex.deserialize_json(
                data["Amex"]
            )
        }
    elif data.get("Visa") is not None:
        import capo_payment_cryptography_data.types.session_key_visa

        return {
            "Visa": capo_payment_cryptography_data.types.session_key_visa.deserialize_json(
                data["Visa"]
            )
        }
    elif data.get("UnionPay") is not None:
        import capo_payment_cryptography_data.types.session_key_union_pay

        return {
            "UnionPay": capo_payment_cryptography_data.types.session_key_union_pay.deserialize_json(
                data["UnionPay"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SessionKeyDerivation: no recognized variant key")


def redact_sensitive(value: SessionKeyDerivation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "EmvCommon" in value:
        import capo_payment_cryptography_data.types.session_key_emv_common

        out["EmvCommon"] = (
            capo_payment_cryptography_data.types.session_key_emv_common.redact_sensitive(
                value["EmvCommon"]
            )
        )
    if "Mastercard" in value:
        import capo_payment_cryptography_data.types.session_key_mastercard

        out["Mastercard"] = (
            capo_payment_cryptography_data.types.session_key_mastercard.redact_sensitive(
                value["Mastercard"]
            )
        )
    if "Emv2000" in value:
        import capo_payment_cryptography_data.types.session_key_emv2000

        out["Emv2000"] = (
            capo_payment_cryptography_data.types.session_key_emv2000.redact_sensitive(
                value["Emv2000"]
            )
        )
    if "Amex" in value:
        import capo_payment_cryptography_data.types.session_key_amex

        out["Amex"] = (
            capo_payment_cryptography_data.types.session_key_amex.redact_sensitive(
                value["Amex"]
            )
        )
    if "Visa" in value:
        import capo_payment_cryptography_data.types.session_key_visa

        out["Visa"] = (
            capo_payment_cryptography_data.types.session_key_visa.redact_sensitive(
                value["Visa"]
            )
        )
    if "UnionPay" in value:
        import capo_payment_cryptography_data.types.session_key_union_pay

        out["UnionPay"] = (
            capo_payment_cryptography_data.types.session_key_union_pay.redact_sensitive(
                value["UnionPay"]
            )
        )
    return out
