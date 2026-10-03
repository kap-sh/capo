"""Generated from Smithy shape ``com.amazonaws.lambda#GetAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.alias
    import capo_lambda.types.function_name


class GetAliasRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    name: "capo_lambda.types.alias.Alias"
    """<p>The name of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAliasRequest:
    out: GetAliasRequest = {}  # type: ignore[typeddict-item]
    return out
