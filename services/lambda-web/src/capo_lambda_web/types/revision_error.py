"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionError``."""

from typing_extensions import TypedDict


class RevisionError(TypedDict, closed=True):
    attribute: "str"
    """<p>The name of the revision attribute that the error applies to.</p>"""
    error_code: "str"
    """<p>A short, machine-readable code that identifies the error.</p>"""
    error_message: "str"
    """<p>A human-readable message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevisionError) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> RevisionError:
    out: RevisionError = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        out["attribute"] = data["attribute"]
    else:
        out["attribute"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
