"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListBulkOperationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_next_token
    import capo_dynamodb.types.bulk_operations_summary_list


class ListBulkOperationsOutput(TypedDict, closed=True):
    bulk_operations_summary_list: NotRequired[
        "capo_dynamodb.types.bulk_operations_summary_list.BulkOperationsSummaryList"
    ]
    """<p>A list of bulk operation summaries for the current Amazon Web Services account and Amazon Web Services Region.</p>"""
    next_token: NotRequired[
        "capo_dynamodb.types.bulk_operation_next_token.BulkOperationNextToken"
    ]
    """<p>If this value is returned, there are additional results to be displayed. To retrieve them, call <code>ListBulkOperations</code> again, with <code>NextToken</code> set to this value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBulkOperationsOutput) -> dict:
    out: dict = {}
    if "bulk_operations_summary_list" in value:
        import capo_dynamodb.types.bulk_operations_summary_list

        out["BulkOperationsSummaryList"] = (
            capo_dynamodb.types.bulk_operations_summary_list.serialize_aws_json_1_0(
                value["bulk_operations_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBulkOperationsOutput:
    out: ListBulkOperationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("BulkOperationsSummaryList") is not None:
        import capo_dynamodb.types.bulk_operations_summary_list

        out["bulk_operations_summary_list"] = (
            capo_dynamodb.types.bulk_operations_summary_list.deserialize_aws_json_1_0(
                data["BulkOperationsSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
