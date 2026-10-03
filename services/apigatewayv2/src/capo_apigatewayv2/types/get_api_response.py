"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetApiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.__list_of__string
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.__timestamp_iso8601
    import capo_apigatewayv2.types.cors
    import capo_apigatewayv2.types.id
    import capo_apigatewayv2.types.ip_address_type
    import capo_apigatewayv2.types.protocol_type
    import capo_apigatewayv2.types.selection_expression
    import capo_apigatewayv2.types.string_with_length_between0_and1024
    import capo_apigatewayv2.types.string_with_length_between1_and64
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.tags


class GetApiResponse(TypedDict, closed=True):
    api_endpoint: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.</p>"""
    api_gateway_managed: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether an API is managed by API Gateway. You can't update or delete a managed API by using API Gateway. A managed API can be deleted only through the tooling or service that created it.</p>"""
    api_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>The API ID.</p>"""
    api_key_selection_expression: NotRequired[
        "capo_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>An API key selection expression. Supported only for WebSocket APIs. See <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API Key Selection Expressions</a>.</p>"""
    cors_configuration: NotRequired["capo_apigatewayv2.types.cors.Cors"]
    """<p>A CORS configuration. Supported only for HTTP APIs.</p>"""
    created_date: NotRequired[
        "capo_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the API was created.</p>"""
    description: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description of the API.</p>"""
    disable_schema_validation: NotRequired[
        "capo_apigatewayv2.types.__boolean.__boolean"
    ]
    """<p>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</p>"""
    disable_execute_api_endpoint: NotRequired[
        "capo_apigatewayv2.types.__boolean.__boolean"
    ]
    """<p>Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>"""
    import_info: NotRequired[
        "capo_apigatewayv2.types.__list_of__string.__listOf__string"
    ]
    """<p>The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.</p>"""
    ip_address_type: NotRequired[
        "capo_apigatewayv2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address types that can invoke the API.</p>"""
    name: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the API.</p>"""
    protocol_type: NotRequired["capo_apigatewayv2.types.protocol_type.ProtocolType"]
    """<p>The API protocol.</p>"""
    route_selection_expression: NotRequired[
        "capo_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>"""
    tags: NotRequired["capo_apigatewayv2.types.tags.Tags"]
    """<p>A collection of tags associated with the API.</p>"""
    version: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>A version identifier for the API.</p>"""
    warnings: NotRequired["capo_apigatewayv2.types.__list_of__string.__listOf__string"]
    """<p>The warning messages reported when failonwarnings is turned on during API import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiResponse) -> dict:
    out: dict = {}
    if "api_endpoint" in value:
        out["apiEndpoint"] = value["api_endpoint"]
    if "api_gateway_managed" in value:
        out["apiGatewayManaged"] = value["api_gateway_managed"]
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "api_key_selection_expression" in value:
        out["apiKeySelectionExpression"] = value["api_key_selection_expression"]
    if "cors_configuration" in value:
        import capo_apigatewayv2.types.cors

        out["corsConfiguration"] = capo_apigatewayv2.types.cors.serialize_json(
            value["cors_configuration"]
        )
    if "created_date" in value:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["createdDate"] = capo_apigatewayv2.types.__timestamp_iso8601.serialize_json(
            value["created_date"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "disable_schema_validation" in value:
        out["disableSchemaValidation"] = value["disable_schema_validation"]
    if "disable_execute_api_endpoint" in value:
        out["disableExecuteApiEndpoint"] = value["disable_execute_api_endpoint"]
    if "import_info" in value:
        import capo_apigatewayv2.types.__list_of__string

        out["importInfo"] = capo_apigatewayv2.types.__list_of__string.serialize_json(
            value["import_info"]
        )
    if "ip_address_type" in value:
        import capo_apigatewayv2.types.ip_address_type

        out["ipAddressType"] = capo_apigatewayv2.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "protocol_type" in value:
        import capo_apigatewayv2.types.protocol_type

        out["protocolType"] = capo_apigatewayv2.types.protocol_type.serialize_json(
            value["protocol_type"]
        )
    if "route_selection_expression" in value:
        out["routeSelectionExpression"] = value["route_selection_expression"]
    if "tags" in value:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.serialize_json(value["tags"])
    if "version" in value:
        out["version"] = value["version"]
    if "warnings" in value:
        import capo_apigatewayv2.types.__list_of__string

        out["warnings"] = capo_apigatewayv2.types.__list_of__string.serialize_json(
            value["warnings"]
        )
    return out


def deserialize_json(data: dict) -> GetApiResponse:
    out: GetApiResponse = {}  # type: ignore[typeddict-item]
    if data.get("apiEndpoint") is not None:
        out["api_endpoint"] = data["apiEndpoint"]
    if data.get("apiGatewayManaged") is not None:
        out["api_gateway_managed"] = data["apiGatewayManaged"]
    if data.get("apiId") is not None:
        out["api_id"] = data["apiId"]
    if data.get("apiKeySelectionExpression") is not None:
        out["api_key_selection_expression"] = data["apiKeySelectionExpression"]
    if data.get("corsConfiguration") is not None:
        import capo_apigatewayv2.types.cors

        out["cors_configuration"] = capo_apigatewayv2.types.cors.deserialize_json(
            data["corsConfiguration"]
        )
    if data.get("createdDate") is not None:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["created_date"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["createdDate"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("disableSchemaValidation") is not None:
        out["disable_schema_validation"] = data["disableSchemaValidation"]
    if data.get("disableExecuteApiEndpoint") is not None:
        out["disable_execute_api_endpoint"] = data["disableExecuteApiEndpoint"]
    if data.get("importInfo") is not None:
        import capo_apigatewayv2.types.__list_of__string

        out["import_info"] = capo_apigatewayv2.types.__list_of__string.deserialize_json(
            data["importInfo"]
        )
    if data.get("ipAddressType") is not None:
        import capo_apigatewayv2.types.ip_address_type

        out["ip_address_type"] = (
            capo_apigatewayv2.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("protocolType") is not None:
        import capo_apigatewayv2.types.protocol_type

        out["protocol_type"] = capo_apigatewayv2.types.protocol_type.deserialize_json(
            data["protocolType"]
        )
    if data.get("routeSelectionExpression") is not None:
        out["route_selection_expression"] = data["routeSelectionExpression"]
    if data.get("tags") is not None:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.deserialize_json(data["tags"])
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("warnings") is not None:
        import capo_apigatewayv2.types.__list_of__string

        out["warnings"] = capo_apigatewayv2.types.__list_of__string.deserialize_json(
            data["warnings"]
        )
    return out
