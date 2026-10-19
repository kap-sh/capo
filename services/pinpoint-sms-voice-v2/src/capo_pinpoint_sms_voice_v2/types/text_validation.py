"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TextValidation``."""

from typing_extensions import TypedDict


class TextValidation(TypedDict, closed=True):
    min_length: "int"
    """<p>The minimum number of characters for the text field.</p>"""
    max_length: "int"
    """<p>The maximum number of characters for the text field.</p>"""
    pattern: "str"
    """<p>The regular expression used to validate the text field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TextValidation) -> dict:
    out: dict = {}
    out["MinLength"] = value["min_length"]
    out["MaxLength"] = value["max_length"]
    out["Pattern"] = value["pattern"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TextValidation:
    out: TextValidation = {}  # type: ignore[typeddict-item]
    if data.get("MinLength") is not None:
        out["min_length"] = data["MinLength"]
    else:
        out["min_length"] = 0
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    else:
        out["max_length"] = 0
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    else:
        out["pattern"] = ""
    return out
