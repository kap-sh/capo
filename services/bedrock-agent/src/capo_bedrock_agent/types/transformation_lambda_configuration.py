"""Generated from Smithy shape ``com.amazonaws.bedrockagent#TransformationLambdaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.lambda_arn


class TransformationLambdaConfiguration(TypedDict, closed=True):
    lambda_arn: "capo_bedrock_agent.types.lambda_arn.LambdaArn"
    """<p>The function's ARN identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformationLambdaConfiguration) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    return out


def deserialize_json(data: dict) -> TransformationLambdaConfiguration:
    out: TransformationLambdaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        out["lambda_arn"] = ""
    return out
