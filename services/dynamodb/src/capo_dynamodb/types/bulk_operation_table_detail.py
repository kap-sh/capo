"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationTableDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_id


class BulkOperationTableDetail(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The name or ARN of the table associated with the bulk operation.</p>"""
    table_id: NotRequired["capo_dynamodb.types.table_id.TableId"]
    """<p>The unique identifier of the table associated with the bulk operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationTableDetail) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BulkOperationTableDetail:
    out: BulkOperationTableDetail = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("TableId") is not None:
        out["table_id"] = data["TableId"]
    return out
