"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableFromBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_arn
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.global_secondary_index_list
    import capo_dynamodb.types.local_secondary_index_list
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.sse_specification
    import capo_dynamodb.types.table_name
    import capo_dynamodb.types.vector_index_list


class RestoreTableFromBackupInput(TypedDict, closed=True):
    target_table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The name of the new table to which the backup must be restored.</p>"""
    backup_arn: "capo_dynamodb.types.backup_arn.BackupArn"
    """<p>The Amazon Resource Name (ARN) associated with the backup.</p>"""
    billing_mode_override: NotRequired["capo_dynamodb.types.billing_mode.BillingMode"]
    """<p>The billing mode of the restored table.</p>"""
    global_secondary_index_override: NotRequired[
        "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
    ]
    """<p>List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>"""
    local_secondary_index_override: NotRequired[
        "capo_dynamodb.types.local_secondary_index_list.LocalSecondaryIndexList"
    ]
    """<p>List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>"""
    provisioned_throughput_override: NotRequired[
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Provisioned throughput settings for the restored table.</p>"""
    on_demand_throughput_override: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    sse_specification_override: NotRequired[
        "capo_dynamodb.types.sse_specification.SSESpecification"
    ]
    """<p>The new server-side encryption settings for the restored table.</p>"""
    vector_index_override: NotRequired[
        "capo_dynamodb.types.vector_index_list.VectorIndexList"
    ]
    """<p>The vector indexes for the restored table. If not specified, all vector indexes from the backup are restored. The indexes provided must match existing vector indexes from the backup. You can choose to exclude some or all of the vector indexes at the time of restore.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreTableFromBackupInput) -> dict:
    out: dict = {}
    out["TargetTableName"] = value["target_table_name"]
    out["BackupArn"] = value["backup_arn"]
    if "billing_mode_override" in value:
        import capo_dynamodb.types.billing_mode

        out["BillingModeOverride"] = (
            capo_dynamodb.types.billing_mode.serialize_aws_json_1_0(
                value["billing_mode_override"]
            )
        )
    if "global_secondary_index_override" in value:
        import capo_dynamodb.types.global_secondary_index_list

        out["GlobalSecondaryIndexOverride"] = (
            capo_dynamodb.types.global_secondary_index_list.serialize_aws_json_1_0(
                value["global_secondary_index_override"]
            )
        )
    if "local_secondary_index_override" in value:
        import capo_dynamodb.types.local_secondary_index_list

        out["LocalSecondaryIndexOverride"] = (
            capo_dynamodb.types.local_secondary_index_list.serialize_aws_json_1_0(
                value["local_secondary_index_override"]
            )
        )
    if "provisioned_throughput_override" in value:
        import capo_dynamodb.types.provisioned_throughput

        out["ProvisionedThroughputOverride"] = (
            capo_dynamodb.types.provisioned_throughput.serialize_aws_json_1_0(
                value["provisioned_throughput_override"]
            )
        )
    if "on_demand_throughput_override" in value:
        import capo_dynamodb.types.on_demand_throughput

        out["OnDemandThroughputOverride"] = (
            capo_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput_override"]
            )
        )
    if "sse_specification_override" in value:
        import capo_dynamodb.types.sse_specification

        out["SSESpecificationOverride"] = (
            capo_dynamodb.types.sse_specification.serialize_aws_json_1_0(
                value["sse_specification_override"]
            )
        )
    if "vector_index_override" in value:
        import capo_dynamodb.types.vector_index_list

        out["VectorIndexOverride"] = (
            capo_dynamodb.types.vector_index_list.serialize_aws_json_1_0(
                value["vector_index_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreTableFromBackupInput:
    out: RestoreTableFromBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetTableName") is not None:
        out["target_table_name"] = data["TargetTableName"]
    else:
        out["target_table_name"] = ""
    if data.get("BackupArn") is not None:
        out["backup_arn"] = data["BackupArn"]
    else:
        out["backup_arn"] = ""
    if data.get("BillingModeOverride") is not None:
        import capo_dynamodb.types.billing_mode

        out["billing_mode_override"] = (
            capo_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingModeOverride"]
            )
        )
    if data.get("GlobalSecondaryIndexOverride") is not None:
        import capo_dynamodb.types.global_secondary_index_list

        out["global_secondary_index_override"] = (
            capo_dynamodb.types.global_secondary_index_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexOverride"]
            )
        )
    if data.get("LocalSecondaryIndexOverride") is not None:
        import capo_dynamodb.types.local_secondary_index_list

        out["local_secondary_index_override"] = (
            capo_dynamodb.types.local_secondary_index_list.deserialize_aws_json_1_0(
                data["LocalSecondaryIndexOverride"]
            )
        )
    if data.get("ProvisionedThroughputOverride") is not None:
        import capo_dynamodb.types.provisioned_throughput

        out["provisioned_throughput_override"] = (
            capo_dynamodb.types.provisioned_throughput.deserialize_aws_json_1_0(
                data["ProvisionedThroughputOverride"]
            )
        )
    if data.get("OnDemandThroughputOverride") is not None:
        import capo_dynamodb.types.on_demand_throughput

        out["on_demand_throughput_override"] = (
            capo_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughputOverride"]
            )
        )
    if data.get("SSESpecificationOverride") is not None:
        import capo_dynamodb.types.sse_specification

        out["sse_specification_override"] = (
            capo_dynamodb.types.sse_specification.deserialize_aws_json_1_0(
                data["SSESpecificationOverride"]
            )
        )
    if data.get("VectorIndexOverride") is not None:
        import capo_dynamodb.types.vector_index_list

        out["vector_index_override"] = (
            capo_dynamodb.types.vector_index_list.deserialize_aws_json_1_0(
                data["VectorIndexOverride"]
            )
        )
    return out
