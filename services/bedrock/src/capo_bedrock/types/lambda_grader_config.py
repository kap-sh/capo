"""Generated from Smithy shape ``com.amazonaws.bedrock#LambdaGraderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.lambda_arn


class LambdaGraderConfig(TypedDict, closed=True):
    lambda_arn: "capo_bedrock.types.lambda_arn.LambdaArn"
    """<p> ARN of the AWS Lambda function that will evaluate model responses and return reward scores for RFT training. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaGraderConfig) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    return out


def deserialize_json(data: dict) -> LambdaGraderConfig:
    out: LambdaGraderConfig = {}  # type: ignore[typeddict-item]
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        out["lambda_arn"] = ""
    return out
