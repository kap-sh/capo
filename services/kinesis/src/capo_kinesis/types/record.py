"""Generated from Smithy shape ``com.amazonaws.kinesis#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.data
    import capo_kinesis.types.encryption_type
    import capo_kinesis.types.partition_key
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.timestamp


class Record(TypedDict, closed=True):
    sequence_number: "capo_kinesis.types.sequence_number.SequenceNumber"
    """<p>The unique identifier of the record within its shard.</p>"""
    approximate_arrival_timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The approximate time that the record was inserted into the stream.</p>"""
    data: "capo_kinesis.types.data.Data"
    """<p>The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).</p>"""
    partition_key: NotRequired["capo_kinesis.types.partition_key.PartitionKey"]
    """<p>Identifies which shard in the stream the data record is assigned to.</p> <p>For a stream that uses the <code>AUTO</code> record distribution strategy, this value is not returned if the producer did not provide a partition key when writing the record. If the producer provided a partition key, the original value is returned even though it was not used to determine shard placement.</p>"""
    encryption_type: NotRequired["capo_kinesis.types.encryption_type.EncryptionType"]
    """<p>The encryption type used on the record. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records in the stream.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Record) -> dict:
    out: dict = {}
    out["SequenceNumber"] = value["sequence_number"]
    if "approximate_arrival_timestamp" in value:
        import capo_kinesis.types.timestamp

        out["ApproximateArrivalTimestamp"] = (
            capo_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["approximate_arrival_timestamp"]
            )
        )
    import capo_kinesis.types.data

    out["Data"] = capo_kinesis.types.data.serialize_aws_json_1_1(value["data"])
    if "partition_key" in value:
        out["PartitionKey"] = value["partition_key"]
    if "encryption_type" in value:
        import capo_kinesis.types.encryption_type

        out["EncryptionType"] = (
            capo_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    else:
        out["sequence_number"] = ""
    if data.get("ApproximateArrivalTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["approximate_arrival_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["ApproximateArrivalTimestamp"]
            )
        )
    if data.get("Data") is not None:
        import capo_kinesis.types.data

        out["data"] = capo_kinesis.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        out["data"] = b""
    if data.get("PartitionKey") is not None:
        out["partition_key"] = data["PartitionKey"]
    if data.get("EncryptionType") is not None:
        import capo_kinesis.types.encryption_type

        out["encryption_type"] = (
            capo_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    return out
