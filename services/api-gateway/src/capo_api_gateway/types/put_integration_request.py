"""Generated from Smithy shape ``com.amazonaws.apigateway#PutIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.connection_type
    import capo_api_gateway.types.content_handling_strategy
    import capo_api_gateway.types.integration_type
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.response_transfer_mode
    import capo_api_gateway.types.string
    import capo_api_gateway.types.tls_config


class PutIntegrationRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>Specifies a put integration request's resource ID.</p>"""
    http_method: "capo_api_gateway.types.string.String"
    """<p>Specifies the HTTP method for the integration.</p>"""
    type: "capo_api_gateway.types.integration_type.IntegrationType"
    """<p>Specifies a put integration input's type.</p>"""
    integration_http_method: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The HTTP method for the integration.</p>"""
    uri: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies Uniform Resource Identifier (URI) of the integration endpoint. For HTTP or <code>HTTP_PROXY</code> integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification, for either standard integration, where <code>connectionType</code> is not <code>VPC_LINK</code>, or private integration, where <code>connectionType</code> is <code>VPC_LINK</code>. For a private HTTP integration, the URI is not used for routing. For <code>AWS</code> or <code>AWS_PROXY</code> integrations, the URI is of the form <code>arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api</code>}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated Amazon Web Services service (e.g., s3); and {subdomain} is a designated subdomain supported by certain Amazon Web Services service for fast host-name lookup. action can be used for an Amazon Web Services service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an Amazon Web Services service path-based API. The ensuing service_api refers to the path to an Amazon Web Services service resource, including the region of the integrated Amazon Web Services service, if applicable. For example, for integration with the S3 API of <code>GetObject</code>, the <code>uri</code> can be either <code>arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}</code> or <code>arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}</code>.</p>"""
    connection_type: NotRequired[
        "capo_api_gateway.types.connection_type.ConnectionType"
    ]
    """<p>The type of the network connection to the integration endpoint. The valid value is <code>INTERNET</code> for connections through the public routable internet or <code>VPC_LINK</code> for private connections between API Gateway and a network load balancer in a VPC. The default value is <code>INTERNET</code>.</p>"""
    connection_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ID of the VpcLink used for the integration. Specify this value only if you specify <code>VPC_LINK</code> as the connection type.</p>"""
    credentials: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies whether credentials are required for a put integration.</p>"""
    request_parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of <code>method.request.{location}.{name}</code>, where <code>location</code> is <code>querystring</code>, <code>path</code>, or <code>header</code> and <code>name</code> must be a valid and unique method request parameter name.</p>"""
    request_templates: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.</p>"""
    passthrough_behavior: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the <code>requestTemplates</code> property on the Integration resource. There are three valid values: <code>WHEN_NO_MATCH</code>, <code>WHEN_NO_TEMPLATES</code>, and <code>NEVER</code>. </p>"""
    cache_namespace: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the <code>cacheNamespace</code>. You can specify the same <code>cacheNamespace</code> across resources to return the same cached data for requests to different resources.</p>"""
    cache_key_parameters: NotRequired[
        "capo_api_gateway.types.list_of_string.ListOfString"
    ]
    """<p>A list of request parameters whose values API Gateway caches. To be valid values for <code>cacheKeyParameters</code>, these parameters must also be specified for Method <code>requestParameters</code>.</p>"""
    content_handling: NotRequired[
        "capo_api_gateway.types.content_handling_strategy.ContentHandlingStrategy"
    ]
    """<p>Specifies how to handle request payload content type conversions. Supported values are <code>CONVERT_TO_BINARY</code> and <code>CONVERT_TO_TEXT</code>, with the following behaviors:</p> <p>If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the <code>passthroughBehavior</code> is configured to support payload pass-through.</p>"""
    timeout_in_millis: NotRequired[
        "capo_api_gateway.types.nullable_integer.NullableInteger"
    ]
    """<p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. You can increase the default value to longer than 29 seconds for Regional or private APIs only.</p>"""
    tls_config: NotRequired["capo_api_gateway.types.tls_config.TlsConfig"]
    response_transfer_mode: NotRequired[
        "capo_api_gateway.types.response_transfer_mode.ResponseTransferMode"
    ]
    """<p> The response transfer mode of the integration. </p>"""
    integration_target: NotRequired["capo_api_gateway.types.string.String"]
    """<p> The ALB or NLB listener to send the request to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutIntegrationRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.integration_type

    out["type"] = capo_api_gateway.types.integration_type.serialize_json(value["type"])
    if "integration_http_method" in value:
        out["httpMethod"] = value["integration_http_method"]
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
    if "cache_namespace" in value:
        out["cacheNamespace"] = value["cache_namespace"]
    if "cache_key_parameters" in value:
        import capo_api_gateway.types.list_of_string

        out["cacheKeyParameters"] = (
            capo_api_gateway.types.list_of_string.serialize_json(
                value["cache_key_parameters"]
            )
        )
    if "content_handling" in value:
        import capo_api_gateway.types.content_handling_strategy

        out["contentHandling"] = (
            capo_api_gateway.types.content_handling_strategy.serialize_json(
                value["content_handling"]
            )
        )
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
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


def deserialize_json(data: dict) -> PutIntegrationRequest:
    out: PutIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_api_gateway.types.integration_type

        out["type"] = capo_api_gateway.types.integration_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_api_gateway.types.integration_type.IntegrationType", ""
        )
    if data.get("httpMethod") is not None:
        out["integration_http_method"] = data["httpMethod"]
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
    if data.get("cacheNamespace") is not None:
        out["cache_namespace"] = data["cacheNamespace"]
    if data.get("cacheKeyParameters") is not None:
        import capo_api_gateway.types.list_of_string

        out["cache_key_parameters"] = (
            capo_api_gateway.types.list_of_string.deserialize_json(
                data["cacheKeyParameters"]
            )
        )
    if data.get("contentHandling") is not None:
        import capo_api_gateway.types.content_handling_strategy

        out["content_handling"] = (
            capo_api_gateway.types.content_handling_strategy.deserialize_json(
                data["contentHandling"]
            )
        )
    if data.get("timeoutInMillis") is not None:
        out["timeout_in_millis"] = data["timeoutInMillis"]
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
