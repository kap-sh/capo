"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteFunctionEventInvokeConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier


class DeleteFunctionEventInvokeConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>A version number or alias name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionEventInvokeConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionEventInvokeConfigRequest:
    out: DeleteFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
    return out
