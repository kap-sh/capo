"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_settings_update
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.global_table_global_secondary_index_settings_update_list
    import capo_dynamodb.types.positive_long_object
    import capo_dynamodb.types.replica_settings_update_list
    import capo_dynamodb.types.table_name


class UpdateGlobalTableSettingsInput(TypedDict, closed=True):
    global_table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The name of the global table</p>"""
    global_table_billing_mode: NotRequired[
        "capo_dynamodb.types.billing_mode.BillingMode"
    ]
    """<p>The billing mode of the global table. If <code>GlobalTableBillingMode</code> is not specified, the global table defaults to <code>PROVISIONED</code> capacity billing mode.</p> <ul> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for predictable workloads. <code>PROVISIONED</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">Provisioned capacity mode</a>.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html">On-demand capacity mode</a>. </p> </li> </ul>"""
    global_table_provisioned_write_capacity_units: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException.</code> </p>"""
    global_table_provisioned_write_capacity_auto_scaling_settings_update: NotRequired[
        "capo_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    """<p>Auto scaling settings for managing provisioned write capacity for the global table.</p>"""
    global_table_global_secondary_index_settings_update: NotRequired[
        "capo_dynamodb.types.global_table_global_secondary_index_settings_update_list.GlobalTableGlobalSecondaryIndexSettingsUpdateList"
    ]
    """<p>Represents the settings of a global secondary index for a global table that will be modified.</p>"""
    replica_settings_update: NotRequired[
        "capo_dynamodb.types.replica_settings_update_list.ReplicaSettingsUpdateList"
    ]
    """<p>Represents the settings for a global table in a Region that will be modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateGlobalTableSettingsInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    if "global_table_billing_mode" in value:
        import capo_dynamodb.types.billing_mode

        out["GlobalTableBillingMode"] = (
            capo_dynamodb.types.billing_mode.serialize_aws_json_1_0(
                value["global_table_billing_mode"]
            )
        )
    if "global_table_provisioned_write_capacity_units" in value:
        out["GlobalTableProvisionedWriteCapacityUnits"] = value[
            "global_table_provisioned_write_capacity_units"
        ]
    if "global_table_provisioned_write_capacity_auto_scaling_settings_update" in value:
        import capo_dynamodb.types.auto_scaling_settings_update

        out["GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"] = (
            capo_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value[
                    "global_table_provisioned_write_capacity_auto_scaling_settings_update"
                ]
            )
        )
    if "global_table_global_secondary_index_settings_update" in value:
        import capo_dynamodb.types.global_table_global_secondary_index_settings_update_list

        out["GlobalTableGlobalSecondaryIndexSettingsUpdate"] = (
            capo_dynamodb.types.global_table_global_secondary_index_settings_update_list.serialize_aws_json_1_0(
                value["global_table_global_secondary_index_settings_update"]
            )
        )
    if "replica_settings_update" in value:
        import capo_dynamodb.types.replica_settings_update_list

        out["ReplicaSettingsUpdate"] = (
            capo_dynamodb.types.replica_settings_update_list.serialize_aws_json_1_0(
                value["replica_settings_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateGlobalTableSettingsInput:
    out: UpdateGlobalTableSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("GlobalTableName") is not None:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        raise DeserializationError(
            "UpdateGlobalTableSettingsInput.global_table_name required"
        )
    if data.get("GlobalTableBillingMode") is not None:
        import capo_dynamodb.types.billing_mode

        out["global_table_billing_mode"] = (
            capo_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
                data["GlobalTableBillingMode"]
            )
        )
    if data.get("GlobalTableProvisionedWriteCapacityUnits") is not None:
        out["global_table_provisioned_write_capacity_units"] = data[
            "GlobalTableProvisionedWriteCapacityUnits"
        ]
    if (
        data.get("GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate")
        is not None
    ):
        import capo_dynamodb.types.auto_scaling_settings_update

        out["global_table_provisioned_write_capacity_auto_scaling_settings_update"] = (
            capo_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"]
            )
        )
    if data.get("GlobalTableGlobalSecondaryIndexSettingsUpdate") is not None:
        import capo_dynamodb.types.global_table_global_secondary_index_settings_update_list

        out["global_table_global_secondary_index_settings_update"] = (
            capo_dynamodb.types.global_table_global_secondary_index_settings_update_list.deserialize_aws_json_1_0(
                data["GlobalTableGlobalSecondaryIndexSettingsUpdate"]
            )
        )
    if data.get("ReplicaSettingsUpdate") is not None:
        import capo_dynamodb.types.replica_settings_update_list

        out["replica_settings_update"] = (
            capo_dynamodb.types.replica_settings_update_list.deserialize_aws_json_1_0(
                data["ReplicaSettingsUpdate"]
            )
        )
    return out
