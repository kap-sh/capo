"""Generated from Smithy shape ``com.amazonaws.datazone#CustomAccountPoolHandler``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.lambda_execution_role_arn
    import capo_datazone.types.lambda_function_arn


class CustomAccountPoolHandler(TypedDict, closed=True):
    lambda_function_arn: "capo_datazone.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The ARN of the Amazon Web Services Lambda function for the custom Amazon Web Services Lambda handler.</p>"""
    lambda_execution_role_arn: NotRequired[
        "capo_datazone.types.lambda_execution_role_arn.LambdaExecutionRoleArn"
    ]
    """<p>The ARN of the IAM role that enables Amazon SageMaker Unified Studio to invoke the Amazon Web Services Lambda funtion if the account source is the custom account pool handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAccountPoolHandler) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    if "lambda_execution_role_arn" in value:
        out["lambdaExecutionRoleArn"] = value["lambda_execution_role_arn"]
    return out


def deserialize_json(data: dict) -> CustomAccountPoolHandler:
    out: CustomAccountPoolHandler = {}  # type: ignore[typeddict-item]
    if data.get("lambdaFunctionArn") is not None:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        out["lambda_function_arn"] = ""
    if data.get("lambdaExecutionRoleArn") is not None:
        out["lambda_execution_role_arn"] = data["lambdaExecutionRoleArn"]
    return out
