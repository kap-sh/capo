"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteFunctionUrlConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_url_function_name
    import capo_lambda.types.function_url_qualifier


class DeleteFunctionUrlConfigRequest(TypedDict, closed=True):
    function_name: (
        "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName"
    )
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
    ]
    """<p>The alias name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionUrlConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionUrlConfigRequest:
    out: DeleteFunctionUrlConfigRequest = {}  # type: ignore[typeddict-item]
    return out
