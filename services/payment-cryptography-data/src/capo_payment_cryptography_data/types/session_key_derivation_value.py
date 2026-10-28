"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyDerivationValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.application_cryptogram_type
    import capo_payment_cryptography_data.types.hex_length_equals4


class SessionKeyDerivationValueApplicationCryptogramMember(TypedDict, closed=True):
    ApplicationCryptogram: "capo_payment_cryptography_data.types.application_cryptogram_type.ApplicationCryptogramType"


class SessionKeyDerivationValueApplicationTransactionCounterMember(
    TypedDict, closed=True
):
    ApplicationTransactionCounter: (
        "capo_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )


SessionKeyDerivationValue: TypeAlias = (
    SessionKeyDerivationValueApplicationCryptogramMember
    | SessionKeyDerivationValueApplicationTransactionCounterMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyDerivationValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SessionKeyDerivationValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ApplicationCryptogram" in value:
        return {"ApplicationCryptogram": value["ApplicationCryptogram"]}
    elif "ApplicationTransactionCounter" in value:
        return {"ApplicationTransactionCounter": value["ApplicationTransactionCounter"]}
    else:
        raise SerializationError("SessionKeyDerivationValue: no variant present")


def deserialize_json(data: dict) -> SessionKeyDerivationValue:
    if data.get("ApplicationCryptogram") is not None:
        return {"ApplicationCryptogram": data["ApplicationCryptogram"]}
    elif data.get("ApplicationTransactionCounter") is not None:
        return {"ApplicationTransactionCounter": data["ApplicationTransactionCounter"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SessionKeyDerivationValue: no recognized variant key"
        )


def redact_sensitive(value: SessionKeyDerivationValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ApplicationCryptogram" in value:
        out["ApplicationCryptogram"] = "*** Sensitive Data Redacted ***"
    return out
