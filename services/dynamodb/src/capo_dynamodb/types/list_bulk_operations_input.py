"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListBulkOperationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_next_token
    import capo_dynamodb.types.list_bulk_operations_max_limit


class ListBulkOperationsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_dynamodb.types.list_bulk_operations_max_limit.ListBulkOperationsMaxLimit"
    ]
    """<p>The maximum number of bulk operation summaries to return in one page. If you don't specify a value, DynamoDB uses 10.</p>"""
    next_token: NotRequired[
        "capo_dynamodb.types.bulk_operation_next_token.BulkOperationNextToken"
    ]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to <code>ListBulkOperations</code>. When provided in this manner, the API fetches the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBulkOperationsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBulkOperationsInput:
    out: ListBulkOperationsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
