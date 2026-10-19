"""Generated from Smithy shape ``com.amazonaws.entityresolution#FailedRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.error_message
    import capo_entityresolution.types.input_source_arn


class FailedRecord(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p> The input source ARN of the record that didn't generate a Match ID.</p>"""
    unique_id: "str"
    """<p> The unique ID of the record that didn't generate a Match ID.</p>"""
    error_message: "capo_entityresolution.types.error_message.ErrorMessage"
    """<p> The error message for the record that didn't generate a Match ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedRecord) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    out["uniqueId"] = value["unique_id"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedRecord:
    out: FailedRecord = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceARN") is not None:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        out["input_source_arn"] = ""
    if data.get("uniqueId") is not None:
        out["unique_id"] = data["uniqueId"]
    else:
        out["unique_id"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
