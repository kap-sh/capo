"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.approximate_arrival_timestamp
    import capo_kinesis.types.data
    import capo_kinesis.types.first_receive_timestamp
    import capo_kinesis.types.partition_key
    import capo_kinesis.types.receipt_handle
    import capo_kinesis.types.receive_count
    import capo_kinesis.types.record_id


class QueueRecord(TypedDict, closed=True):
    receipt_handle: "capo_kinesis.types.receipt_handle.ReceiptHandle"
    """<p>The identifier you use to acknowledge this record, change its visibility, or restore it after it becomes a dead-letter record. A new receipt handle is issued each time the record is received.</p>"""
    record_id: "capo_kinesis.types.record_id.RecordId"
    """<p>The unique identifier of the record. This value stays the same across every delivery of the record, and it is the same in every queue on the stream that delivers the record. To identify a single delivery, use <code>ReceiptHandle</code> instead.</p>"""
    partition_key: NotRequired["capo_kinesis.types.partition_key.PartitionKey"]
    """<p>The partition key the record was written to the data stream with.</p>"""
    data: "capo_kinesis.types.data.Data"
    """<p>The data blob of the record. Amazon Kinesis Data Streams does not inspect, interpret, or change the data.</p>"""
    approximate_arrival_timestamp: (
        "capo_kinesis.types.approximate_arrival_timestamp.ApproximateArrivalTimestamp"
    )
    """<p>The approximate time the record arrived in the data stream. The difference between this value and the current time is how long the record took to reach your queue consumer.</p>"""
    first_receive_timestamp: (
        "capo_kinesis.types.first_receive_timestamp.FirstReceiveTimestamp"
    )
    """<p>The approximate time the record was first received from the queue.</p>"""
    receive_count: "capo_kinesis.types.receive_count.ReceiveCount"
    """<p>The number of times this record has been received without being acknowledged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueRecord) -> dict:
    out: dict = {}
    out["ReceiptHandle"] = value["receipt_handle"]
    out["RecordId"] = value["record_id"]
    if "partition_key" in value:
        out["PartitionKey"] = value["partition_key"]
    import capo_kinesis.types.data

    out["Data"] = capo_kinesis.types.data.serialize_aws_json_1_1(value["data"])
    import capo_kinesis.types.approximate_arrival_timestamp

    out["ApproximateArrivalTimestamp"] = (
        capo_kinesis.types.approximate_arrival_timestamp.serialize_aws_json_1_1(
            value["approximate_arrival_timestamp"]
        )
    )
    import capo_kinesis.types.first_receive_timestamp

    out["FirstReceiveTimestamp"] = (
        capo_kinesis.types.first_receive_timestamp.serialize_aws_json_1_1(
            value["first_receive_timestamp"]
        )
    )
    out["ReceiveCount"] = value["receive_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueueRecord:
    out: QueueRecord = {}  # type: ignore[typeddict-item]
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    else:
        out["record_id"] = ""
    if data.get("PartitionKey") is not None:
        out["partition_key"] = data["PartitionKey"]
    if data.get("Data") is not None:
        import capo_kinesis.types.data

        out["data"] = capo_kinesis.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        out["data"] = b""
    if data.get("ApproximateArrivalTimestamp") is not None:
        import capo_kinesis.types.approximate_arrival_timestamp

        out["approximate_arrival_timestamp"] = (
            capo_kinesis.types.approximate_arrival_timestamp.deserialize_aws_json_1_1(
                data["ApproximateArrivalTimestamp"]
            )
        )
    else:
        import datetime

        out["approximate_arrival_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("FirstReceiveTimestamp") is not None:
        import capo_kinesis.types.first_receive_timestamp

        out["first_receive_timestamp"] = (
            capo_kinesis.types.first_receive_timestamp.deserialize_aws_json_1_1(
                data["FirstReceiveTimestamp"]
            )
        )
    else:
        import datetime

        out["first_receive_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ReceiveCount") is not None:
        out["receive_count"] = data["ReceiveCount"]
    else:
        out["receive_count"] = 0
    return out
