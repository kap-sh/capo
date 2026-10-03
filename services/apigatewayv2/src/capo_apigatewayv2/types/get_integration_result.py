"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetIntegrationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.arn
    import capo_apigatewayv2.types.connection_type
    import capo_apigatewayv2.types.content_handling_strategy
    import capo_apigatewayv2.types.id
    import capo_apigatewayv2.types.integer_with_length_between50_and30000
    import capo_apigatewayv2.types.integration_parameters
    import capo_apigatewayv2.types.integration_type
    import capo_apigatewayv2.types.passthrough_behavior
    import capo_apigatewayv2.types.response_parameters
    import capo_apigatewayv2.types.selection_expression
    import capo_apigatewayv2.types.string_with_length_between0_and1024
    import capo_apigatewayv2.types.string_with_length_between1_and64
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.string_with_length_between1_and1024
    import capo_apigatewayv2.types.template_map
    import capo_apigatewayv2.types.tls_config
    import capo_apigatewayv2.types.uri_with_length_between1_and2048


class GetIntegrationResult(TypedDict, closed=True):
    api_gateway_managed: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether an integration is managed by API Gateway. If you created an API using using quick create, the resulting integration is managed by API Gateway. You can update a managed integration, but you can't delete it.</p>"""
    connection_id: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and1024.StringWithLengthBetween1And1024"
    ]
    """<p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>"""
    connection_type: NotRequired[
        "capo_apigatewayv2.types.connection_type.ConnectionType"
    ]
    """<p>The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.</p>"""
    content_handling_strategy: NotRequired[
        "capo_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
    ]
    """<p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>"""
    credentials_arn: NotRequired["capo_apigatewayv2.types.arn.Arn"]
    """<p>Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.</p>"""
    description: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>Represents the description of an integration.</p>"""
    integration_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>Represents the identifier of an integration.</p>"""
    integration_method: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>Specifies the integration's HTTP method type.</p>"""
    integration_response_selection_expression: NotRequired[
        "capo_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The integration response selection expression for the integration. Supported only for WebSocket APIs. See <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions">Integration Response Selection Expressions</a>.</p>"""
    integration_subtype: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html">Integration subtype reference</a>.</p>"""
    integration_type: NotRequired[
        "capo_apigatewayv2.types.integration_type.IntegrationType"
    ]
    """<p>The integration type of an integration. One of the following:</p> <p>AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.</p> <p>AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.</p> <p>HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.</p> <p>HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration.</p> <p>MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.</p>"""
    integration_uri: NotRequired[
        "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>For a Lambda integration, specify the URI of a Lambda function.</p> <p>For an HTTP integration, specify a fully-qualified URL.</p> <p>For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html">DiscoverInstances</a>. For private integrations, all resources must be owned by the same AWS account.</p>"""
    passthrough_behavior: NotRequired[
        "capo_apigatewayv2.types.passthrough_behavior.PassthroughBehavior"
    ]
    """<p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.</p> <p>WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.</p> <p>NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.</p> <p>WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.</p>"""
    payload_format_version: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>Specifies the format of the payload sent to an integration. Required for HTTP APIs. Supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html">Working with AWS Lambda proxy integrations for HTTP APIs</a>.</p>"""
    request_parameters: NotRequired[
        "capo_apigatewayv2.types.integration_parameters.IntegrationParameters"
    ]
    """<p>For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.<replaceable>{location}</replaceable>.<replaceable>{name}</replaceable> , where <replaceable>{location}</replaceable> is querystring, path, or header; and <replaceable>{name}</replaceable> must be a valid and unique method request parameter name.</p> <p>For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html">Working with AWS service integrations for HTTP APIs</a>.</p> <p>For HTTP API integrations, without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to backend integrations. The key should follow the pattern &lt;action&gt;:&lt;header|querystring|path&gt;.&lt;location&gt;. The action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html">Transforming API requests and responses</a>.</p>"""
    request_templates: NotRequired["capo_apigatewayv2.types.template_map.TemplateMap"]
    """<p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.</p>"""
    response_parameters: NotRequired[
        "capo_apigatewayv2.types.response_parameters.ResponseParameters"
    ]
    """<p>Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match pattern &lt;action&gt;:&lt;header&gt;.&lt;location&gt; or overwrite.statuscode. The action can be append, overwrite or remove. The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html">Transforming API requests and responses</a>.</p>"""
    template_selection_expression: NotRequired[
        "capo_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The template selection expression for the integration. Supported only for WebSocket APIs.</p>"""
    timeout_in_millis: NotRequired[
        "capo_apigatewayv2.types.integer_with_length_between50_and30000.IntegerWithLengthBetween50And30000"
    ]
    """<p>Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.</p>"""
    tls_config: NotRequired["capo_apigatewayv2.types.tls_config.TlsConfig"]
    """<p>The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationResult) -> dict:
    out: dict = {}
    if "api_gateway_managed" in value:
        out["apiGatewayManaged"] = value["api_gateway_managed"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "connection_type" in value:
        import capo_apigatewayv2.types.connection_type

        out["connectionType"] = capo_apigatewayv2.types.connection_type.serialize_json(
            value["connection_type"]
        )
    if "content_handling_strategy" in value:
        import capo_apigatewayv2.types.content_handling_strategy

        out["contentHandlingStrategy"] = (
            capo_apigatewayv2.types.content_handling_strategy.serialize_json(
                value["content_handling_strategy"]
            )
        )
    if "credentials_arn" in value:
        out["credentialsArn"] = value["credentials_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "integration_id" in value:
        out["integrationId"] = value["integration_id"]
    if "integration_method" in value:
        out["integrationMethod"] = value["integration_method"]
    if "integration_response_selection_expression" in value:
        out["integrationResponseSelectionExpression"] = value[
            "integration_response_selection_expression"
        ]
    if "integration_subtype" in value:
        out["integrationSubtype"] = value["integration_subtype"]
    if "integration_type" in value:
        import capo_apigatewayv2.types.integration_type

        out["integrationType"] = (
            capo_apigatewayv2.types.integration_type.serialize_json(
                value["integration_type"]
            )
        )
    if "integration_uri" in value:
        out["integrationUri"] = value["integration_uri"]
    if "passthrough_behavior" in value:
        import capo_apigatewayv2.types.passthrough_behavior

        out["passthroughBehavior"] = (
            capo_apigatewayv2.types.passthrough_behavior.serialize_json(
                value["passthrough_behavior"]
            )
        )
    if "payload_format_version" in value:
        out["payloadFormatVersion"] = value["payload_format_version"]
    if "request_parameters" in value:
        import capo_apigatewayv2.types.integration_parameters

        out["requestParameters"] = (
            capo_apigatewayv2.types.integration_parameters.serialize_json(
                value["request_parameters"]
            )
        )
    if "request_templates" in value:
        import capo_apigatewayv2.types.template_map

        out["requestTemplates"] = capo_apigatewayv2.types.template_map.serialize_json(
            value["request_templates"]
        )
    if "response_parameters" in value:
        import capo_apigatewayv2.types.response_parameters

        out["responseParameters"] = (
            capo_apigatewayv2.types.response_parameters.serialize_json(
                value["response_parameters"]
            )
        )
    if "template_selection_expression" in value:
        out["templateSelectionExpression"] = value["template_selection_expression"]
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
    if "tls_config" in value:
        import capo_apigatewayv2.types.tls_config

        out["tlsConfig"] = capo_apigatewayv2.types.tls_config.serialize_json(
            value["tls_config"]
        )
    return out


def deserialize_json(data: dict) -> GetIntegrationResult:
    out: GetIntegrationResult = {}  # type: ignore[typeddict-item]
    if data.get("apiGatewayManaged") is not None:
        out["api_gateway_managed"] = data["apiGatewayManaged"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("connectionType") is not None:
        import capo_apigatewayv2.types.connection_type

        out["connection_type"] = (
            capo_apigatewayv2.types.connection_type.deserialize_json(
                data["connectionType"]
            )
        )
    if data.get("contentHandlingStrategy") is not None:
        import capo_apigatewayv2.types.content_handling_strategy

        out["content_handling_strategy"] = (
            capo_apigatewayv2.types.content_handling_strategy.deserialize_json(
                data["contentHandlingStrategy"]
            )
        )
    if data.get("credentialsArn") is not None:
        out["credentials_arn"] = data["credentialsArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    if data.get("integrationMethod") is not None:
        out["integration_method"] = data["integrationMethod"]
    if data.get("integrationResponseSelectionExpression") is not None:
        out["integration_response_selection_expression"] = data[
            "integrationResponseSelectionExpression"
        ]
    if data.get("integrationSubtype") is not None:
        out["integration_subtype"] = data["integrationSubtype"]
    if data.get("integrationType") is not None:
        import capo_apigatewayv2.types.integration_type

        out["integration_type"] = (
            capo_apigatewayv2.types.integration_type.deserialize_json(
                data["integrationType"]
            )
        )
    if data.get("integrationUri") is not None:
        out["integration_uri"] = data["integrationUri"]
    if data.get("passthroughBehavior") is not None:
        import capo_apigatewayv2.types.passthrough_behavior

        out["passthrough_behavior"] = (
            capo_apigatewayv2.types.passthrough_behavior.deserialize_json(
                data["passthroughBehavior"]
            )
        )
    if data.get("payloadFormatVersion") is not None:
        out["payload_format_version"] = data["payloadFormatVersion"]
    if data.get("requestParameters") is not None:
        import capo_apigatewayv2.types.integration_parameters

        out["request_parameters"] = (
            capo_apigatewayv2.types.integration_parameters.deserialize_json(
                data["requestParameters"]
            )
        )
    if data.get("requestTemplates") is not None:
        import capo_apigatewayv2.types.template_map

        out["request_templates"] = (
            capo_apigatewayv2.types.template_map.deserialize_json(
                data["requestTemplates"]
            )
        )
    if data.get("responseParameters") is not None:
        import capo_apigatewayv2.types.response_parameters

        out["response_parameters"] = (
            capo_apigatewayv2.types.response_parameters.deserialize_json(
                data["responseParameters"]
            )
        )
    if data.get("templateSelectionExpression") is not None:
        out["template_selection_expression"] = data["templateSelectionExpression"]
    if data.get("timeoutInMillis") is not None:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    if data.get("tlsConfig") is not None:
        import capo_apigatewayv2.types.tls_config

        out["tls_config"] = capo_apigatewayv2.types.tls_config.deserialize_json(
            data["tlsConfig"]
        )
    return out
