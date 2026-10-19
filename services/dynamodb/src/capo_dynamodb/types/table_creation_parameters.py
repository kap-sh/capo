"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableCreationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_definitions
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.global_secondary_index_list
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.sse_specification
    import capo_dynamodb.types.table_name
    import capo_dynamodb.types.vector_index_list


class TableCreationParameters(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_name.TableName"
    """<p> The name of the table created as part of the import operation. </p>"""
    attribute_definitions: (
        "capo_dynamodb.types.attribute_definitions.AttributeDefinitions"
    )
    """<p> The attributes of the table created as part of the import operation. </p>"""
    key_schema: "capo_dynamodb.types.key_schema.KeySchema"
    """<p> The primary key and option sort key of the table created as part of the import operation. </p>"""
    billing_mode: NotRequired["capo_dynamodb.types.billing_mode.BillingMode"]
    """<p> The billing mode for provisioning the table created as part of the import operation. </p>"""
    provisioned_throughput: NotRequired[
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    sse_specification: NotRequired[
        "capo_dynamodb.types.sse_specification.SSESpecification"
    ]
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
    ]
    """<p> The Global Secondary Indexes (GSI) of the table to be created as part of the import operation. </p>"""
    vector_indexes: NotRequired["capo_dynamodb.types.vector_index_list.VectorIndexList"]
    """<p>The vector indexes of the table to be created as part of the import operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableCreationParameters) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import capo_dynamodb.types.attribute_definitions

    out["AttributeDefinitions"] = (
        capo_dynamodb.types.attribute_definitions.serialize_aws_json_1_0(
            value["attribute_definitions"]
        )
    )
    import capo_dynamodb.types.key_schema

    out["KeySchema"] = capo_dynamodb.types.key_schema.serialize_aws_json_1_0(
        value["key_schema"]
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
    if "on_demand_throughput" in value:
        import capo_dynamodb.types.on_demand_throughput

        out["OnDemandThroughput"] = (
            capo_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput"]
            )
        )
    if "sse_specification" in value:
        import capo_dynamodb.types.sse_specification

        out["SSESpecification"] = (
            capo_dynamodb.types.sse_specification.serialize_aws_json_1_0(
                value["sse_specification"]
            )
        )
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.global_secondary_index_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
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


def deserialize_aws_json_1_0(data: dict) -> TableCreationParameters:
    out: TableCreationParameters = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("AttributeDefinitions") is not None:
        import capo_dynamodb.types.attribute_definitions

        out["attribute_definitions"] = (
            capo_dynamodb.types.attribute_definitions.deserialize_aws_json_1_0(
                data["AttributeDefinitions"]
            )
        )
    else:
        out["attribute_definitions"] = []
    if data.get("KeySchema") is not None:
        import capo_dynamodb.types.key_schema

        out["key_schema"] = capo_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    else:
        out["key_schema"] = []
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
    if data.get("OnDemandThroughput") is not None:
        import capo_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            capo_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if data.get("SSESpecification") is not None:
        import capo_dynamodb.types.sse_specification

        out["sse_specification"] = (
            capo_dynamodb.types.sse_specification.deserialize_aws_json_1_0(
                data["SSESpecification"]
            )
        )
    if data.get("GlobalSecondaryIndexes") is not None:
        import capo_dynamodb.types.global_secondary_index_list

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.global_secondary_index_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
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
