"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ValidationExceptionDetail``."""

from typing_extensions import TypedDict


class ValidationExceptionDetail(TypedDict, closed=True):
    field_name: "str"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "str"
    """<p>A message with the reason for the validation exception error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionDetail) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionDetail:
    out: ValidationExceptionDetail = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    else:
        out["field_name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
