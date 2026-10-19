"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LambdaEvaluatorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_arn


class LambdaEvaluatorConfig(TypedDict, closed=True):
    lambda_arn: "capo_bedrock_agentcore_control.types.lambda_arn.LambdaArn"
    """<p> The Amazon Resource Name (ARN) of the Lambda function that implements the evaluation logic. </p>"""
    lambda_timeout_in_seconds: NotRequired["int"]
    """<p> The timeout in seconds for the Lambda function invocation. Defaults to 60. Must be between 1 and 300. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEvaluatorConfig) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    if "lambda_timeout_in_seconds" in value:
        out["lambdaTimeoutInSeconds"] = value["lambda_timeout_in_seconds"]
    return out


def deserialize_json(data: dict) -> LambdaEvaluatorConfig:
    out: LambdaEvaluatorConfig = {}  # type: ignore[typeddict-item]
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        out["lambda_arn"] = ""
    if data.get("lambdaTimeoutInSeconds") is not None:
        out["lambda_timeout_in_seconds"] = data["lambdaTimeoutInSeconds"]
    return out
