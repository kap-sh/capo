"""Generated from Smithy shape ``com.amazonaws.kinesis#SequenceNumberRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.sequence_number


class SequenceNumberRange(TypedDict, closed=True):
    starting_sequence_number: "capo_kinesis.types.sequence_number.SequenceNumber"
    """<p>The starting sequence number for the range.</p>"""
    ending_sequence_number: NotRequired[
        "capo_kinesis.types.sequence_number.SequenceNumber"
    ]
    """<p>The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SequenceNumberRange) -> dict:
    out: dict = {}
    out["StartingSequenceNumber"] = value["starting_sequence_number"]
    if "ending_sequence_number" in value:
        out["EndingSequenceNumber"] = value["ending_sequence_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SequenceNumberRange:
    out: SequenceNumberRange = {}  # type: ignore[typeddict-item]
    if data.get("StartingSequenceNumber") is not None:
        out["starting_sequence_number"] = data["StartingSequenceNumber"]
    else:
        out["starting_sequence_number"] = ""
    if data.get("EndingSequenceNumber") is not None:
        out["ending_sequence_number"] = data["EndingSequenceNumber"]
    return out
