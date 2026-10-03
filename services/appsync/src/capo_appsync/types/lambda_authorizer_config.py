"""Generated from Smithy shape ``com.amazonaws.appsync#LambdaAuthorizerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.string
    import capo_appsync.types.ttl


class LambdaAuthorizerConfig(TypedDict, closed=True):
    authorizer_result_ttl_in_seconds: "capo_appsync.types.ttl.TTL"
    """<p>The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you don't specify a value for <code>authorizerResultTtlInSeconds</code>, the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a <code>ttlOverride</code> key in its response.</p>"""
    authorizer_uri: "capo_appsync.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (<code>.../v3</code>), or an alias ARN. </p> <p> <b>Note</b>: This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To use the Command Line Interface (CLI), run the following:</p> <p> <code>aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction</code> </p>"""
    identity_validation_expression: NotRequired["capo_appsync.types.string.String"]
    """<p>A regular expression for validation of tokens before the Lambda function is called.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaAuthorizerConfig) -> dict:
    out: dict = {}
    out["authorizerResultTtlInSeconds"] = value.get(
        "authorizer_result_ttl_in_seconds", 0
    )
    out["authorizerUri"] = value["authorizer_uri"]
    if "identity_validation_expression" in value:
        out["identityValidationExpression"] = value["identity_validation_expression"]
    return out


def deserialize_json(data: dict) -> LambdaAuthorizerConfig:
    out: LambdaAuthorizerConfig = {}  # type: ignore[typeddict-item]
    if data.get("authorizerResultTtlInSeconds") is not None:
        out["authorizer_result_ttl_in_seconds"] = data["authorizerResultTtlInSeconds"]
    else:
        out["authorizer_result_ttl_in_seconds"] = 0
    if data.get("authorizerUri") is not None:
        out["authorizer_uri"] = data["authorizerUri"]
    else:
        raise DeserializationError("LambdaAuthorizerConfig.authorizer_uri required")
    if data.get("identityValidationExpression") is not None:
        out["identity_validation_expression"] = data["identityValidationExpression"]
    return out
