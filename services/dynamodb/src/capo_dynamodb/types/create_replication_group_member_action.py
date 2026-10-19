"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateReplicationGroupMemberAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.kms_master_key_id
    import capo_dynamodb.types.on_demand_throughput_override
    import capo_dynamodb.types.provisioned_throughput_override
    import capo_dynamodb.types.region_name
    import capo_dynamodb.types.replica_global_secondary_index_list
    import capo_dynamodb.types.table_class


class CreateReplicationGroupMemberAction(TypedDict, closed=True):
    region_name: "capo_dynamodb.types.region_name.RegionName"
    """<p>The Region where the new replica will be created.</p>"""
    kms_master_key_id: NotRequired[
        "capo_dynamodb.types.kms_master_key_id.KMSMasterKeyId"
    ]
    """<p>The KMS key that should be used for KMS encryption in the new replica. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS key <code>alias/aws/dynamodb</code>.</p>"""
    provisioned_throughput_override: NotRequired[
        "capo_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>Replica-specific provisioned throughput. If not specified, uses the source table's provisioned throughput settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "capo_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>The maximum on-demand throughput settings for the specified replica table being created. You can only modify <code>MaxReadRequestUnits</code>, because you can't modify <code>MaxWriteRequestUnits</code> for individual replica tables. </p>"""
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.replica_global_secondary_index_list.ReplicaGlobalSecondaryIndexList"
    ]
    """<p>Replica-specific global secondary index settings.</p>"""
    table_class_override: NotRequired["capo_dynamodb.types.table_class.TableClass"]
    """<p>Replica-specific table class. If not specified, uses the source table's table class.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateReplicationGroupMemberAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    if "kms_master_key_id" in value:
        out["KMSMasterKeyId"] = value["kms_master_key_id"]
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
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.replica_global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.replica_global_secondary_index_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    if "table_class_override" in value:
        import capo_dynamodb.types.table_class

        out["TableClassOverride"] = (
            capo_dynamodb.types.table_class.serialize_aws_json_1_0(
                value["table_class_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateReplicationGroupMemberAction:
    out: CreateReplicationGroupMemberAction = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    if data.get("KMSMasterKeyId") is not None:
        out["kms_master_key_id"] = data["KMSMasterKeyId"]
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
    if data.get("GlobalSecondaryIndexes") is not None:
        import capo_dynamodb.types.replica_global_secondary_index_list

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.replica_global_secondary_index_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    if data.get("TableClassOverride") is not None:
        import capo_dynamodb.types.table_class

        out["table_class_override"] = (
            capo_dynamodb.types.table_class.deserialize_aws_json_1_0(
                data["TableClassOverride"]
            )
        )
    return out
