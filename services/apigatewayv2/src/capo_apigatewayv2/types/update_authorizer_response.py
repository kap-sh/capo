"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateAuthorizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.arn
    import capo_apigatewayv2.types.authorizer_type
    import capo_apigatewayv2.types.id
    import capo_apigatewayv2.types.identity_source_list
    import capo_apigatewayv2.types.integer_with_length_between0_and3600
    import capo_apigatewayv2.types.jwt_configuration
    import capo_apigatewayv2.types.string_with_length_between0_and1024
    import capo_apigatewayv2.types.string_with_length_between1_and64
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.uri_with_length_between1_and2048


class UpdateAuthorizerResponse(TypedDict, closed=True):
    authorizer_credentials_arn: NotRequired["capo_apigatewayv2.types.arn.Arn"]
    """<p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter. Supported only for REQUEST authorizers.</p>"""
    authorizer_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>The authorizer identifier.</p>"""
    authorizer_payload_format_version: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are 1.0 and 2.0. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a>.</p>"""
    authorizer_result_ttl_in_seconds: NotRequired[
        "capo_apigatewayv2.types.integer_with_length_between0_and3600.IntegerWithLengthBetween0And3600"
    ]
    """<p>The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.</p>"""
    authorizer_type: NotRequired[
        "capo_apigatewayv2.types.authorizer_type.AuthorizerType"
    ]
    """<p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>"""
    authorizer_uri: NotRequired[
        "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>The authorizer's Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:<replaceable>{account_id}</replaceable>:function:<replaceable>{lambda_function_name}</replaceable>/invocations. In general, the URI has this form: arn:aws:apigateway:<replaceable>{region}</replaceable>:lambda:path/<replaceable>{service_api}</replaceable> , where <replaceable></replaceable>{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.</p>"""
    enable_simple_responses: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether a Lambda authorizer returns a response in a simple format. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a></p>"""
    identity_source: NotRequired[
        "capo_apigatewayv2.types.identity_source_list.IdentitySourceList"
    ]
    """<p>The identity source for which authorization is requested.</p> <p>For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with $, for example, $request.header.Auth, $request.querystring.Name. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a>.</p> <p>For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example $request.header.Authorization.</p>"""
    identity_validation_expression: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The validation expression does not apply to the REQUEST authorizer.</p>"""
    jwt_configuration: NotRequired[
        "capo_apigatewayv2.types.jwt_configuration.JWTConfiguration"
    ]
    """<p>Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.</p>"""
    name: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the authorizer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAuthorizerResponse) -> dict:
    out: dict = {}
    if "authorizer_credentials_arn" in value:
        out["authorizerCredentialsArn"] = value["authorizer_credentials_arn"]
    if "authorizer_id" in value:
        out["authorizerId"] = value["authorizer_id"]
    if "authorizer_payload_format_version" in value:
        out["authorizerPayloadFormatVersion"] = value[
            "authorizer_payload_format_version"
        ]
    if "authorizer_result_ttl_in_seconds" in value:
        out["authorizerResultTtlInSeconds"] = value["authorizer_result_ttl_in_seconds"]
    if "authorizer_type" in value:
        import capo_apigatewayv2.types.authorizer_type

        out["authorizerType"] = capo_apigatewayv2.types.authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    if "authorizer_uri" in value:
        out["authorizerUri"] = value["authorizer_uri"]
    if "enable_simple_responses" in value:
        out["enableSimpleResponses"] = value["enable_simple_responses"]
    if "identity_source" in value:
        import capo_apigatewayv2.types.identity_source_list

        out["identitySource"] = (
            capo_apigatewayv2.types.identity_source_list.serialize_json(
                value["identity_source"]
            )
        )
    if "identity_validation_expression" in value:
        out["identityValidationExpression"] = value["identity_validation_expression"]
    if "jwt_configuration" in value:
        import capo_apigatewayv2.types.jwt_configuration

        out["jwtConfiguration"] = (
            capo_apigatewayv2.types.jwt_configuration.serialize_json(
                value["jwt_configuration"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAuthorizerResponse:
    out: UpdateAuthorizerResponse = {}  # type: ignore[typeddict-item]
    if data.get("authorizerCredentialsArn") is not None:
        out["authorizer_credentials_arn"] = data["authorizerCredentialsArn"]
    if data.get("authorizerId") is not None:
        out["authorizer_id"] = data["authorizerId"]
    if data.get("authorizerPayloadFormatVersion") is not None:
        out["authorizer_payload_format_version"] = data[
            "authorizerPayloadFormatVersion"
        ]
    if data.get("authorizerResultTtlInSeconds") is not None:
        out["authorizer_result_ttl_in_seconds"] = data["authorizerResultTtlInSeconds"]
    if data.get("authorizerType") is not None:
        import capo_apigatewayv2.types.authorizer_type

        out["authorizer_type"] = (
            capo_apigatewayv2.types.authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    if data.get("authorizerUri") is not None:
        out["authorizer_uri"] = data["authorizerUri"]
    if data.get("enableSimpleResponses") is not None:
        out["enable_simple_responses"] = data["enableSimpleResponses"]
    if data.get("identitySource") is not None:
        import capo_apigatewayv2.types.identity_source_list

        out["identity_source"] = (
            capo_apigatewayv2.types.identity_source_list.deserialize_json(
                data["identitySource"]
            )
        )
    if data.get("identityValidationExpression") is not None:
        out["identity_validation_expression"] = data["identityValidationExpression"]
    if data.get("jwtConfiguration") is not None:
        import capo_apigatewayv2.types.jwt_configuration

        out["jwt_configuration"] = (
            capo_apigatewayv2.types.jwt_configuration.deserialize_json(
                data["jwtConfiguration"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
