"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_settings_description
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.index_status
    import capo_dynamodb.types.positive_long_object


class ReplicaGlobalSecondaryIndexSettingsDescription(TypedDict, closed=True):
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index. The name must be unique among all other indexes on this table.</p>"""
    index_status: NotRequired["capo_dynamodb.types.index_status.IndexStatus"]
    """<p> The current status of the global secondary index:</p> <ul> <li> <p> <code>CREATING</code> - The global secondary index is being created.</p> </li> <li> <p> <code>UPDATING</code> - The global secondary index is being updated.</p> </li> <li> <p> <code>DELETING</code> - The global secondary index is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The global secondary index is ready for use.</p> </li> </ul>"""
    provisioned_read_capacity_units: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "capo_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global secondary index replica's read capacity units.</p>"""
    provisioned_write_capacity_units: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "capo_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global secondary index replica's write capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexSettingsDescription,
) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    if "index_status" in value:
        import capo_dynamodb.types.index_status

        out["IndexStatus"] = capo_dynamodb.types.index_status.serialize_aws_json_1_0(
            value["index_status"]
        )
    if "provisioned_read_capacity_units" in value:
        out["ProvisionedReadCapacityUnits"] = value["provisioned_read_capacity_units"]
    if "provisioned_read_capacity_auto_scaling_settings" in value:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["ProvisionedReadCapacityAutoScalingSettings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["provisioned_read_capacity_auto_scaling_settings"]
            )
        )
    if "provisioned_write_capacity_units" in value:
        out["ProvisionedWriteCapacityUnits"] = value["provisioned_write_capacity_units"]
    if "provisioned_write_capacity_auto_scaling_settings" in value:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["ProvisionedWriteCapacityAutoScalingSettings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["provisioned_write_capacity_auto_scaling_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ReplicaGlobalSecondaryIndexSettingsDescription:
    out: ReplicaGlobalSecondaryIndexSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("IndexStatus") is not None:
        import capo_dynamodb.types.index_status

        out["index_status"] = capo_dynamodb.types.index_status.deserialize_aws_json_1_0(
            data["IndexStatus"]
        )
    if data.get("ProvisionedReadCapacityUnits") is not None:
        out["provisioned_read_capacity_units"] = data["ProvisionedReadCapacityUnits"]
    if data.get("ProvisionedReadCapacityAutoScalingSettings") is not None:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["provisioned_read_capacity_auto_scaling_settings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ProvisionedReadCapacityAutoScalingSettings"]
            )
        )
    if data.get("ProvisionedWriteCapacityUnits") is not None:
        out["provisioned_write_capacity_units"] = data["ProvisionedWriteCapacityUnits"]
    if data.get("ProvisionedWriteCapacityAutoScalingSettings") is not None:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["provisioned_write_capacity_auto_scaling_settings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ProvisionedWriteCapacityAutoScalingSettings"]
            )
        )
    return out
