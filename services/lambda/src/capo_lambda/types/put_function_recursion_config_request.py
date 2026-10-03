"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionRecursionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.recursive_loop
    import capo_lambda.types.unqualified_function_name


class PutFunctionRecursionConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    recursive_loop: "capo_lambda.types.recursive_loop.RecursiveLoop"
    """<p>If you set your function's recursive loop detection configuration to <code>Allow</code>, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop. We recommend that you only use this setting if your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes it.</p> <p>If you set your function's recursive loop detection configuration to <code>Terminate</code>, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.</p> <p>By default, Lambda sets your function's configuration to <code>Terminate</code>.</p> <important> <p>If your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes the function, then use caution and implement suitable guard rails to prevent unexpected charges being billed to your Amazon Web Services account. To learn more about best practices for using recursive invocation patterns, see <a href="https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway">Recursive patterns that cause run-away Lambda functions</a> in Serverless Land.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionRecursionConfigRequest) -> dict:
    out: dict = {}
    import capo_lambda.types.recursive_loop

    out["RecursiveLoop"] = capo_lambda.types.recursive_loop.serialize_json(
        value["recursive_loop"]
    )
    return out


def deserialize_json(data: dict) -> PutFunctionRecursionConfigRequest:
    out: PutFunctionRecursionConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecursiveLoop") is not None:
        import capo_lambda.types.recursive_loop

        out["recursive_loop"] = capo_lambda.types.recursive_loop.deserialize_json(
            data["RecursiveLoop"]
        )
    else:
        raise DeserializationError(
            "PutFunctionRecursionConfigRequest.recursive_loop required"
        )
    return out
