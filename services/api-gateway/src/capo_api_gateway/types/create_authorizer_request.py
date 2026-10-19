"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.authorizer_type
    import capo_api_gateway.types.list_of_ar_ns
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.string


class CreateAuthorizerRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    name: "capo_api_gateway.types.string.String"
    """<p>The name of the authorizer.</p>"""
    type: "capo_api_gateway.types.authorizer_type.AuthorizerType"
    """<p>The authorizer type. Valid values are <code>TOKEN</code> for a Lambda function using a single authorization token submitted in a custom header, <code>REQUEST</code> for a Lambda function using incoming request parameters, and <code>COGNITO_USER_POOLS</code> for using an Amazon Cognito user pool.</p>"""
    provider_ar_ns: NotRequired["capo_api_gateway.types.list_of_ar_ns.ListOfARNs"]
    """<p>A list of the Amazon Cognito user pool ARNs for the <code>COGNITO_USER_POOLS</code> authorizer. Each element is of this format: <code>arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</code>. For a <code>TOKEN</code> or <code>REQUEST</code> authorizer, this is not defined. </p>"""
    auth_type: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Optional customer-defined field, used in OpenAPI imports and exports without functional impact.</p>"""
    authorizer_uri: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies the authorizer's Uniform Resource Identifier (URI). For <code>TOKEN</code> or <code>REQUEST</code> authorizers, this must be a well-formed Lambda function URI, for example, <code>arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations</code>. In general, the URI has this form <code>arn:aws:apigateway:{region}:lambda:path/{service_api}</code>, where <code>{region}</code> is the same as the region hosting the Lambda function, <code>path</code> indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial <code>/</code>. For Lambda functions, this is usually of the form <code>/2015-03-31/functions/[FunctionARN]/invocations</code>.</p>"""
    authorizer_credentials: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.</p>"""
    identity_source: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identity source for which authorization is requested. For a <code>TOKEN</code> or <code>COGNITO_USER_POOLS</code> authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is <code>Auth</code>, the header mapping expression is <code>method.request.header.Auth</code>. For the <code>REQUEST</code> authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an <code>Auth</code> header, a <code>Name</code> query string parameter are defined as identity sources, this value is <code>method.request.header.Auth, method.request.querystring.Name</code>. These parameters will be used to derive the authorization caching key and to perform runtime validation of the <code>REQUEST</code> authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.</p>"""
    identity_validation_expression: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A validation expression for the incoming identity token. For <code>TOKEN</code> authorizers, this value is a regular expression. For <code>COGNITO_USER_POOLS</code> authorizers, API Gateway will match the <code>aud</code> field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the <code>REQUEST</code> authorizer.</p>"""
    authorizer_result_ttl_in_seconds: NotRequired[
        "capo_api_gateway.types.nullable_integer.NullableInteger"
    ]
    """<p>The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAuthorizerRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_api_gateway.types.authorizer_type

    out["type"] = capo_api_gateway.types.authorizer_type.serialize_json(value["type"])
    if "provider_ar_ns" in value:
        import capo_api_gateway.types.list_of_ar_ns

        out["providerARNs"] = capo_api_gateway.types.list_of_ar_ns.serialize_json(
            value["provider_ar_ns"]
        )
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "authorizer_uri" in value:
        out["authorizerUri"] = value["authorizer_uri"]
    if "authorizer_credentials" in value:
        out["authorizerCredentials"] = value["authorizer_credentials"]
    if "identity_source" in value:
        out["identitySource"] = value["identity_source"]
    if "identity_validation_expression" in value:
        out["identityValidationExpression"] = value["identity_validation_expression"]
    if "authorizer_result_ttl_in_seconds" in value:
        out["authorizerResultTtlInSeconds"] = value["authorizer_result_ttl_in_seconds"]
    return out


def deserialize_json(data: dict) -> CreateAuthorizerRequest:
    out: CreateAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_api_gateway.types.authorizer_type

        out["type"] = capo_api_gateway.types.authorizer_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_api_gateway.types.authorizer_type.AuthorizerType", ""
        )
    if data.get("providerARNs") is not None:
        import capo_api_gateway.types.list_of_ar_ns

        out["provider_ar_ns"] = capo_api_gateway.types.list_of_ar_ns.deserialize_json(
            data["providerARNs"]
        )
    if data.get("authType") is not None:
        out["auth_type"] = data["authType"]
    if data.get("authorizerUri") is not None:
        out["authorizer_uri"] = data["authorizerUri"]
    if data.get("authorizerCredentials") is not None:
        out["authorizer_credentials"] = data["authorizerCredentials"]
    if data.get("identitySource") is not None:
        out["identity_source"] = data["identitySource"]
    if data.get("identityValidationExpression") is not None:
        out["identity_validation_expression"] = data["identityValidationExpression"]
    if data.get("authorizerResultTtlInSeconds") is not None:
        out["authorizer_result_ttl_in_seconds"] = data["authorizerResultTtlInSeconds"]
    return out
