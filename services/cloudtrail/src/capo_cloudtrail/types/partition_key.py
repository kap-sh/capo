"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PartitionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.partition_key_name
    import capo_cloudtrail.types.partition_key_type


class PartitionKey(TypedDict, closed=True):
    name: "capo_cloudtrail.types.partition_key_name.PartitionKeyName"
    """<p>The name of the partition key.</p>"""
    type: "capo_cloudtrail.types.partition_key_type.PartitionKeyType"
    """<p>The data type of the partition key. For example, <code>bigint</code> or <code>string</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionKey) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionKey:
    out: PartitionKey = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
