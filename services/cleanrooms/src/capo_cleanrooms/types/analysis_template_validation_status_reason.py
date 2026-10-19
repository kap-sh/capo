"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusReason``."""

from typing_extensions import TypedDict


class AnalysisTemplateValidationStatusReason(TypedDict, closed=True):
    message: "str"
    """<p>The validation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusReason) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AnalysisTemplateValidationStatusReason:
    out: AnalysisTemplateValidationStatusReason = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
