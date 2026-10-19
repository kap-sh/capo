"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.put_response_record_id


class PutRecordOutput(TypedDict, closed=True):
    record_id: "capo_firehose.types.put_response_record_id.PutResponseRecordId"
    """<p>The ID of the record.</p>"""
    encrypted: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Indicates whether server-side encryption (SSE) was enabled during this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordOutput) -> dict:
    out: dict = {}
    out["RecordId"] = value["record_id"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordOutput:
    out: PutRecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    else:
        out["record_id"] = ""
    if data.get("Encrypted") is not None:
        out["encrypted"] = data["Encrypted"]
    return out
