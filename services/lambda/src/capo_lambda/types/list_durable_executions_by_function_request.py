"""Generated from Smithy shape ``com.amazonaws.lambda#ListDurableExecutionsByFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_name
    import capo_lambda.types.execution_status_list
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.item_count
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.reverse_order
    import capo_lambda.types.string


class ListDurableExecutionsByFunctionRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>The function version to filter executions by. If you don't specify a qualifier, this operation returns executions across all versions of the Lambda function.</p>"""
    durable_execution_name: NotRequired[
        "capo_lambda.types.durable_execution_name.DurableExecutionName"
    ]
    """<p>Filter executions by name. Only executions with names that matches this string are returned.</p>"""
    statuses: NotRequired["capo_lambda.types.execution_status_list.ExecutionStatusList"]
    """<p>Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED.</p>"""
    started_after: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>Filter executions that started after this timestamp (ISO 8601 format).</p>"""
    started_before: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>Filter executions that started before this timestamp (ISO 8601 format).</p>"""
    reverse_order: NotRequired["capo_lambda.types.reverse_order.ReverseOrder"]
    """<p>Set to true to return results in chronological order (oldest first). Default is false.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Pagination token from a previous request to continue retrieving results.</p>"""
    max_items: "capo_lambda.types.item_count.ItemCount"
    """<p>Maximum number of executions to return (1-1000). Default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDurableExecutionsByFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDurableExecutionsByFunctionRequest:
    out: ListDurableExecutionsByFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
