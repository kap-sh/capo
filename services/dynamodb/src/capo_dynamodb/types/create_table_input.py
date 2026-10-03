"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_definitions
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.deletion_protection_enabled
    import capo_dynamodb.types.global_secondary_index_list
    import capo_dynamodb.types.global_table_settings_replication_mode
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.local_secondary_index_list
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.resource_policy
    import capo_dynamodb.types.sse_specification
    import capo_dynamodb.types.stream_specification
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_class
    import capo_dynamodb.types.tag_list
    import capo_dynamodb.types.vector_index_list
    import capo_dynamodb.types.warm_throughput


class CreateTableInput(TypedDict, closed=True):
    attribute_definitions: NotRequired[
        "capo_dynamodb.types.attribute_definitions.AttributeDefinitions"
    ]
    """<p>An array of attributes that describe the key schema for the table and indexes.</p>"""
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to create. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    key_schema: NotRequired["capo_dynamodb.types.key_schema.KeySchema"]
    """<p>Specifies the attributes that make up the primary key for a table or an index. The attributes in <code>KeySchema</code> must also be defined in the <code>AttributeDefinitions</code> array. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html">Data Model</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>Each <code>KeySchemaElement</code> in the array is composed of:</p> <ul> <li> <p> <code>AttributeName</code> - The name of this key attribute.</p> </li> <li> <p> <code>KeyType</code> - The role that the key attribute will assume:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term "hash attribute" derives from the DynamoDB usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note> <p>For a simple primary key (partition key), you must provide exactly one element with a <code>KeyType</code> of <code>HASH</code>.</p> <p>For a composite primary key (partition key and sort key), you must provide exactly two elements, in this order: The first element must have a <code>KeyType</code> of <code>HASH</code>, and the second element must have a <code>KeyType</code> of <code>RANGE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#WorkingWithTables.primary.key">Working with Tables</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    local_secondary_indexes: NotRequired[
        "capo_dynamodb.types.local_secondary_index_list.LocalSecondaryIndexList"
    ]
    """<p>One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained.</p> <p>Each local secondary index in the array includes the following:</p> <ul> <li> <p> <code>IndexName</code> - The name of the local secondary index. Must be unique only for this table.</p> <p></p> </li> <li> <p> <code>KeySchema</code> - Specifies the key schema for the local secondary index. The key schema must begin with the same partition key as the table.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:</p> <ul> <li> <p> <code>ProjectionType</code> - One of the following:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - Only the specified table attributes are projected into the index. The list of projected attributes is in <code>NonKeyAttributes</code>.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> </li> <li> <p> <code>NonKeyAttributes</code> - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in <code>NonKeyAttributes</code>, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p> </li> </ul> </li> </ul>"""
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
    ]
    """<p>One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following:</p> <ul> <li> <p> <code>IndexName</code> - The name of the global secondary index. Must be unique only for this table.</p> <p></p> </li> <li> <p> <code>KeySchema</code> - Specifies the key schema for the global secondary index. Each global secondary index supports up to 4 partition keys and up to 4 sort keys.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:</p> <ul> <li> <p> <code>ProjectionType</code> - One of the following:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - Only the specified table attributes are projected into the index. The list of projected attributes is in <code>NonKeyAttributes</code>.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> </li> <li> <p> <code>NonKeyAttributes</code> - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in <code>NonKeyAttributes</code>, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p> </li> </ul> </li> <li> <p> <code>ProvisionedThroughput</code> - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units.</p> </li> </ul>"""
    billing_mode: NotRequired["capo_dynamodb.types.billing_mode.BillingMode"]
    """<p>Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.</p> <ul> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for most DynamoDB workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html">On-demand capacity mode</a>. </p> </li> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for steady workloads with predictable growth where capacity requirements can be reliably forecasted. <code>PROVISIONED</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">Provisioned capacity mode</a>.</p> </li> </ul>"""
    provisioned_throughput: NotRequired[
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the <code>UpdateTable</code> operation.</p> <p> If you set BillingMode as <code>PROVISIONED</code>, you must specify this property. If you set BillingMode as <code>PAY_PER_REQUEST</code>, you cannot specify this property.</p> <p>For current minimum and maximum provisioned throughput values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    stream_specification: NotRequired[
        "capo_dynamodb.types.stream_specification.StreamSpecification"
    ]
    """<p>The settings for DynamoDB Streams on the table. These settings consist of:</p> <ul> <li> <p> <code>StreamEnabled</code> - Indicates whether DynamoDB Streams is to be enabled (true) or disabled (false).</p> </li> <li> <p> <code>StreamViewType</code> - When an item in the table is modified, <code>StreamViewType</code> determines what information is written to the table's stream. Valid values for <code>StreamViewType</code> are:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the key attributes of the modified item are written to the stream.</p> </li> <li> <p> <code>NEW_IMAGE</code> - The entire item, as it appears after it was modified, is written to the stream.</p> </li> <li> <p> <code>OLD_IMAGE</code> - The entire item, as it appeared before it was modified, is written to the stream.</p> </li> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - Both the new and the old item images of the item are written to the stream.</p> </li> </ul> </li> </ul>"""
    sse_specification: NotRequired[
        "capo_dynamodb.types.sse_specification.SSESpecification"
    ]
    """<p>Represents the settings used to enable server-side encryption.</p>"""
    tags: NotRequired["capo_dynamodb.types.tag_list.TagList"]
    """<p>A list of key-value pairs to label the table. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html">Tagging for DynamoDB</a>.</p>"""
    table_class: NotRequired["capo_dynamodb.types.table_class.TableClass"]
    """<p>The table class of the new table. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</p>"""
    deletion_protection_enabled: NotRequired[
        "capo_dynamodb.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.</p>"""
    warm_throughput: NotRequired["capo_dynamodb.types.warm_throughput.WarmThroughput"]
    """<p>Represents the warm throughput (in read units per second and write units per second) for creating a table.</p>"""
    resource_policy: NotRequired["capo_dynamodb.types.resource_policy.ResourcePolicy"]
    """<p>An Amazon Web Services resource-based policy document in JSON format that will be attached to the table.</p> <p>When you attach a resource-based policy while creating a table, the policy application is <i>strongly consistent</i>.</p> <p>The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit. For a full list of all considerations that apply for resource-based policies, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html">Resource-based policy considerations</a>.</p> <note> <p>You need to specify the <code>CreateTable</code> and <code>PutResourcePolicy</code> IAM actions for authorizing a user to create a table with a resource-based policy.</p> </note>"""
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>Sets the maximum number of read and write units for the specified table in on-demand capacity mode. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>"""
    global_table_source_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The Amazon Resource Name (ARN) of the source table used for the creation of a multi-account global table.</p>"""
    global_table_settings_replication_mode: NotRequired[
        "capo_dynamodb.types.global_table_settings_replication_mode.GlobalTableSettingsReplicationMode"
    ]
    """<p>Controls the settings synchronization mode for the global table. For multi-account global tables, this parameter is required and the only supported value is ENABLED. For same-account global tables, this parameter is set to ENABLED_WITH_OVERRIDES. </p>"""
    vector_indexes: NotRequired["capo_dynamodb.types.vector_index_list.VectorIndexList"]
    """<p>One or more vector indexes to be created on the table. Each vector index enables similarity search on a vector attribute. Each element in the list consists of:</p> <ul> <li> <p> <code>IndexName</code> - The name of the vector index. Must be unique within the table.</p> </li> <li> <p> <code>VectorAttribute</code> - The attribute that contains vector embeddings. If multiple vector indexes reference the same attribute, they must all use the same number of dimensions.</p> </li> <li> <p> <code>Dimensions</code> - The number of dimensions in each vector.</p> </li> <li> <p> <code>DistanceFunction</code> - The distance function used to calculate similarity. Valid values: <code>COSINE</code>, <code>EUCLIDEAN</code>, <code>DOT_PRODUCT</code>.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the vector index. The total number of projected non-key attributes is shared across the vector attribute (counts as 1) and <code>INLINE_FILTER</code> search schema elements (each counts as 1). <code>HASH</code> search schema elements do not count toward this limit.</p> </li> <li> <p> <code>SearchSchema</code> - (Optional) Defines the partition key (<code>HASH</code>) and inline filter (<code>INLINE_FILTER</code>) attributes for the vector index.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTableInput) -> dict:
    out: dict = {}
    if "attribute_definitions" in value:
        import capo_dynamodb.types.attribute_definitions

        out["AttributeDefinitions"] = (
            capo_dynamodb.types.attribute_definitions.serialize_aws_json_1_0(
                value["attribute_definitions"]
            )
        )
    out["TableName"] = value["table_name"]
    if "key_schema" in value:
        import capo_dynamodb.types.key_schema

        out["KeySchema"] = capo_dynamodb.types.key_schema.serialize_aws_json_1_0(
            value["key_schema"]
        )
    if "local_secondary_indexes" in value:
        import capo_dynamodb.types.local_secondary_index_list

        out["LocalSecondaryIndexes"] = (
            capo_dynamodb.types.local_secondary_index_list.serialize_aws_json_1_0(
                value["local_secondary_indexes"]
            )
        )
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.global_secondary_index_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
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
    if "tags" in value:
        import capo_dynamodb.types.tag_list

        out["Tags"] = capo_dynamodb.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "table_class" in value:
        import capo_dynamodb.types.table_class

        out["TableClass"] = capo_dynamodb.types.table_class.serialize_aws_json_1_0(
            value["table_class"]
        )
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "warm_throughput" in value:
        import capo_dynamodb.types.warm_throughput

        out["WarmThroughput"] = (
            capo_dynamodb.types.warm_throughput.serialize_aws_json_1_0(
                value["warm_throughput"]
            )
        )
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "on_demand_throughput" in value:
        import capo_dynamodb.types.on_demand_throughput

        out["OnDemandThroughput"] = (
            capo_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput"]
            )
        )
    if "global_table_source_arn" in value:
        out["GlobalTableSourceArn"] = value["global_table_source_arn"]
    if "global_table_settings_replication_mode" in value:
        import capo_dynamodb.types.global_table_settings_replication_mode

        out["GlobalTableSettingsReplicationMode"] = (
            capo_dynamodb.types.global_table_settings_replication_mode.serialize_aws_json_1_0(
                value["global_table_settings_replication_mode"]
            )
        )
    if "vector_indexes" in value:
        import capo_dynamodb.types.vector_index_list

        out["VectorIndexes"] = (
            capo_dynamodb.types.vector_index_list.serialize_aws_json_1_0(
                value["vector_indexes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTableInput:
    out: CreateTableInput = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CreateTableInput.table_name required")
    if data.get("KeySchema") is not None:
        import capo_dynamodb.types.key_schema

        out["key_schema"] = capo_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    if data.get("LocalSecondaryIndexes") is not None:
        import capo_dynamodb.types.local_secondary_index_list

        out["local_secondary_indexes"] = (
            capo_dynamodb.types.local_secondary_index_list.deserialize_aws_json_1_0(
                data["LocalSecondaryIndexes"]
            )
        )
    if data.get("GlobalSecondaryIndexes") is not None:
        import capo_dynamodb.types.global_secondary_index_list

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.global_secondary_index_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
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
    if data.get("Tags") is not None:
        import capo_dynamodb.types.tag_list

        out["tags"] = capo_dynamodb.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("TableClass") is not None:
        import capo_dynamodb.types.table_class

        out["table_class"] = capo_dynamodb.types.table_class.deserialize_aws_json_1_0(
            data["TableClass"]
        )
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if data.get("WarmThroughput") is not None:
        import capo_dynamodb.types.warm_throughput

        out["warm_throughput"] = (
            capo_dynamodb.types.warm_throughput.deserialize_aws_json_1_0(
                data["WarmThroughput"]
            )
        )
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    if data.get("OnDemandThroughput") is not None:
        import capo_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            capo_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if data.get("GlobalTableSourceArn") is not None:
        out["global_table_source_arn"] = data["GlobalTableSourceArn"]
    if data.get("GlobalTableSettingsReplicationMode") is not None:
        import capo_dynamodb.types.global_table_settings_replication_mode

        out["global_table_settings_replication_mode"] = (
            capo_dynamodb.types.global_table_settings_replication_mode.deserialize_aws_json_1_0(
                data["GlobalTableSettingsReplicationMode"]
            )
        )
    if data.get("VectorIndexes") is not None:
        import capo_dynamodb.types.vector_index_list

        out["vector_indexes"] = (
            capo_dynamodb.types.vector_index_list.deserialize_aws_json_1_0(
                data["VectorIndexes"]
            )
        )
    return out
