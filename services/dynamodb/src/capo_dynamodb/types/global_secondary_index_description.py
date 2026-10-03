"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backfilling
    import capo_dynamodb.types.global_secondary_index_warm_throughput_description
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.index_status
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.long_object
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.projection
    import capo_dynamodb.types.provisioned_throughput_description
    import capo_dynamodb.types.string


class GlobalSecondaryIndexDescription(TypedDict, closed=True):
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    key_schema: NotRequired["capo_dynamodb.types.key_schema.KeySchema"]
    """<p>The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: NotRequired["capo_dynamodb.types.projection.Projection"]
    """<p>Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""
    index_status: NotRequired["capo_dynamodb.types.index_status.IndexStatus"]
    """<p>The current state of the global secondary index:</p> <ul> <li> <p> <code>CREATING</code> - The index is being created.</p> </li> <li> <p> <code>UPDATING</code> - The index is being updated.</p> </li> <li> <p> <code>DELETING</code> - The index is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The index is ready for use.</p> </li> </ul>"""
    backfilling: NotRequired["capo_dynamodb.types.backfilling.Backfilling"]
    """<p>Indicates whether the index is currently backfilling. <i>Backfilling</i> is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and <code>Backfilling</code> is false.</p> <p>You can delete an index that is being created during the <code>Backfilling</code> phase when <code>IndexStatus</code> is set to CREATING and <code>Backfilling</code> is true. You can't delete the index that is being created when <code>IndexStatus</code> is set to CREATING and <code>Backfilling</code> is false. </p> <note> <p>For indexes that were created during a <code>CreateTable</code> operation, the <code>Backfilling</code> attribute does not appear in the <code>DescribeTable</code> output.</p> </note>"""
    provisioned_throughput: NotRequired[
        "capo_dynamodb.types.provisioned_throughput_description.ProvisionedThroughputDescription"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index.</p> <p>For current minimum and maximum provisioned throughput values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    index_size_bytes: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    item_count: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    index_arn: NotRequired["capo_dynamodb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the index.</p>"""
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>"""
    warm_throughput: NotRequired[
        "capo_dynamodb.types.global_secondary_index_warm_throughput_description.GlobalSecondaryIndexWarmThroughputDescription"
    ]
    """<p>Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexDescription) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "key_schema" in value:
        import capo_dynamodb.types.key_schema

        out["KeySchema"] = capo_dynamodb.types.key_schema.serialize_aws_json_1_0(
            value["key_schema"]
        )
    if "projection" in value:
        import capo_dynamodb.types.projection

        out["Projection"] = capo_dynamodb.types.projection.serialize_aws_json_1_0(
            value["projection"]
        )
    if "index_status" in value:
        import capo_dynamodb.types.index_status

        out["IndexStatus"] = capo_dynamodb.types.index_status.serialize_aws_json_1_0(
            value["index_status"]
        )
    if "backfilling" in value:
        out["Backfilling"] = value["backfilling"]
    if "provisioned_throughput" in value:
        import capo_dynamodb.types.provisioned_throughput_description

        out["ProvisionedThroughput"] = (
            capo_dynamodb.types.provisioned_throughput_description.serialize_aws_json_1_0(
                value["provisioned_throughput"]
            )
        )
    if "index_size_bytes" in value:
        out["IndexSizeBytes"] = value["index_size_bytes"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "index_arn" in value:
        out["IndexArn"] = value["index_arn"]
    if "on_demand_throughput" in value:
        import capo_dynamodb.types.on_demand_throughput

        out["OnDemandThroughput"] = (
            capo_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput"]
            )
        )
    if "warm_throughput" in value:
        import capo_dynamodb.types.global_secondary_index_warm_throughput_description

        out["WarmThroughput"] = (
            capo_dynamodb.types.global_secondary_index_warm_throughput_description.serialize_aws_json_1_0(
                value["warm_throughput"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalSecondaryIndexDescription:
    out: GlobalSecondaryIndexDescription = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    if data.get("KeySchema") is not None:
        import capo_dynamodb.types.key_schema

        out["key_schema"] = capo_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    if data.get("Projection") is not None:
        import capo_dynamodb.types.projection

        out["projection"] = capo_dynamodb.types.projection.deserialize_aws_json_1_0(
            data["Projection"]
        )
    if data.get("IndexStatus") is not None:
        import capo_dynamodb.types.index_status

        out["index_status"] = capo_dynamodb.types.index_status.deserialize_aws_json_1_0(
            data["IndexStatus"]
        )
    if data.get("Backfilling") is not None:
        out["backfilling"] = data["Backfilling"]
    if data.get("ProvisionedThroughput") is not None:
        import capo_dynamodb.types.provisioned_throughput_description

        out["provisioned_throughput"] = (
            capo_dynamodb.types.provisioned_throughput_description.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    if data.get("IndexSizeBytes") is not None:
        out["index_size_bytes"] = data["IndexSizeBytes"]
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    if data.get("IndexArn") is not None:
        out["index_arn"] = data["IndexArn"]
    if data.get("OnDemandThroughput") is not None:
        import capo_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            capo_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if data.get("WarmThroughput") is not None:
        import capo_dynamodb.types.global_secondary_index_warm_throughput_description

        out["warm_throughput"] = (
            capo_dynamodb.types.global_secondary_index_warm_throughput_description.deserialize_aws_json_1_0(
                data["WarmThroughput"]
            )
        )
    return out
