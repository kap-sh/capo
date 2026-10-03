"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionConcurrencyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.function_name
    import capo_lambda.types.reserved_concurrent_executions


class PutFunctionConcurrencyRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    reserved_concurrent_executions: (
        "capo_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions"
    )
    """<p>The number of simultaneous executions to reserve for the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionConcurrencyRequest) -> dict:
    out: dict = {}
    out["ReservedConcurrentExecutions"] = value["reserved_concurrent_executions"]
    return out


def deserialize_json(data: dict) -> PutFunctionConcurrencyRequest:
    out: PutFunctionConcurrencyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReservedConcurrentExecutions") is not None:
        out["reserved_concurrent_executions"] = data["ReservedConcurrentExecutions"]
    else:
        raise DeserializationError(
            "PutFunctionConcurrencyRequest.reserved_concurrent_executions required"
        )
    return out
