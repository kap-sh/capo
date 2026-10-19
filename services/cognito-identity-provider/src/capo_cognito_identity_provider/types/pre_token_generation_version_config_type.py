"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreTokenGenerationVersionConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type


class PreTokenGenerationVersionConfigType(TypedDict, closed=True):
    lambda_version: "capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type.PreTokenGenerationLambdaVersionType"
    """<p>The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.</p>"""
    lambda_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.</p> <p>This parameter and the <code>PreTokenGeneration</code> property of <code>LambdaConfig</code> have the same value. For new instances of pre token generation triggers, set <code>LambdaArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreTokenGenerationVersionConfigType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type

    out["LambdaVersion"] = (
        capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type.serialize_aws_json_1_1(
            value["lambda_version"]
        )
    )
    out["LambdaArn"] = value["lambda_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreTokenGenerationVersionConfigType:
    out: PreTokenGenerationVersionConfigType = {}  # type: ignore[typeddict-item]
    if data.get("LambdaVersion") is not None:
        import capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type

        out["lambda_version"] = (
            capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type.deserialize_aws_json_1_1(
                data["LambdaVersion"]
            )
        )
    else:
        import typing

        out["lambda_version"] = typing.cast(
            "capo_cognito_identity_provider.types.pre_token_generation_lambda_version_type.PreTokenGenerationLambdaVersionType",
            "",
        )
    if data.get("LambdaArn") is not None:
        out["lambda_arn"] = data["LambdaArn"]
    else:
        out["lambda_arn"] = ""
    return out
