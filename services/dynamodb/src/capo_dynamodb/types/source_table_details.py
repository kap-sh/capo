"""Generated from Smithy shape ``com.amazonaws.dynamodb#SourceTableDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.item_count
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.long_object
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_creation_date_time
    import capo_dynamodb.types.table_id
    import capo_dynamodb.types.table_name


class SourceTableDetails(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The name of the table for which the backup was created. </p>"""
    table_id: "capo_dynamodb.types.table_id.TableId"
    """<p>Unique identifier for the table for which the backup was created. </p>"""
    table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>ARN of the table for which backup was created. </p>"""
    table_size_bytes: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>Size of the table in bytes. Note that this is an approximate value.</p>"""
    key_schema: "capo_dynamodb.types.key_schema.KeySchema"
    """<p>Schema of the table. </p>"""
    table_creation_date_time: (
        "capo_dynamodb.types.table_creation_date_time.TableCreationDateTime"
    )
    """<p>Time when the source table was created. </p>"""
    provisioned_throughput: (
        "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    )
    """<p>Read IOPs and Write IOPS on the table when the backup was created.</p>"""
    on_demand_throughput: NotRequired[
        "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    item_count: NotRequired["capo_dynamodb.types.item_count.ItemCount"]
    """<p>Number of items in the table. Note that this is an approximate value. </p>"""
    billing_mode: NotRequired["capo_dynamodb.types.billing_mode.BillingMode"]
    """<p>Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.</p> <ul> <li> <p> <code>PROVISIONED</code> - Sets the read/write capacity mode to <code>PROVISIONED</code>. We recommend using <code>PROVISIONED</code> for predictable workloads.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - Sets the read/write capacity mode to <code>PAY_PER_REQUEST</code>. We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceTableDetails) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["TableId"] = value["table_id"]
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "table_size_bytes" in value:
        out["TableSizeBytes"] = value["table_size_bytes"]
    import capo_dynamodb.types.key_schema

    out["KeySchema"] = capo_dynamodb.types.key_schema.serialize_aws_json_1_0(
        value["key_schema"]
    )
    import capo_dynamodb.types.table_creation_date_time

    out["TableCreationDateTime"] = (
        capo_dynamodb.types.table_creation_date_time.serialize_aws_json_1_0(
            value["table_creation_date_time"]
        )
    )
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
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "billing_mode" in value:
        import capo_dynamodb.types.billing_mode

        out["BillingMode"] = capo_dynamodb.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceTableDetails:
    out: SourceTableDetails = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("TableId") is not None:
        out["table_id"] = data["TableId"]
    else:
        out["table_id"] = ""
    if data.get("TableArn") is not None:
        out["table_arn"] = data["TableArn"]
    if data.get("TableSizeBytes") is not None:
        out["table_size_bytes"] = data["TableSizeBytes"]
    if data.get("KeySchema") is not None:
        import capo_dynamodb.types.key_schema

        out["key_schema"] = capo_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    else:
        out["key_schema"] = []
    if data.get("TableCreationDateTime") is not None:
        import capo_dynamodb.types.table_creation_date_time

        out["table_creation_date_time"] = (
            capo_dynamodb.types.table_creation_date_time.deserialize_aws_json_1_0(
                data["TableCreationDateTime"]
            )
        )
    else:
        import datetime

        out["table_creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ProvisionedThroughput") is not None:
        import capo_dynamodb.types.provisioned_throughput

        out["provisioned_throughput"] = (
            capo_dynamodb.types.provisioned_throughput.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    else:
        raise DeserializationError("SourceTableDetails.provisioned_throughput required")
    if data.get("OnDemandThroughput") is not None:
        import capo_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            capo_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    if data.get("BillingMode") is not None:
        import capo_dynamodb.types.billing_mode

        out["billing_mode"] = capo_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
            data["BillingMode"]
        )
    return out
