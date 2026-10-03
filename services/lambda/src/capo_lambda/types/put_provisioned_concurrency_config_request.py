"""Generated from Smithy shape ``com.amazonaws.lambda#PutProvisionedConcurrencyConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.function_name
    import capo_lambda.types.positive_integer
    import capo_lambda.types.qualifier


class PutProvisionedConcurrencyConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    qualifier: "capo_lambda.types.qualifier.Qualifier"
    """<p>The version number or alias name.</p>"""
    provisioned_concurrent_executions: (
        "capo_lambda.types.positive_integer.PositiveInteger"
    )
    """<p>The amount of provisioned concurrency to allocate for the version or alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutProvisionedConcurrencyConfigRequest) -> dict:
    out: dict = {}
    out["ProvisionedConcurrentExecutions"] = value["provisioned_concurrent_executions"]
    return out


def deserialize_json(data: dict) -> PutProvisionedConcurrencyConfigRequest:
    out: PutProvisionedConcurrencyConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedConcurrentExecutions") is not None:
        out["provisioned_concurrent_executions"] = data[
            "ProvisionedConcurrentExecutions"
        ]
    else:
        raise DeserializationError(
            "PutProvisionedConcurrencyConfigRequest.provisioned_concurrent_executions required"
        )
    return out
