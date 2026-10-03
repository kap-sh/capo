"""Generated from Smithy shape ``com.amazonaws.lambda#ListAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_name
    import capo_lambda.types.max_list_items
    import capo_lambda.types.string
    import capo_lambda.types.version_with_latest_published


class ListAliasesRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    function_version: NotRequired[
        "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    ]
    """<p>Specify a function version to only list aliases that invoke that version.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["capo_lambda.types.max_list_items.MaxListItems"]
    """<p>Limit the number of aliases returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAliasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAliasesRequest:
    out: ListAliasesRequest = {}  # type: ignore[typeddict-item]
    return out
