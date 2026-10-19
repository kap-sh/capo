"""Generated from Smithy shape ``com.amazonaws.pcs#ValidationExceptionField``."""

from typing_extensions import TypedDict


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the exception.</p>"""
    message: "str"
    """<p>The message body of the exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
