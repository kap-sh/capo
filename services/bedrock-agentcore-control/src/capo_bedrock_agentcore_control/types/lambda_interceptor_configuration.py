"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LambdaInterceptorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_function_arn


class LambdaInterceptorConfiguration(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The arn of the lambda function to be invoked for the interceptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaInterceptorConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaInterceptorConfiguration:
    out: LambdaInterceptorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
