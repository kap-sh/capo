"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.data
    import capo_kinesis.types.hash_key
    import capo_kinesis.types.partition_key


class PutRecordsRequestEntry(TypedDict, closed=True):
    data: "capo_kinesis.types.data.Data"
    """<p>The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).</p>"""
    explicit_hash_key: NotRequired["capo_kinesis.types.hash_key.HashKey"]
    """<p>The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.</p>"""
    partition_key: NotRequired["capo_kinesis.types.partition_key.PartitionKey"]
    """<p>Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.</p> <p>If the stream uses the <code>USER_PARTITION_KEY</code> record distribution strategy (the default), a partition key is required for each record. If the stream uses the <code>AUTO</code> record distribution strategy, the partition key is optional and any value you provide is ignored, along with any <code>ExplicitHashKey</code> you provide. In that case, Amazon Kinesis Data Streams distributes records across shards using service-managed algorithms. For more information, see <code>UpdateStreamRecordDistributionStrategy</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsRequestEntry) -> dict:
    out: dict = {}
    import capo_kinesis.types.data

    out["Data"] = capo_kinesis.types.data.serialize_aws_json_1_1(value["data"])
    if "explicit_hash_key" in value:
        out["ExplicitHashKey"] = value["explicit_hash_key"]
    if "partition_key" in value:
        out["PartitionKey"] = value["partition_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordsRequestEntry:
    out: PutRecordsRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("Data") is not None:
        import capo_kinesis.types.data

        out["data"] = capo_kinesis.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        out["data"] = b""
    if data.get("ExplicitHashKey") is not None:
        out["explicit_hash_key"] = data["ExplicitHashKey"]
    if data.get("PartitionKey") is not None:
        out["partition_key"] = data["PartitionKey"]
    return out
