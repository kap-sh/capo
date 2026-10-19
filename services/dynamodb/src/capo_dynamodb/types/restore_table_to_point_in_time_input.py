"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableToPointInTimeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.boolean_object
    import capo_dynamodb.types.date
    import capo_dynamodb.types.global_secondary_index_list
    import capo_dynamodb.types.local_secondary_index_list
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.sse_specification
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_name
    import capo_dynamodb.types.vector_index_list


class RestoreTableToPointInTimeInput(TypedDict, closed=True):
    source_table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The DynamoDB table that will be restored. This value is an Amazon Resource Name (ARN).</p>"""
    source_table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>Name of the source table that is being restored.</p>"""
    target_table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The name of the new table to which it must be restored to.</p>"""
    use_latest_restorable_time: NotRequired[
        "capo_dynamodb.types.boolean_object.BooleanObject"
    ]
    """<p>Restore the table to the latest possible time. <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. </p>"""
    restore_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>Time in the past to restore the table to.</p>"""
    billing_mode_override: NotRequired["capo_dynamodb.types.billing_mode.BillingMode"]
    """<p>The billing mode of the restored table.</p>"""
    global_secondary_index_override: NotRequired[
        "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
    ]
    """<p>List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p> <p>The <code>WarmThroughput</code> setting is not supported on global secondary indexes when you use <code>RestoreTableToPointInTime</code>. Although <code>WarmThroughput</code> appears in the shared index definition, including it in a <code>GlobalSecondaryIndexOverride</code> entry causes the request to fail with a validation error.</p>"""
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
    """<p>The vector indexes for the restored table. If not specified, all vector indexes from the source table are restored. The indexes provided must match existing vector indexes from the source table. You can choose to exclude some or all of the vector indexes at the time of restore.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreTableToPointInTimeInput) -> dict:
    out: dict = {}
    if "source_table_arn" in value:
        out["SourceTableArn"] = value["source_table_arn"]
    if "source_table_name" in value:
        out["SourceTableName"] = value["source_table_name"]
    out["TargetTableName"] = value["target_table_name"]
    if "use_latest_restorable_time" in value:
        out["UseLatestRestorableTime"] = value["use_latest_restorable_time"]
    if "restore_date_time" in value:
        import capo_dynamodb.types.date

        out["RestoreDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
            value["restore_date_time"]
        )
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


def deserialize_aws_json_1_0(data: dict) -> RestoreTableToPointInTimeInput:
    out: RestoreTableToPointInTimeInput = {}  # type: ignore[typeddict-item]
    if data.get("SourceTableArn") is not None:
        out["source_table_arn"] = data["SourceTableArn"]
    if data.get("SourceTableName") is not None:
        out["source_table_name"] = data["SourceTableName"]
    if data.get("TargetTableName") is not None:
        out["target_table_name"] = data["TargetTableName"]
    else:
        out["target_table_name"] = ""
    if data.get("UseLatestRestorableTime") is not None:
        out["use_latest_restorable_time"] = data["UseLatestRestorableTime"]
    if data.get("RestoreDateTime") is not None:
        import capo_dynamodb.types.date

        out["restore_date_time"] = capo_dynamodb.types.date.deserialize_aws_json_1_0(
            data["RestoreDateTime"]
        )
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
