"""Generated from Smithy shape ``com.amazonaws.apigateway#Integration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.connection_type
    import capo_api_gateway.types.content_handling_strategy
    import capo_api_gateway.types.integer
    import capo_api_gateway.types.integration_type
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_integration_response
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.response_transfer_mode
    import capo_api_gateway.types.string
    import capo_api_gateway.types.tls_config


class Integration(TypedDict, closed=True):
    type: NotRequired["capo_api_gateway.types.integration_type.IntegrationType"]
    """<p>Specifies an API method integration type. The valid value is one of the following:</p> <p>For the HTTP and HTTP proxy integrations, each integration can specify a protocol (<code>http/https</code>), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a <code>connectionType</code> of <code>VPC_LINK</code> is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.</p>"""
    http_method: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies the integration's HTTP method type. For the Type property, if you specify <code>MOCK</code>, this property is optional. For Lambda integrations, you must set the integration method to <code>POST</code>. For all other types, you must specify this property.</p>"""
    uri: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies Uniform Resource Identifier (URI) of the integration endpoint.</p> <p>For <code>HTTP</code> or <code>HTTP_PROXY</code> integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification for standard integrations. If <code>connectionType</code> is <code>VPC_LINK</code> specify the Network Load Balancer DNS name. For <code>AWS</code> or <code>AWS_PROXY</code> integrations, the URI is of the form <code>arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}</code>. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated Amazon Web Services service (e.g., s3); and {subdomain} is a designated subdomain supported by certain Amazon Web Services service for fast host-name lookup. action can be used for an Amazon Web Services service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an Amazon Web Services service path-based API. The ensuing service_api refers to the path to an Amazon Web Services service resource, including the region of the integrated Amazon Web Services service, if applicable. For example, for integration with the S3 API of GetObject, the uri can be either <code>arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}</code> or <code>arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}</code> </p>"""
    connection_type: NotRequired[
        "capo_api_gateway.types.connection_type.ConnectionType"
    ]
    """<p>The type of the network connection to the integration endpoint. The valid value is <code>INTERNET</code> for connections through the public routable internet or <code>VPC_LINK</code> for private connections between API Gateway and a network load balancer in a VPC. The default value is <code>INTERNET</code>.</p>"""
    connection_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ID of the VpcLink used for the integration when <code>connectionType=VPC_LINK</code> and undefined, otherwise.</p>"""
    credentials: NotRequired["capo_api_gateway.types.string.String"]
    r"""<p>Specifies the credentials required for the integration, if any. For Amazon Web Services integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string <code>arn:aws:iam::\*:user/\*</code>. To use resource-based permissions on supported Amazon Web Services services, specify null.</p>"""
    request_parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of <code>method.request.{location}.{name}</code>, where <code>location</code> is <code>querystring</code>, <code>path</code>, or <code>header</code> and <code>name</code> must be a valid and unique method request parameter name.</p>"""
    request_templates: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.</p>"""
    passthrough_behavior: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in <code>requestTemplates</code>. The valid value is one of the following: <code>WHEN_NO_MATCH</code>: passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. <code>WHEN_NO_TEMPLATES</code>: passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP 415 Unsupported Media Type response. <code>NEVER</code>: rejects the method request with an HTTP 415 Unsupported Media Type response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request.</p>"""
    content_handling: NotRequired[
        "capo_api_gateway.types.content_handling_strategy.ContentHandlingStrategy"
    ]
    """<p>Specifies how to handle request payload content type conversions. Supported values are <code>CONVERT_TO_BINARY</code> and <code>CONVERT_TO_TEXT</code>, with the following behaviors:</p> <p>If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the <code>passthroughBehavior</code> is configured to support payload pass-through.</p>"""
    timeout_in_millis: "capo_api_gateway.types.integer.Integer"
    """<p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. You can increase the default value to longer than 29 seconds for Regional or private APIs only.</p>"""
    cache_namespace: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the <code>cacheNamespace</code>. You can specify the same <code>cacheNamespace</code> across resources to return the same cached data for requests to different resources.</p>"""
    cache_key_parameters: NotRequired[
        "capo_api_gateway.types.list_of_string.ListOfString"
    ]
    """<p>A list of request parameters whose values API Gateway caches. To be valid values for <code>cacheKeyParameters</code>, these parameters must also be specified for Method <code>requestParameters</code>.</p>"""
    integration_responses: NotRequired[
        "capo_api_gateway.types.map_of_integration_response.MapOfIntegrationResponse"
    ]
    """<p>Specifies the integration's responses.</p>"""
    tls_config: NotRequired["capo_api_gateway.types.tls_config.TlsConfig"]
    """<p>Specifies the TLS configuration for an integration.</p>"""
    response_transfer_mode: NotRequired[
        "capo_api_gateway.types.response_transfer_mode.ResponseTransferMode"
    ]
    """<p> The response transfer mode of the integration. </p>"""
    integration_target: NotRequired["capo_api_gateway.types.string.String"]
    """<p> The ALB or NLB ARN to send the request to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Integration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_api_gateway.types.integration_type

        out["type"] = capo_api_gateway.types.integration_type.serialize_json(
            value["type"]
        )
    if "http_method" in value:
        out["httpMethod"] = value["http_method"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "connection_type" in value:
        import capo_api_gateway.types.connection_type

        out["connectionType"] = capo_api_gateway.types.connection_type.serialize_json(
            value["connection_type"]
        )
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "credentials" in value:
        out["credentials"] = value["credentials"]
    if "request_parameters" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["requestParameters"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["request_parameters"]
            )
        )
    if "request_templates" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["requestTemplates"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["request_templates"]
            )
        )
    if "passthrough_behavior" in value:
        out["passthroughBehavior"] = value["passthrough_behavior"]
    if "content_handling" in value:
        import capo_api_gateway.types.content_handling_strategy

        out["contentHandling"] = (
            capo_api_gateway.types.content_handling_strategy.serialize_json(
                value["content_handling"]
            )
        )
    out["timeoutInMillis"] = value.get("timeout_in_millis", 0)
    if "cache_namespace" in value:
        out["cacheNamespace"] = value["cache_namespace"]
    if "cache_key_parameters" in value:
        import capo_api_gateway.types.list_of_string

        out["cacheKeyParameters"] = (
            capo_api_gateway.types.list_of_string.serialize_json(
                value["cache_key_parameters"]
            )
        )
    if "integration_responses" in value:
        import capo_api_gateway.types.map_of_integration_response

        out["integrationResponses"] = (
            capo_api_gateway.types.map_of_integration_response.serialize_json(
                value["integration_responses"]
            )
        )
    if "tls_config" in value:
        import capo_api_gateway.types.tls_config

        out["tlsConfig"] = capo_api_gateway.types.tls_config.serialize_json(
            value["tls_config"]
        )
    if "response_transfer_mode" in value:
        import capo_api_gateway.types.response_transfer_mode

        out["responseTransferMode"] = (
            capo_api_gateway.types.response_transfer_mode.serialize_json(
                value["response_transfer_mode"]
            )
        )
    if "integration_target" in value:
        out["integrationTarget"] = value["integration_target"]
    return out


def deserialize_json(data: dict) -> Integration:
    out: Integration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_api_gateway.types.integration_type

        out["type"] = capo_api_gateway.types.integration_type.deserialize_json(
            data["type"]
        )
    if data.get("httpMethod") is not None:
        out["http_method"] = data["httpMethod"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("connectionType") is not None:
        import capo_api_gateway.types.connection_type

        out["connection_type"] = (
            capo_api_gateway.types.connection_type.deserialize_json(
                data["connectionType"]
            )
        )
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("credentials") is not None:
        out["credentials"] = data["credentials"]
    if data.get("requestParameters") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["request_parameters"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["requestParameters"]
            )
        )
    if data.get("requestTemplates") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["request_templates"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["requestTemplates"]
            )
        )
    if data.get("passthroughBehavior") is not None:
        out["passthrough_behavior"] = data["passthroughBehavior"]
    if data.get("contentHandling") is not None:
        import capo_api_gateway.types.content_handling_strategy

        out["content_handling"] = (
            capo_api_gateway.types.content_handling_strategy.deserialize_json(
                data["contentHandling"]
            )
        )
    if data.get("timeoutInMillis") is not None:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    else:
        out["timeout_in_millis"] = 0
    if data.get("cacheNamespace") is not None:
        out["cache_namespace"] = data["cacheNamespace"]
    if data.get("cacheKeyParameters") is not None:
        import capo_api_gateway.types.list_of_string

        out["cache_key_parameters"] = (
            capo_api_gateway.types.list_of_string.deserialize_json(
                data["cacheKeyParameters"]
            )
        )
    if data.get("integrationResponses") is not None:
        import capo_api_gateway.types.map_of_integration_response

        out["integration_responses"] = (
            capo_api_gateway.types.map_of_integration_response.deserialize_json(
                data["integrationResponses"]
            )
        )
    if data.get("tlsConfig") is not None:
        import capo_api_gateway.types.tls_config

        out["tls_config"] = capo_api_gateway.types.tls_config.deserialize_json(
            data["tlsConfig"]
        )
    if data.get("responseTransferMode") is not None:
        import capo_api_gateway.types.response_transfer_mode

        out["response_transfer_mode"] = (
            capo_api_gateway.types.response_transfer_mode.deserialize_json(
                data["responseTransferMode"]
            )
        )
    if data.get("integrationTarget") is not None:
        out["integration_target"] = data["integrationTarget"]
    return out
