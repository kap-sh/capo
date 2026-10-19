"""Generated from Smithy shape ``com.amazonaws.evs#ErrorDetail``."""

from typing_extensions import TypedDict


class ErrorDetail(TypedDict, closed=True):
    error_code: "str"
    """<p>The error code.</p>"""
    error_message: "str"
    """<p>The error message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorDetail) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
