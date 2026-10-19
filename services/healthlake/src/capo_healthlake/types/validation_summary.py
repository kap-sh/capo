"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#ValidationSummary``."""

from typing_extensions import TypedDict


class ValidationSummary(TypedDict, closed=True):
    error_count: "int"
    """<p>The number of validation errors found.</p>"""
    warning_count: "int"
    """<p>The number of validation warnings found.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationSummary) -> dict:
    out: dict = {}
    out["ErrorCount"] = value["error_count"]
    out["WarningCount"] = value["warning_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationSummary:
    out: ValidationSummary = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCount") is not None:
        out["error_count"] = data["ErrorCount"]
    else:
        out["error_count"] = 0
    if data.get("WarningCount") is not None:
        out["warning_count"] = data["WarningCount"]
    else:
        out["warning_count"] = 0
    return out
