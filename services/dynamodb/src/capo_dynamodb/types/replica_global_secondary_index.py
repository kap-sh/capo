"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.on_demand_throughput_override
    import capo_dynamodb.types.provisioned_throughput_override


class ReplicaGlobalSecondaryIndex(TypedDict, closed=True):
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index.</p>"""
    provisioned_throughput_override: NotRequired[
        "capo_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>Replica table GSI-specific provisioned throughput. If not specified, uses the source table GSI's read capacity settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "capo_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>Overrides the maximum on-demand throughput settings for the specified global secondary index in the specified replica table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndex) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    if "provisioned_throughput_override" in value:
        import capo_dynamodb.types.provisioned_throughput_override

        out["ProvisionedThroughputOverride"] = (
            capo_dynamodb.types.provisioned_throughput_override.serialize_aws_json_1_0(
                value["provisioned_throughput_override"]
            )
        )
    if "on_demand_throughput_override" in value:
        import capo_dynamodb.types.on_demand_throughput_override

        out["OnDemandThroughputOverride"] = (
            capo_dynamodb.types.on_demand_throughput_override.serialize_aws_json_1_0(
                value["on_demand_throughput_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaGlobalSecondaryIndex:
    out: ReplicaGlobalSecondaryIndex = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("ProvisionedThroughputOverride") is not None:
        import capo_dynamodb.types.provisioned_throughput_override

        out["provisioned_throughput_override"] = (
            capo_dynamodb.types.provisioned_throughput_override.deserialize_aws_json_1_0(
                data["ProvisionedThroughputOverride"]
            )
        )
    if data.get("OnDemandThroughputOverride") is not None:
        import capo_dynamodb.types.on_demand_throughput_override

        out["on_demand_throughput_override"] = (
            capo_dynamodb.types.on_demand_throughput_override.deserialize_aws_json_1_0(
                data["OnDemandThroughputOverride"]
            )
        )
    return out
