"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionDataValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string


class _RuntimeSessionDataValue_stringValue(TypedDict, closed=True):
    stringValue: (
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    )


RuntimeSessionDataValue: TypeAlias = _RuntimeSessionDataValue_stringValue


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionDataValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    else:
        raise SerializationError("RuntimeSessionDataValue: no variant present")


def deserialize_json(data: dict) -> RuntimeSessionDataValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    else:
        raise DeserializationError("RuntimeSessionDataValue: no recognized variant key")


def redact_sensitive(value: RuntimeSessionDataValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stringValue" in value:
        out["stringValue"] = "*** Sensitive Data Redacted ***"
    return out
