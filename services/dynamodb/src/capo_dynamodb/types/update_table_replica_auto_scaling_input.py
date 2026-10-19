"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTableReplicaAutoScalingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_settings_update
    import capo_dynamodb.types.global_secondary_index_auto_scaling_update_list
    import capo_dynamodb.types.replica_auto_scaling_update_list
    import capo_dynamodb.types.table_arn


class UpdateTableReplicaAutoScalingInput(TypedDict, closed=True):
    global_secondary_index_updates: NotRequired[
        "capo_dynamodb.types.global_secondary_index_auto_scaling_update_list.GlobalSecondaryIndexAutoScalingUpdateList"
    ]
    """<p>Represents the auto scaling settings of the global secondary indexes of the replica to be updated.</p>"""
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the global table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    provisioned_write_capacity_auto_scaling_update: NotRequired[
        "capo_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    replica_updates: NotRequired[
        "capo_dynamodb.types.replica_auto_scaling_update_list.ReplicaAutoScalingUpdateList"
    ]
    """<p>Represents the auto scaling settings of replicas of the table that will be modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableReplicaAutoScalingInput) -> dict:
    out: dict = {}
    if "global_secondary_index_updates" in value:
        import capo_dynamodb.types.global_secondary_index_auto_scaling_update_list

        out["GlobalSecondaryIndexUpdates"] = (
            capo_dynamodb.types.global_secondary_index_auto_scaling_update_list.serialize_aws_json_1_0(
                value["global_secondary_index_updates"]
            )
        )
    out["TableName"] = value["table_name"]
    if "provisioned_write_capacity_auto_scaling_update" in value:
        import capo_dynamodb.types.auto_scaling_settings_update

        out["ProvisionedWriteCapacityAutoScalingUpdate"] = (
            capo_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value["provisioned_write_capacity_auto_scaling_update"]
            )
        )
    if "replica_updates" in value:
        import capo_dynamodb.types.replica_auto_scaling_update_list

        out["ReplicaUpdates"] = (
            capo_dynamodb.types.replica_auto_scaling_update_list.serialize_aws_json_1_0(
                value["replica_updates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableReplicaAutoScalingInput:
    out: UpdateTableReplicaAutoScalingInput = {}  # type: ignore[typeddict-item]
    if data.get("GlobalSecondaryIndexUpdates") is not None:
        import capo_dynamodb.types.global_secondary_index_auto_scaling_update_list

        out["global_secondary_index_updates"] = (
            capo_dynamodb.types.global_secondary_index_auto_scaling_update_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexUpdates"]
            )
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("ProvisionedWriteCapacityAutoScalingUpdate") is not None:
        import capo_dynamodb.types.auto_scaling_settings_update

        out["provisioned_write_capacity_auto_scaling_update"] = (
            capo_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["ProvisionedWriteCapacityAutoScalingUpdate"]
            )
        )
    if data.get("ReplicaUpdates") is not None:
        import capo_dynamodb.types.replica_auto_scaling_update_list

        out["replica_updates"] = (
            capo_dynamodb.types.replica_auto_scaling_update_list.deserialize_aws_json_1_0(
                data["ReplicaUpdates"]
            )
        )
    return out
