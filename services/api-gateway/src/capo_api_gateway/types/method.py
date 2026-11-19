"""Generated from Smithy shape ``com.amazonaws.apigateway#Method``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.integration
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_method_response
    import capo_api_gateway.types.map_of_string_to_boolean
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.nullable_boolean
    import capo_api_gateway.types.string


class Method(TypedDict, closed=True):
    http_method: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The method's HTTP verb.</p>"""
    authorization_type: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The method's authorization type. Valid values are <code>NONE</code> for open access, <code>AWS_IAM</code> for using Amazon Web Services IAM permissions, <code>CUSTOM</code> for using a custom authorizer, <code>COGNITO_USER_POOLS</code> for using a Cognito user pool, or <code>JWT</code> for using a JWT authorizer.</p>"""
    authorizer_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of an Authorizer to use on this method. The <code>authorizationType</code> must be <code>CUSTOM</code>.</p>"""
    api_key_required: NotRequired[
        "capo_api_gateway.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A boolean flag specifying whether a valid ApiKey is required to invoke this method.</p>"""
    request_validator_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of a RequestValidator for request validation.</p>"""
    operation_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A human-friendly operation identifier for the method. For example, you can assign the <code>operationName</code> of <code>ListPets</code> for the <code>GET /pets</code> method in the <code>PetStore</code> example.</p>"""
    request_parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_boolean.MapOfStringToBoolean"
    ]
    """<p>A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of <code>method.request.{location}.{name}</code>, where <code>location</code> is <code>querystring</code>, <code>path</code>, or <code>header</code> and <code>name</code> is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (<code>true</code>) or optional (<code>false</code>). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or templates.</p>"""
    request_models: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).</p>"""
    method_responses: NotRequired[
        "capo_api_gateway.types.map_of_method_response.MapOfMethodResponse"
    ]
    """<p>Gets a method response associated with a given HTTP status code. </p>"""
    method_integration: NotRequired["capo_api_gateway.types.integration.Integration"]
    """<p>Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.</p>"""
    authorization_scopes: NotRequired[
        "capo_api_gateway.types.list_of_string.ListOfString"
    ]
    """<p>A list of authorization scopes configured on the method. The scopes are used with a <code>COGNITO_USER_POOLS</code> authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes. The scopes are also used with a <code>JWT</code> authorizer. When scopes are configured, the <code>scope</code> (or <code>scp</code>) claim of the token must contain at least one of the configured scopes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Method) -> dict:
    out: dict = {}
    if "http_method" in value:
        out["httpMethod"] = value["http_method"]
    if "authorization_type" in value:
        out["authorizationType"] = value["authorization_type"]
    if "authorizer_id" in value:
        out["authorizerId"] = value["authorizer_id"]
    if "api_key_required" in value:
        out["apiKeyRequired"] = value["api_key_required"]
    if "request_validator_id" in value:
        out["requestValidatorId"] = value["request_validator_id"]
    if "operation_name" in value:
        out["operationName"] = value["operation_name"]
    if "request_parameters" in value:
        import capo_api_gateway.types.map_of_string_to_boolean

        out["requestParameters"] = (
            capo_api_gateway.types.map_of_string_to_boolean.serialize_json(
                value["request_parameters"]
            )
        )
    if "request_models" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["requestModels"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["request_models"]
            )
        )
    if "method_responses" in value:
        import capo_api_gateway.types.map_of_method_response

        out["methodResponses"] = (
            capo_api_gateway.types.map_of_method_response.serialize_json(
                value["method_responses"]
            )
        )
    if "method_integration" in value:
        import capo_api_gateway.types.integration

        out["methodIntegration"] = capo_api_gateway.types.integration.serialize_json(
            value["method_integration"]
        )
    if "authorization_scopes" in value:
        import capo_api_gateway.types.list_of_string

        out["authorizationScopes"] = (
            capo_api_gateway.types.list_of_string.serialize_json(
                value["authorization_scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> Method:
    out: Method = {}  # type: ignore[typeddict-item]
    if data.get("httpMethod") is not None:
        out["http_method"] = data["httpMethod"]
    if data.get("authorizationType") is not None:
        out["authorization_type"] = data["authorizationType"]
    if data.get("authorizerId") is not None:
        out["authorizer_id"] = data["authorizerId"]
    if data.get("apiKeyRequired") is not None:
        out["api_key_required"] = data["apiKeyRequired"]
    if data.get("requestValidatorId") is not None:
        out["request_validator_id"] = data["requestValidatorId"]
    if data.get("operationName") is not None:
        out["operation_name"] = data["operationName"]
    if data.get("requestParameters") is not None:
        import capo_api_gateway.types.map_of_string_to_boolean

        out["request_parameters"] = (
            capo_api_gateway.types.map_of_string_to_boolean.deserialize_json(
                data["requestParameters"]
            )
        )
    if data.get("requestModels") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["request_models"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["requestModels"]
            )
        )
    if data.get("methodResponses") is not None:
        import capo_api_gateway.types.map_of_method_response

        out["method_responses"] = (
            capo_api_gateway.types.map_of_method_response.deserialize_json(
                data["methodResponses"]
            )
        )
    if data.get("methodIntegration") is not None:
        import capo_api_gateway.types.integration

        out["method_integration"] = capo_api_gateway.types.integration.deserialize_json(
            data["methodIntegration"]
        )
    if data.get("authorizationScopes") is not None:
        import capo_api_gateway.types.list_of_string

        out["authorization_scopes"] = (
            capo_api_gateway.types.list_of_string.deserialize_json(
                data["authorizationScopes"]
            )
        )
    return out
