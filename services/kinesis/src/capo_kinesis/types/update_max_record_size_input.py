"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateMaxRecordSizeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.max_record_size_in_ki_b
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id


class UpdateMaxRecordSizeInput(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The Amazon Resource Name (ARN) of the stream for the <code>MaxRecordSize</code> update.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    max_record_size_in_ki_b: (
        "capo_kinesis.types.max_record_size_in_ki_b.MaxRecordSizeInKiB"
    )
    """<p>The maximum record size of a single record in KiB that you can write to, and read from a stream. Specify a value between 1024 and 10240 KiB (1 to 10 MiB). If you specify a value that is out of this range, <code>UpdateMaxRecordSize</code> sends back an <code>ValidationException</code> message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaxRecordSizeInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    out["MaxRecordSizeInKiB"] = value["max_record_size_in_ki_b"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaxRecordSizeInput:
    out: UpdateMaxRecordSizeInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("MaxRecordSizeInKiB") is not None:
        out["max_record_size_in_ki_b"] = data["MaxRecordSizeInKiB"]
    else:
        out["max_record_size_in_ki_b"] = 0
    return out
