"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.put_record_batch_request_entry_list


class PutRecordBatchInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    records: "capo_firehose.types.put_record_batch_request_entry_list.PutRecordBatchRequestEntryList"
    """<p>One or more records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordBatchInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import capo_firehose.types.put_record_batch_request_entry_list

    out["Records"] = (
        capo_firehose.types.put_record_batch_request_entry_list.serialize_aws_json_1_1(
            value["records"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordBatchInput:
    out: PutRecordBatchInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("Records") is not None:
        import capo_firehose.types.put_record_batch_request_entry_list

        out["records"] = (
            capo_firehose.types.put_record_batch_request_entry_list.deserialize_aws_json_1_1(
                data["Records"]
            )
        )
    else:
        out["records"] = []
    return out
