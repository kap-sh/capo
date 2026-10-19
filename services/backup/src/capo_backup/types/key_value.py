"""Generated from Smithy shape ``com.amazonaws.backup#KeyValue``."""

from typing_extensions import TypedDict


class KeyValue(TypedDict, closed=True):
    key: "str"
    r"""<p>The tag key (String). The key can't start with <code>aws:</code>.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 128.</p> <p>Pattern: <code>^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$</code> </p>"""
    value: "str"
    r"""<p>The value of the key.</p> <p>Length Constraints: Maximum length of 256.</p> <p>Pattern: <code>^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyValue) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KeyValue:
    out: KeyValue = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
