"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dynamo_db_table_attribute_definition_list
    import capo_securityhub.types.aws_dynamo_db_table_billing_mode_summary
    import capo_securityhub.types.aws_dynamo_db_table_global_secondary_index_list
    import capo_securityhub.types.aws_dynamo_db_table_key_schema_list
    import capo_securityhub.types.aws_dynamo_db_table_local_secondary_index_list
    import capo_securityhub.types.aws_dynamo_db_table_provisioned_throughput
    import capo_securityhub.types.aws_dynamo_db_table_replica_list
    import capo_securityhub.types.aws_dynamo_db_table_restore_summary
    import capo_securityhub.types.aws_dynamo_db_table_sse_description
    import capo_securityhub.types.aws_dynamo_db_table_stream_specification
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.size_bytes


class AwsDynamoDbTableDetails(TypedDict, closed=True):
    attribute_definitions: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_attribute_definition_list.AwsDynamoDbTableAttributeDefinitionList"
    ]
    """<p>A list of attribute definitions for the table.</p>"""
    billing_mode_summary: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_billing_mode_summary.AwsDynamoDbTableBillingModeSummary"
    ]
    """<p>Information about the billing for read/write capacity on the table.</p>"""
    creation_date_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the table was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    global_secondary_indexes: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_global_secondary_index_list.AwsDynamoDbTableGlobalSecondaryIndexList"
    ]
    """<p>List of global secondary indexes for the table.</p>"""
    global_table_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of global tables being used.</p>"""
    item_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of items in the table.</p>"""
    key_schema: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_key_schema_list.AwsDynamoDbTableKeySchemaList"
    ]
    """<p>The primary key structure for the table.</p>"""
    latest_stream_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the latest stream for the table.</p>"""
    latest_stream_label: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The label of the latest stream. The label is not a unique identifier.</p>"""
    local_secondary_indexes: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_local_secondary_index_list.AwsDynamoDbTableLocalSecondaryIndexList"
    ]
    """<p>The list of local secondary indexes for the table.</p>"""
    provisioned_throughput: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_provisioned_throughput.AwsDynamoDbTableProvisionedThroughput"
    ]
    """<p>Information about the provisioned throughput for the table.</p>"""
    replicas: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_replica_list.AwsDynamoDbTableReplicaList"
    ]
    """<p>The list of replicas of this table.</p>"""
    restore_summary: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_restore_summary.AwsDynamoDbTableRestoreSummary"
    ]
    """<p>Information about the restore for the table.</p>"""
    sse_description: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_sse_description.AwsDynamoDbTableSseDescription"
    ]
    """<p>Information about the server-side encryption for the table.</p>"""
    stream_specification: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_stream_specification.AwsDynamoDbTableStreamSpecification"
    ]
    """<p>The current DynamoDB Streams configuration for the table.</p>"""
    table_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the table.</p>"""
    table_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the table.</p>"""
    table_size_bytes: NotRequired["capo_securityhub.types.size_bytes.SizeBytes"]
    """<p>The total size of the table in bytes.</p>"""
    table_status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current status of the table. Valid values are as follows:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>ARCHIVED</code> </p> </li> <li> <p> <code>ARCHIVING</code> </p> </li> <li> <p> <code>CREATING</code> </p> </li> <li> <p> <code>DELETING</code> </p> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_CREDENTIALS</code> </p> </li> <li> <p> <code>UPDATING</code> </p> </li> </ul>"""
    deletion_protection_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableDetails) -> dict:
    out: dict = {}
    if "attribute_definitions" in value:
        import capo_securityhub.types.aws_dynamo_db_table_attribute_definition_list

        out["AttributeDefinitions"] = (
            capo_securityhub.types.aws_dynamo_db_table_attribute_definition_list.serialize_json(
                value["attribute_definitions"]
            )
        )
    if "billing_mode_summary" in value:
        import capo_securityhub.types.aws_dynamo_db_table_billing_mode_summary

        out["BillingModeSummary"] = (
            capo_securityhub.types.aws_dynamo_db_table_billing_mode_summary.serialize_json(
                value["billing_mode_summary"]
            )
        )
    if "creation_date_time" in value:
        out["CreationDateTime"] = value["creation_date_time"]
    if "global_secondary_indexes" in value:
        import capo_securityhub.types.aws_dynamo_db_table_global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            capo_securityhub.types.aws_dynamo_db_table_global_secondary_index_list.serialize_json(
                value["global_secondary_indexes"]
            )
        )
    if "global_table_version" in value:
        out["GlobalTableVersion"] = value["global_table_version"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "key_schema" in value:
        import capo_securityhub.types.aws_dynamo_db_table_key_schema_list

        out["KeySchema"] = (
            capo_securityhub.types.aws_dynamo_db_table_key_schema_list.serialize_json(
                value["key_schema"]
            )
        )
    if "latest_stream_arn" in value:
        out["LatestStreamArn"] = value["latest_stream_arn"]
    if "latest_stream_label" in value:
        out["LatestStreamLabel"] = value["latest_stream_label"]
    if "local_secondary_indexes" in value:
        import capo_securityhub.types.aws_dynamo_db_table_local_secondary_index_list

        out["LocalSecondaryIndexes"] = (
            capo_securityhub.types.aws_dynamo_db_table_local_secondary_index_list.serialize_json(
                value["local_secondary_indexes"]
            )
        )
    if "provisioned_throughput" in value:
        import capo_securityhub.types.aws_dynamo_db_table_provisioned_throughput

        out["ProvisionedThroughput"] = (
            capo_securityhub.types.aws_dynamo_db_table_provisioned_throughput.serialize_json(
                value["provisioned_throughput"]
            )
        )
    if "replicas" in value:
        import capo_securityhub.types.aws_dynamo_db_table_replica_list

        out["Replicas"] = (
            capo_securityhub.types.aws_dynamo_db_table_replica_list.serialize_json(
                value["replicas"]
            )
        )
    if "restore_summary" in value:
        import capo_securityhub.types.aws_dynamo_db_table_restore_summary

        out["RestoreSummary"] = (
            capo_securityhub.types.aws_dynamo_db_table_restore_summary.serialize_json(
                value["restore_summary"]
            )
        )
    if "sse_description" in value:
        import capo_securityhub.types.aws_dynamo_db_table_sse_description

        out["SseDescription"] = (
            capo_securityhub.types.aws_dynamo_db_table_sse_description.serialize_json(
                value["sse_description"]
            )
        )
    if "stream_specification" in value:
        import capo_securityhub.types.aws_dynamo_db_table_stream_specification

        out["StreamSpecification"] = (
            capo_securityhub.types.aws_dynamo_db_table_stream_specification.serialize_json(
                value["stream_specification"]
            )
        )
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "table_size_bytes" in value:
        out["TableSizeBytes"] = value["table_size_bytes"]
    if "table_status" in value:
        out["TableStatus"] = value["table_status"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableDetails:
    out: AwsDynamoDbTableDetails = {}  # type: ignore[typeddict-item]
    if data.get("AttributeDefinitions") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_attribute_definition_list

        out["attribute_definitions"] = (
            capo_securityhub.types.aws_dynamo_db_table_attribute_definition_list.deserialize_json(
                data["AttributeDefinitions"]
            )
        )
    if data.get("BillingModeSummary") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_billing_mode_summary

        out["billing_mode_summary"] = (
            capo_securityhub.types.aws_dynamo_db_table_billing_mode_summary.deserialize_json(
                data["BillingModeSummary"]
            )
        )
    if data.get("CreationDateTime") is not None:
        out["creation_date_time"] = data["CreationDateTime"]
    if data.get("GlobalSecondaryIndexes") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_global_secondary_index_list

        out["global_secondary_indexes"] = (
            capo_securityhub.types.aws_dynamo_db_table_global_secondary_index_list.deserialize_json(
                data["GlobalSecondaryIndexes"]
            )
        )
    if data.get("GlobalTableVersion") is not None:
        out["global_table_version"] = data["GlobalTableVersion"]
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    if data.get("KeySchema") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_key_schema_list

        out["key_schema"] = (
            capo_securityhub.types.aws_dynamo_db_table_key_schema_list.deserialize_json(
                data["KeySchema"]
            )
        )
    if data.get("LatestStreamArn") is not None:
        out["latest_stream_arn"] = data["LatestStreamArn"]
    if data.get("LatestStreamLabel") is not None:
        out["latest_stream_label"] = data["LatestStreamLabel"]
    if data.get("LocalSecondaryIndexes") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_local_secondary_index_list

        out["local_secondary_indexes"] = (
            capo_securityhub.types.aws_dynamo_db_table_local_secondary_index_list.deserialize_json(
                data["LocalSecondaryIndexes"]
            )
        )
    if data.get("ProvisionedThroughput") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_provisioned_throughput

        out["provisioned_throughput"] = (
            capo_securityhub.types.aws_dynamo_db_table_provisioned_throughput.deserialize_json(
                data["ProvisionedThroughput"]
            )
        )
    if data.get("Replicas") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_replica_list

        out["replicas"] = (
            capo_securityhub.types.aws_dynamo_db_table_replica_list.deserialize_json(
                data["Replicas"]
            )
        )
    if data.get("RestoreSummary") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_restore_summary

        out["restore_summary"] = (
            capo_securityhub.types.aws_dynamo_db_table_restore_summary.deserialize_json(
                data["RestoreSummary"]
            )
        )
    if data.get("SseDescription") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_sse_description

        out["sse_description"] = (
            capo_securityhub.types.aws_dynamo_db_table_sse_description.deserialize_json(
                data["SseDescription"]
            )
        )
    if data.get("StreamSpecification") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_stream_specification

        out["stream_specification"] = (
            capo_securityhub.types.aws_dynamo_db_table_stream_specification.deserialize_json(
                data["StreamSpecification"]
            )
        )
    if data.get("TableId") is not None:
        out["table_id"] = data["TableId"]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("TableSizeBytes") is not None:
        out["table_size_bytes"] = data["TableSizeBytes"]
    if data.get("TableStatus") is not None:
        out["table_status"] = data["TableStatus"]
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    return out
