"""Generated from Smithy shape ``com.amazonaws.codepipeline#LambdaExecutorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.lambda_function_arn


class LambdaExecutorConfiguration(TypedDict, closed=True):
    lambda_function_arn: "capo_codepipeline.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The ARN of the Lambda function used by the action engine.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaExecutorConfiguration) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaExecutorConfiguration:
    out: LambdaExecutorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lambdaFunctionArn") is not None:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        out["lambda_function_arn"] = ""
    return out
