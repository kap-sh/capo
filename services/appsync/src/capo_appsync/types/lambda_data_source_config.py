"""Generated from Smithy shape ``com.amazonaws.appsync#LambdaDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class LambdaDataSourceConfig(TypedDict, closed=True):
    lambda_function_arn: "capo_appsync.types.string.String"
    """<p>The Amazon Resource Name (ARN) for the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDataSourceConfig) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaDataSourceConfig:
    out: LambdaDataSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("lambdaFunctionArn") is not None:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        out["lambda_function_arn"] = ""
    return out
