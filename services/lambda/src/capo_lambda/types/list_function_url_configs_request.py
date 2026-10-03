"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionUrlConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_url_function_name
    import capo_lambda.types.max_items
    import capo_lambda.types.string


class ListFunctionUrlConfigsRequest(TypedDict, closed=True):
    function_name: (
        "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName"
    )
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["capo_lambda.types.max_items.MaxItems"]
    """<p>The maximum number of function URLs to return in the response. Note that <code>ListFunctionUrlConfigs</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionUrlConfigsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionUrlConfigsRequest:
    out: ListFunctionUrlConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
