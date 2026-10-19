"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.encryption_type
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.shard_id


class PutRecordOutput(TypedDict, closed=True):
    shard_id: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the shard where the data record was placed.</p>"""
    sequence_number: "capo_kinesis.types.sequence_number.SequenceNumber"
    """<p>The sequence number identifier that was assigned to the put data record. The sequence number for the record is unique across all records in the stream. A sequence number is the identifier associated with every record put into the stream.</p>"""
    encryption_type: NotRequired["capo_kinesis.types.encryption_type.EncryptionType"]
    """<p>The encryption type to use on the record. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records in the stream.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordOutput) -> dict:
    out: dict = {}
    out["ShardId"] = value["shard_id"]
    out["SequenceNumber"] = value["sequence_number"]
    if "encryption_type" in value:
        import capo_kinesis.types.encryption_type

        out["EncryptionType"] = (
            capo_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordOutput:
    out: PutRecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    else:
        out["shard_id"] = ""
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    else:
        out["sequence_number"] = ""
    if data.get("EncryptionType") is not None:
        import capo_kinesis.types.encryption_type

        out["encryption_type"] = (
            capo_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    return out
