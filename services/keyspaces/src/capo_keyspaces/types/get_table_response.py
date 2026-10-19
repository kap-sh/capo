"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.capacity_specification_summary
    import capo_keyspaces.types.cdc_specification_summary
    import capo_keyspaces.types.client_side_timestamps
    import capo_keyspaces.types.comment
    import capo_keyspaces.types.default_time_to_live
    import capo_keyspaces.types.encryption_specification
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.point_in_time_recovery_summary
    import capo_keyspaces.types.replica_specification_summary_list
    import capo_keyspaces.types.schema_definition
    import capo_keyspaces.types.stream_arn
    import capo_keyspaces.types.table_name
    import capo_keyspaces.types.table_status
    import capo_keyspaces.types.time_to_live
    import capo_keyspaces.types.timestamp
    import capo_keyspaces.types.warm_throughput_specification_summary


class GetTableResponse(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace that the specified table is stored in.</p>"""
    table_name: "capo_keyspaces.types.table_name.TableName"
    """<p>The name of the specified table.</p>"""
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the specified table.</p>"""
    creation_timestamp: NotRequired["capo_keyspaces.types.timestamp.Timestamp"]
    """<p>The creation timestamp of the specified table.</p>"""
    status: NotRequired["capo_keyspaces.types.table_status.TableStatus"]
    """<p>The current status of the specified table.</p>"""
    schema_definition: NotRequired[
        "capo_keyspaces.types.schema_definition.SchemaDefinition"
    ]
    """<p>The schema definition of the specified table.</p>"""
    capacity_specification: NotRequired[
        "capo_keyspaces.types.capacity_specification_summary.CapacitySpecificationSummary"
    ]
    """<p>The read/write throughput capacity mode for a table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> </p> </li> </ul>"""
    encryption_specification: NotRequired[
        "capo_keyspaces.types.encryption_specification.EncryptionSpecification"
    ]
    """<p>The encryption settings of the specified table.</p>"""
    point_in_time_recovery: NotRequired[
        "capo_keyspaces.types.point_in_time_recovery_summary.PointInTimeRecoverySummary"
    ]
    """<p>The point-in-time recovery status of the specified table.</p>"""
    ttl: NotRequired["capo_keyspaces.types.time_to_live.TimeToLive"]
    """<p>The custom Time to Live settings of the specified table.</p>"""
    default_time_to_live: NotRequired[
        "capo_keyspaces.types.default_time_to_live.DefaultTimeToLive"
    ]
    """<p>The default Time to Live settings in seconds of the specified table.</p>"""
    comment: NotRequired["capo_keyspaces.types.comment.Comment"]
    """<p>The the description of the specified table.</p>"""
    client_side_timestamps: NotRequired[
        "capo_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
    ]
    """<p> The client-side timestamps setting of the table.</p>"""
    replica_specifications: NotRequired[
        "capo_keyspaces.types.replica_specification_summary_list.ReplicaSpecificationSummaryList"
    ]
    """<p>Returns the Amazon Web Services Region specific settings of all Regions a multi-Region table is replicated in.</p>"""
    latest_stream_arn: NotRequired["capo_keyspaces.types.stream_arn.StreamArn"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    cdc_specification: NotRequired[
        "capo_keyspaces.types.cdc_specification_summary.CdcSpecificationSummary"
    ]
    """<p>The CDC stream settings of the table.</p>"""
    warm_throughput_specification: NotRequired[
        "capo_keyspaces.types.warm_throughput_specification_summary.WarmThroughputSpecificationSummary"
    ]
    """<p>The warm throughput settings for the table, including the current status and configured read and write capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTableResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["resourceArn"] = value["resource_arn"]
    if "creation_timestamp" in value:
        import capo_keyspaces.types.timestamp

        out["creationTimestamp"] = (
            capo_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["creation_timestamp"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "schema_definition" in value:
        import capo_keyspaces.types.schema_definition

        out["schemaDefinition"] = (
            capo_keyspaces.types.schema_definition.serialize_aws_json_1_0(
                value["schema_definition"]
            )
        )
    if "capacity_specification" in value:
        import capo_keyspaces.types.capacity_specification_summary

        out["capacitySpecification"] = (
            capo_keyspaces.types.capacity_specification_summary.serialize_aws_json_1_0(
                value["capacity_specification"]
            )
        )
    if "encryption_specification" in value:
        import capo_keyspaces.types.encryption_specification

        out["encryptionSpecification"] = (
            capo_keyspaces.types.encryption_specification.serialize_aws_json_1_0(
                value["encryption_specification"]
            )
        )
    if "point_in_time_recovery" in value:
        import capo_keyspaces.types.point_in_time_recovery_summary

        out["pointInTimeRecovery"] = (
            capo_keyspaces.types.point_in_time_recovery_summary.serialize_aws_json_1_0(
                value["point_in_time_recovery"]
            )
        )
    if "ttl" in value:
        import capo_keyspaces.types.time_to_live

        out["ttl"] = capo_keyspaces.types.time_to_live.serialize_aws_json_1_0(
            value["ttl"]
        )
    if "default_time_to_live" in value:
        out["defaultTimeToLive"] = value["default_time_to_live"]
    if "comment" in value:
        import capo_keyspaces.types.comment

        out["comment"] = capo_keyspaces.types.comment.serialize_aws_json_1_0(
            value["comment"]
        )
    if "client_side_timestamps" in value:
        import capo_keyspaces.types.client_side_timestamps

        out["clientSideTimestamps"] = (
            capo_keyspaces.types.client_side_timestamps.serialize_aws_json_1_0(
                value["client_side_timestamps"]
            )
        )
    if "replica_specifications" in value:
        import capo_keyspaces.types.replica_specification_summary_list

        out["replicaSpecifications"] = (
            capo_keyspaces.types.replica_specification_summary_list.serialize_aws_json_1_0(
                value["replica_specifications"]
            )
        )
    if "latest_stream_arn" in value:
        out["latestStreamArn"] = value["latest_stream_arn"]
    if "cdc_specification" in value:
        import capo_keyspaces.types.cdc_specification_summary

        out["cdcSpecification"] = (
            capo_keyspaces.types.cdc_specification_summary.serialize_aws_json_1_0(
                value["cdc_specification"]
            )
        )
    if "warm_throughput_specification" in value:
        import capo_keyspaces.types.warm_throughput_specification_summary

        out["warmThroughputSpecification"] = (
            capo_keyspaces.types.warm_throughput_specification_summary.serialize_aws_json_1_0(
                value["warm_throughput_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTableResponse:
    out: GetTableResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("creationTimestamp") is not None:
        import capo_keyspaces.types.timestamp

        out["creation_timestamp"] = (
            capo_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["creationTimestamp"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("schemaDefinition") is not None:
        import capo_keyspaces.types.schema_definition

        out["schema_definition"] = (
            capo_keyspaces.types.schema_definition.deserialize_aws_json_1_0(
                data["schemaDefinition"]
            )
        )
    if data.get("capacitySpecification") is not None:
        import capo_keyspaces.types.capacity_specification_summary

        out["capacity_specification"] = (
            capo_keyspaces.types.capacity_specification_summary.deserialize_aws_json_1_0(
                data["capacitySpecification"]
            )
        )
    if data.get("encryptionSpecification") is not None:
        import capo_keyspaces.types.encryption_specification

        out["encryption_specification"] = (
            capo_keyspaces.types.encryption_specification.deserialize_aws_json_1_0(
                data["encryptionSpecification"]
            )
        )
    if data.get("pointInTimeRecovery") is not None:
        import capo_keyspaces.types.point_in_time_recovery_summary

        out["point_in_time_recovery"] = (
            capo_keyspaces.types.point_in_time_recovery_summary.deserialize_aws_json_1_0(
                data["pointInTimeRecovery"]
            )
        )
    if data.get("ttl") is not None:
        import capo_keyspaces.types.time_to_live

        out["ttl"] = capo_keyspaces.types.time_to_live.deserialize_aws_json_1_0(
            data["ttl"]
        )
    if data.get("defaultTimeToLive") is not None:
        out["default_time_to_live"] = data["defaultTimeToLive"]
    if data.get("comment") is not None:
        import capo_keyspaces.types.comment

        out["comment"] = capo_keyspaces.types.comment.deserialize_aws_json_1_0(
            data["comment"]
        )
    if data.get("clientSideTimestamps") is not None:
        import capo_keyspaces.types.client_side_timestamps

        out["client_side_timestamps"] = (
            capo_keyspaces.types.client_side_timestamps.deserialize_aws_json_1_0(
                data["clientSideTimestamps"]
            )
        )
    if data.get("replicaSpecifications") is not None:
        import capo_keyspaces.types.replica_specification_summary_list

        out["replica_specifications"] = (
            capo_keyspaces.types.replica_specification_summary_list.deserialize_aws_json_1_0(
                data["replicaSpecifications"]
            )
        )
    if data.get("latestStreamArn") is not None:
        out["latest_stream_arn"] = data["latestStreamArn"]
    if data.get("cdcSpecification") is not None:
        import capo_keyspaces.types.cdc_specification_summary

        out["cdc_specification"] = (
            capo_keyspaces.types.cdc_specification_summary.deserialize_aws_json_1_0(
                data["cdcSpecification"]
            )
        )
    if data.get("warmThroughputSpecification") is not None:
        import capo_keyspaces.types.warm_throughput_specification_summary

        out["warm_throughput_specification"] = (
            capo_keyspaces.types.warm_throughput_specification_summary.deserialize_aws_json_1_0(
                data["warmThroughputSpecification"]
            )
        )
    return out
