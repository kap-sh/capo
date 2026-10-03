"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteFunctionCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.namespaced_function_name


class DeleteFunctionCodeSigningConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionCodeSigningConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionCodeSigningConfigRequest:
    out: DeleteFunctionCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    return out
