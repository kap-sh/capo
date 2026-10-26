"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionDataValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string


class _RuntimeSessionDataValue_stringValue(TypedDict, closed=True):
    stringValue: (
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    )


RuntimeSessionDataValue: TypeAlias = (
    _RuntimeSessionDataValue_stringValue | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionDataValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuntimeSessionDataValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    else:
        raise SerializationError("RuntimeSessionDataValue: no variant present")


def deserialize_json(data: dict) -> RuntimeSessionDataValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuntimeSessionDataValue: no recognized variant key")


def redact_sensitive(value: RuntimeSessionDataValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stringValue" in value:
        out["stringValue"] = "*** Sensitive Data Redacted ***"
    return out
