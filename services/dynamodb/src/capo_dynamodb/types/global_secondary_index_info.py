"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.projection
    import capo_dynamodb.types.provisioned_throughput


class GlobalSecondaryIndexInfo(TypedDict, closed=True):
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    key_schema: NotRequired["capo_dynamodb.types.key_schema.KeySchema"]
    """<p>The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: NotRequired["capo_dynamodb.types.projection.Projection"]
    """<p>Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""
    provisioned_throughput: NotRequired[
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index. </p>"""
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexInfo) -> dict:
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
    if "provisioned_throughput" in value:
        import capo_dynamodb.types.provisioned_throughput

        out["ProvisionedThroughput"] = (
            capo_dynamodb.types.provisioned_throughput.serialize_aws_json_1_0(
                value["provisioned_throughput"]
            )
        )
    if "on_demand_throughput" in value:
        import capo_dynamodb.types.on_demand_throughput

        out["OnDemandThroughput"] = (
            capo_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalSecondaryIndexInfo:
    out: GlobalSecondaryIndexInfo = {}  # type: ignore[typeddict-item]
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
    if data.get("ProvisionedThroughput") is not None:
        import capo_dynamodb.types.provisioned_throughput

        out["provisioned_throughput"] = (
            capo_dynamodb.types.provisioned_throughput.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    if data.get("OnDemandThroughput") is not None:
        import capo_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            capo_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    return out
