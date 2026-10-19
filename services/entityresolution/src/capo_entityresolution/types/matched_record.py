"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchedRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.input_source_arn


class MatchedRecord(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p> The input source ARN of the matched record.</p>"""
    record_id: "str"
    """<p> The record ID of the matched record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchedRecord) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    out["recordId"] = value["record_id"]
    return out


def deserialize_json(data: dict) -> MatchedRecord:
    out: MatchedRecord = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceARN") is not None:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        out["input_source_arn"] = ""
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        out["record_id"] = ""
    return out
