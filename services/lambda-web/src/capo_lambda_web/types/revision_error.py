"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionError``."""

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError


class RevisionError(TypedDict, closed=True):
    attribute: "str"
    """<p>The name of the revision attribute that the error applies to. Must be between 1 and 64 characters.</p>"""
    error_code: "str"
    """<p>A short, machine-readable code that identifies the error. Must be between 1 and 64 characters.</p>"""
    error_message: "str"
    """<p>A human-readable message describing the error. Must be between 1 and 2048 characters.</p>"""


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
        raise DeserializationError("RevisionError.attribute required")
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("RevisionError.error_code required")
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("RevisionError.error_message required")
    return out
