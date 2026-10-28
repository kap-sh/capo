"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinData``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.pin_offset_type
    import capo_payment_cryptography_data.types.verification_value_type


class PinDataPinOffsetMember(TypedDict, closed=True):
    PinOffset: "capo_payment_cryptography_data.types.pin_offset_type.PinOffsetType"


class PinDataVerificationValueMember(TypedDict, closed=True):
    VerificationValue: "capo_payment_cryptography_data.types.verification_value_type.VerificationValueType"


PinData: TypeAlias = (
    PinDataPinOffsetMember | PinDataVerificationValueMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PinData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PinData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PinOffset" in value:
        return {"PinOffset": value["PinOffset"]}
    elif "VerificationValue" in value:
        return {"VerificationValue": value["VerificationValue"]}
    else:
        raise SerializationError("PinData: no variant present")


def deserialize_json(data: dict) -> PinData:
    if data.get("PinOffset") is not None:
        return {"PinOffset": data["PinOffset"]}
    elif data.get("VerificationValue") is not None:
        return {"VerificationValue": data["VerificationValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PinData: no recognized variant key")


def redact_sensitive(value: PinData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "PinOffset" in value:
        out["PinOffset"] = "*** Sensitive Data Redacted ***"
    if "VerificationValue" in value:
        out["VerificationValue"] = "*** Sensitive Data Redacted ***"
    return out
