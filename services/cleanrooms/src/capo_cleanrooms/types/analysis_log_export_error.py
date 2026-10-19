"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExportError``."""

from typing_extensions import TypedDict


class AnalysisLogExportError(TypedDict, closed=True):
    code: "str"
    """<p>The error code for the analysis log export.</p>"""
    message: "str"
    """<p>The message for the analysis log export error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExportError) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AnalysisLogExportError:
    out: AnalysisLogExportError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
