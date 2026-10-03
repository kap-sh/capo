"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalSecondaryIndexAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.projection
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.warm_throughput


class CreateGlobalSecondaryIndexAction(TypedDict, closed=True):
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index to be created.</p>"""
    key_schema: "capo_dynamodb.types.key_schema.KeySchema"
    """<p>The key schema for the global secondary index. Global secondary index supports up to 4 partition and up to 4 sort keys.</p>"""
    projection: "capo_dynamodb.types.projection.Projection"
    """<p>Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.</p>"""
    provisioned_throughput: NotRequired[
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index.</p> <p>For current minimum and maximum provisioned throughput values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>The maximum number of read and write units for the global secondary index being created. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both. You must use either <code>OnDemand Throughput</code> or <code>ProvisionedThroughput</code> based on your table's capacity mode.</p>"""
    warm_throughput: NotRequired["capo_dynamodb.types.warm_throughput.WarmThroughput"]
    """<p>Represents the warm throughput value (in read units per second and write units per second) when creating a secondary index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateGlobalSecondaryIndexAction) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    import capo_dynamodb.types.key_schema

    out["KeySchema"] = capo_dynamodb.types.key_schema.serialize_aws_json_1_0(
        value["key_schema"]
    )
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
    if "warm_throughput" in value:
        import capo_dynamodb.types.warm_throughput

        out["WarmThroughput"] = (
            capo_dynamodb.types.warm_throughput.serialize_aws_json_1_0(
                value["warm_throughput"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateGlobalSecondaryIndexAction:
    out: CreateGlobalSecondaryIndexAction = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError(
            "CreateGlobalSecondaryIndexAction.index_name required"
        )
    if data.get("KeySchema") is not None:
        import capo_dynamodb.types.key_schema

        out["key_schema"] = capo_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    else:
        raise DeserializationError(
            "CreateGlobalSecondaryIndexAction.key_schema required"
        )
    if data.get("Projection") is not None:
        import capo_dynamodb.types.projection

        out["projection"] = capo_dynamodb.types.projection.deserialize_aws_json_1_0(
            data["Projection"]
        )
    else:
        raise DeserializationError(
            "CreateGlobalSecondaryIndexAction.projection required"
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
    if data.get("WarmThroughput") is not None:
        import capo_dynamodb.types.warm_throughput

        out["warm_throughput"] = (
            capo_dynamodb.types.warm_throughput.deserialize_aws_json_1_0(
                data["WarmThroughput"]
            )
        )
    return out
