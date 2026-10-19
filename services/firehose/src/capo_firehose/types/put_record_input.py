"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.record


class PutRecordInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    record: "capo_firehose.types.record.Record"
    """<p>The record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import capo_firehose.types.record

    out["Record"] = capo_firehose.types.record.serialize_aws_json_1_1(value["record"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordInput:
    out: PutRecordInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("Record") is not None:
        import capo_firehose.types.record

        out["record"] = capo_firehose.types.record.deserialize_aws_json_1_1(
            data["Record"]
        )
    else:
        raise DeserializationError("PutRecordInput.record required")
    return out
