"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDescribeUserLimitsError``."""

from typing_extensions import NotRequired, TypedDict


class BatchDescribeUserLimitsError(TypedDict, closed=True):
    user_name: NotRequired["str"]
    """<p>The name of the user that failed.</p>"""
    namespace: NotRequired["str"]
    """<p>The namespace of the user that failed.</p>"""
    user_arn: NotRequired["str"]
    """<p>The ARN of the user that failed.</p>"""
    error_code: "str"
    """<p>The error code for the failure.</p>"""
    message: "str"
    """<p>The error message for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeUserLimitsError) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    out["errorCode"] = value["error_code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDescribeUserLimitsError:
    out: BatchDescribeUserLimitsError = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("userArn") is not None:
        out["user_arn"] = data["userArn"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
