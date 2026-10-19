"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ValidationExceptionField``."""

from typing_extensions import TypedDict


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>Name of the field that failed validation.</p>"""
    reason: "str"
    """<p>Reason for the validation failure.</p>"""
    message: "str"
    """<p>Detailed error message describing the validation issue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Reason"] = value["reason"]
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        out["reason"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
