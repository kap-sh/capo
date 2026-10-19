"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.data
    import capo_kinesis.types.hash_key
    import capo_kinesis.types.partition_key
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class PutRecordInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to put the data record into.</p>"""
    data: "capo_kinesis.types.data.Data"
    """<p>The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).</p>"""
    partition_key: NotRequired["capo_kinesis.types.partition_key.PartitionKey"]
    """<p>Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.</p> <p>If the stream uses the <code>USER_PARTITION_KEY</code> record distribution strategy (the default), a partition key is required. If the stream uses the <code>AUTO</code> record distribution strategy, the partition key is optional and any value you provide is ignored, along with any <code>ExplicitHashKey</code> you provide. In that case, Amazon Kinesis Data Streams distributes the record across shards using service-managed algorithms. For more information, see <code>UpdateStreamRecordDistributionStrategy</code>.</p>"""
    explicit_hash_key: NotRequired["capo_kinesis.types.hash_key.HashKey"]
    """<p>The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.</p>"""
    sequence_number_for_ordering: NotRequired[
        "capo_kinesis.types.sequence_number.SequenceNumber"
    ]
    """<p>Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the <code>SequenceNumberForOrdering</code> of record <i>n</i> to the sequence number of record <i>n-1</i> (as returned in the result when putting record <i>n-1</i>). If this parameter is not set, records are coarsely ordered based on arrival time.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    dry_run: NotRequired["capo_kinesis.types.boolean_object.BooleanObject"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import capo_kinesis.types.data

    out["Data"] = capo_kinesis.types.data.serialize_aws_json_1_1(value["data"])
    if "partition_key" in value:
        out["PartitionKey"] = value["partition_key"]
    if "explicit_hash_key" in value:
        out["ExplicitHashKey"] = value["explicit_hash_key"]
    if "sequence_number_for_ordering" in value:
        out["SequenceNumberForOrdering"] = value["sequence_number_for_ordering"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordInput:
    out: PutRecordInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("Data") is not None:
        import capo_kinesis.types.data

        out["data"] = capo_kinesis.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        out["data"] = b""
    if data.get("PartitionKey") is not None:
        out["partition_key"] = data["PartitionKey"]
    if data.get("ExplicitHashKey") is not None:
        out["explicit_hash_key"] = data["ExplicitHashKey"]
    if data.get("SequenceNumberForOrdering") is not None:
        out["sequence_number_for_ordering"] = data["SequenceNumberForOrdering"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
