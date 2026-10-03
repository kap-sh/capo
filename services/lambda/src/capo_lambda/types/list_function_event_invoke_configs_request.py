"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionEventInvokeConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.max_function_event_invoke_config_list_items
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.string


class ListFunctionEventInvokeConfigsRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired[
        "capo_lambda.types.max_function_event_invoke_config_list_items.MaxFunctionEventInvokeConfigListItems"
    ]
    """<p>The maximum number of configurations to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionEventInvokeConfigsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionEventInvokeConfigsRequest:
    out: ListFunctionEventInvokeConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
