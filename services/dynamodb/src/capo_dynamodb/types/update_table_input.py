"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_definitions
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.deletion_protection_enabled
    import capo_dynamodb.types.global_secondary_index_update_list
    import capo_dynamodb.types.global_table_settings_replication_mode
    import capo_dynamodb.types.global_table_witness_group_update_list
    import capo_dynamodb.types.multi_region_consistency
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.replication_group_update_list
    import capo_dynamodb.types.sse_specification
    import capo_dynamodb.types.stream_specification
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_class
    import capo_dynamodb.types.vector_index_update_list
    import capo_dynamodb.types.warm_throughput


class UpdateTableInput(TypedDict, closed=True):
    attribute_definitions: NotRequired[
        "capo_dynamodb.types.attribute_definitions.AttributeDefinitions"
    ]
    """<p>An array of attributes that describe the key schema for the table and indexes. If you are adding a new global secondary index to the table, <code>AttributeDefinitions</code> must include the key element(s) of the new index.</p>"""
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    billing_mode: NotRequired["capo_dynamodb.types.billing_mode.BillingMode"]
    """<p>Controls how you are charged for read and write throughput and how you manage capacity. When switching from pay-per-request to provisioned capacity, initial provisioned capacity values must be set. The initial provisioned capacity values are estimated based on the consumed read and write capacity of your table and global secondary indexes over the past 30 minutes.</p> <ul> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for most DynamoDB workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html">On-demand capacity mode</a>. </p> </li> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for steady workloads with predictable growth where capacity requirements can be reliably forecasted. <code>PROVISIONED</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">Provisioned capacity mode</a>.</p> </li> </ul>"""
    provisioned_throughput: NotRequired[
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>The new provisioned throughput settings for the specified table or index.</p>"""
    global_secondary_index_updates: NotRequired[
        "capo_dynamodb.types.global_secondary_index_update_list.GlobalSecondaryIndexUpdateList"
    ]
    """<p>An array of one or more global secondary indexes for the table. For each index in the array, you can request one action:</p> <ul> <li> <p> <code>Create</code> - add a new global secondary index to the table.</p> </li> <li> <p> <code>Update</code> - modify the provisioned throughput settings of an existing global secondary index.</p> </li> <li> <p> <code>Delete</code> - remove a global secondary index from the table.</p> </li> </ul> <p>You can create or delete only one global secondary index per <code>UpdateTable</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.html">Managing Global Secondary Indexes</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p>"""
    stream_specification: NotRequired[
        "capo_dynamodb.types.stream_specification.StreamSpecification"
    ]
    """<p>Represents the DynamoDB Streams configuration for the table.</p> <note> <p>You receive a <code>ValidationException</code> if you try to enable a stream on a table that already has a stream, or if you try to disable a stream on a table that doesn't have a stream.</p> </note>"""
    sse_specification: NotRequired[
        "capo_dynamodb.types.sse_specification.SSESpecification"
    ]
    """<p>The new server-side encryption settings for the specified table.</p>"""
    replica_updates: NotRequired[
        "capo_dynamodb.types.replication_group_update_list.ReplicationGroupUpdateList"
    ]
    """<p>A list of replica update actions (create, delete, or update) for the table.</p>"""
    table_class: NotRequired["capo_dynamodb.types.table_class.TableClass"]
    """<p>The table class of the table to be updated. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</p>"""
    deletion_protection_enabled: NotRequired[
        "capo_dynamodb.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.</p>"""
    multi_region_consistency: NotRequired[
        "capo_dynamodb.types.multi_region_consistency.MultiRegionConsistency"
    ]
    """<p>Specifies the consistency mode for a new global table. This parameter is only valid when you create a global table by specifying one or more <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicationGroupUpdate.html#DDB-Type-ReplicationGroupUpdate-Create">Create</a> actions in the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html#DDB-UpdateTable-request-ReplicaUpdates">ReplicaUpdates</a> action list.</p> <p>You can specify one of the following consistency modes:</p> <ul> <li> <p> <code>EVENTUAL</code>: Configures a new global table for multi-Region eventual consistency (MREC). This is the default consistency mode for global tables.</p> </li> <li> <p> <code>STRONG</code>: Configures a new global table for multi-Region strong consistency (MRSC).</p> </li> </ul> <p>If you don't specify this field, the global table consistency mode defaults to <code>EVENTUAL</code>. For more information about global tables consistency modes, see <a href="https://docs.aws.amazon.com/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes"> Consistency modes</a> in DynamoDB developer guide. </p>"""
    global_table_witness_updates: NotRequired[
        "capo_dynamodb.types.global_table_witness_group_update_list.GlobalTableWitnessGroupUpdateList"
    ]
    """<p>A list of witness updates for a MRSC global table. A witness provides a cost-effective alternative to a full replica in a MRSC global table by maintaining replicated change data written to global table replicas. You cannot perform read or write operations on a witness. For each witness, you can request one action:</p> <ul> <li> <p> <code>Create</code> - add a new witness to the global table.</p> </li> <li> <p> <code>Delete</code> - remove a witness from the global table.</p> </li> </ul> <p>You can create or delete only one witness per <code>UpdateTable</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes">Multi-Region strong consistency (MRSC)</a> in the Amazon DynamoDB Developer Guide</p>"""
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>Updates the maximum number of read and write units for the specified table in on-demand capacity mode. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>"""
    warm_throughput: NotRequired["capo_dynamodb.types.warm_throughput.WarmThroughput"]
    """<p>Represents the warm throughput (in read units per second and write units per second) for updating a table.</p>"""
    global_table_settings_replication_mode: NotRequired[
        "capo_dynamodb.types.global_table_settings_replication_mode.GlobalTableSettingsReplicationMode"
    ]
    """<p>Controls the settings replication mode for a global table replica. This attribute can be defined using UpdateTable operation only on a regional table with values:</p> <ul> <li> <p> <code>ENABLED</code>: Defines settings replication on a regional table to be used as a source table for creating Multi-Account Global Table.</p> </li> <li> <p> <code>DISABLED</code>: Remove settings replication on a regional table. Settings replication needs to be defined to ENABLED again in order to create a Multi-Account Global Table using this table. </p> </li> </ul>"""
    vector_index_updates: NotRequired[
        "capo_dynamodb.types.vector_index_update_list.VectorIndexUpdateList"
    ]
    """<p>A list of vector indexes to be added to or removed from the table. You can add or remove one vector index for each <code>UpdateTable</code> operation.</p> <p>To add a vector index, specify <code>IndexName</code>, <code>VectorAttribute</code>, <code>Dimensions</code>, <code>DistanceFunction</code>, and <code>Projection</code>. To remove a vector index, specify only the <code>IndexName</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableInput) -> dict:
    out: dict = {}
    if "attribute_definitions" in value:
        import capo_dynamodb.types.attribute_definitions

        out["AttributeDefinitions"] = (
            capo_dynamodb.types.attribute_definitions.serialize_aws_json_1_0(
                value["attribute_definitions"]
            )
        )
    out["TableName"] = value["table_name"]
    if "billing_mode" in value:
        import capo_dynamodb.types.billing_mode

        out["BillingMode"] = capo_dynamodb.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    if "provisioned_throughput" in value:
        import capo_dynamodb.types.provisioned_throughput

        out["ProvisionedThroughput"] = (
            capo_dynamodb.types.provisioned_throughput.serialize_aws_json_1_0(
                value["provisioned_throughput"]
            )
        )
    if "global_secondary_index_updates" in value:
        import capo_dynamodb.types.global_secondary_index_update_list

        out["GlobalSecondaryIndexUpdates"] = (
            capo_dynamodb.types.global_secondary_index_update_list.serialize_aws_json_1_0(
                value["global_secondary_index_updates"]
            )
        )
    if "stream_specification" in value:
        import capo_dynamodb.types.stream_specification

        out["StreamSpecification"] = (
            capo_dynamodb.types.stream_specification.serialize_aws_json_1_0(
                value["stream_specification"]
            )
        )
    if "sse_specification" in value:
        import capo_dynamodb.types.sse_specification

        out["SSESpecification"] = (
            capo_dynamodb.types.sse_specification.serialize_aws_json_1_0(
                value["sse_specification"]
            )
        )
    if "replica_updates" in value:
        import capo_dynamodb.types.replication_group_update_list

        out["ReplicaUpdates"] = (
            capo_dynamodb.types.replication_group_update_list.serialize_aws_json_1_0(
                value["replica_updates"]
            )
        )
    if "table_class" in value:
        import capo_dynamodb.types.table_class

        out["TableClass"] = capo_dynamodb.types.table_class.serialize_aws_json_1_0(
            value["table_class"]
        )
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "multi_region_consistency" in value:
        import capo_dynamodb.types.multi_region_consistency

        out["MultiRegionConsistency"] = (
            capo_dynamodb.types.multi_region_consistency.serialize_aws_json_1_0(
                value["multi_region_consistency"]
            )
        )
    if "global_table_witness_updates" in value:
        import capo_dynamodb.types.global_table_witness_group_update_list

        out["GlobalTableWitnessUpdates"] = (
            capo_dynamodb.types.global_table_witness_group_update_list.serialize_aws_json_1_0(
                value["global_table_witness_updates"]
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
    if "global_table_settings_replication_mode" in value:
        import capo_dynamodb.types.global_table_settings_replication_mode

        out["GlobalTableSettingsReplicationMode"] = (
            capo_dynamodb.types.global_table_settings_replication_mode.serialize_aws_json_1_0(
                value["global_table_settings_replication_mode"]
            )
        )
    if "vector_index_updates" in value:
        import capo_dynamodb.types.vector_index_update_list

        out["VectorIndexUpdates"] = (
            capo_dynamodb.types.vector_index_update_list.serialize_aws_json_1_0(
                value["vector_index_updates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableInput:
    out: UpdateTableInput = {}  # type: ignore[typeddict-item]
    if data.get("AttributeDefinitions") is not None:
        import capo_dynamodb.types.attribute_definitions

        out["attribute_definitions"] = (
            capo_dynamodb.types.attribute_definitions.deserialize_aws_json_1_0(
                data["AttributeDefinitions"]
            )
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("UpdateTableInput.table_name required")
    if data.get("BillingMode") is not None:
        import capo_dynamodb.types.billing_mode

        out["billing_mode"] = capo_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
            data["BillingMode"]
        )
    if data.get("ProvisionedThroughput") is not None:
        import capo_dynamodb.types.provisioned_throughput

        out["provisioned_throughput"] = (
            capo_dynamodb.types.provisioned_throughput.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    if data.get("GlobalSecondaryIndexUpdates") is not None:
        import capo_dynamodb.types.global_secondary_index_update_list

        out["global_secondary_index_updates"] = (
            capo_dynamodb.types.global_secondary_index_update_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexUpdates"]
            )
        )
    if data.get("StreamSpecification") is not None:
        import capo_dynamodb.types.stream_specification

        out["stream_specification"] = (
            capo_dynamodb.types.stream_specification.deserialize_aws_json_1_0(
                data["StreamSpecification"]
            )
        )
    if data.get("SSESpecification") is not None:
        import capo_dynamodb.types.sse_specification

        out["sse_specification"] = (
            capo_dynamodb.types.sse_specification.deserialize_aws_json_1_0(
                data["SSESpecification"]
            )
        )
    if data.get("ReplicaUpdates") is not None:
        import capo_dynamodb.types.replication_group_update_list

        out["replica_updates"] = (
            capo_dynamodb.types.replication_group_update_list.deserialize_aws_json_1_0(
                data["ReplicaUpdates"]
            )
        )
    if data.get("TableClass") is not None:
        import capo_dynamodb.types.table_class

        out["table_class"] = capo_dynamodb.types.table_class.deserialize_aws_json_1_0(
            data["TableClass"]
        )
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if data.get("MultiRegionConsistency") is not None:
        import capo_dynamodb.types.multi_region_consistency

        out["multi_region_consistency"] = (
            capo_dynamodb.types.multi_region_consistency.deserialize_aws_json_1_0(
                data["MultiRegionConsistency"]
            )
        )
    if data.get("GlobalTableWitnessUpdates") is not None:
        import capo_dynamodb.types.global_table_witness_group_update_list

        out["global_table_witness_updates"] = (
            capo_dynamodb.types.global_table_witness_group_update_list.deserialize_aws_json_1_0(
                data["GlobalTableWitnessUpdates"]
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
    if data.get("GlobalTableSettingsReplicationMode") is not None:
        import capo_dynamodb.types.global_table_settings_replication_mode

        out["global_table_settings_replication_mode"] = (
            capo_dynamodb.types.global_table_settings_replication_mode.deserialize_aws_json_1_0(
                data["GlobalTableSettingsReplicationMode"]
            )
        )
    if data.get("VectorIndexUpdates") is not None:
        import capo_dynamodb.types.vector_index_update_list

        out["vector_index_updates"] = (
            capo_dynamodb.types.vector_index_update_list.deserialize_aws_json_1_0(
                data["VectorIndexUpdates"]
            )
        )
    return out
