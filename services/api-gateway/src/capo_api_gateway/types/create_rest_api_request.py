"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateRestApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.api_key_source_type
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.endpoint_access_mode
    import capo_api_gateway.types.endpoint_configuration
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.security_policy
    import capo_api_gateway.types.string


class CreateRestApiRequest(TypedDict, closed=True):
    name: "capo_api_gateway.types.string.String"
    """<p>The name of the RestApi.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the RestApi.</p>"""
    version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A version identifier for the API.</p>"""
    clone_from: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ID of the RestApi that you want to clone from.</p>"""
    binary_media_types: NotRequired[
        "capo_api_gateway.types.list_of_string.ListOfString"
    ]
    """<p>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p>"""
    minimum_compression_size: NotRequired[
        "capo_api_gateway.types.nullable_integer.NullableInteger"
    ]
    """<p>A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.</p>"""
    api_key_source: NotRequired[
        "capo_api_gateway.types.api_key_source_type.ApiKeySourceType"
    ]
    """<p>The source of the API key for metering requests according to a usage plan. Valid values are: <code>HEADER</code> to read the API key from the <code>X-API-Key</code> header of a request. <code>AUTHORIZER</code> to read the API key from the <code>UsageIdentifierKey</code> from a custom authorizer.</p>"""
    endpoint_configuration: NotRequired[
        "capo_api_gateway.types.endpoint_configuration.EndpointConfiguration"
    ]
    """<p>The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API. </p>"""
    policy: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""
    disable_execute_api_endpoint: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>Specifies whether clients can invoke your API by using the default <code>execute-api</code> endpoint. By default, clients can invoke your API with the default <code>https://{api_id}.execute-api.{region}.amazonaws.com</code> endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint</p>"""
    security_policy: NotRequired[
        "capo_api_gateway.types.security_policy.SecurityPolicy"
    ]
    """<p> The Transport Layer Security (TLS) version + cipher suite for this RestApi. </p>"""
    endpoint_access_mode: NotRequired[
        "capo_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
    ]
    """<p> The endpoint access mode of the RestApi. Only available for RestApis that use security policies that start with <code>SecurityPolicy_</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestApiRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "version" in value:
        out["version"] = value["version"]
    if "clone_from" in value:
        out["cloneFrom"] = value["clone_from"]
    if "binary_media_types" in value:
        import capo_api_gateway.types.list_of_string

        out["binaryMediaTypes"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["binary_media_types"]
        )
    if "minimum_compression_size" in value:
        out["minimumCompressionSize"] = value["minimum_compression_size"]
    if "api_key_source" in value:
        import capo_api_gateway.types.api_key_source_type

        out["apiKeySource"] = capo_api_gateway.types.api_key_source_type.serialize_json(
            value["api_key_source"]
        )
    if "endpoint_configuration" in value:
        import capo_api_gateway.types.endpoint_configuration

        out["endpointConfiguration"] = (
            capo_api_gateway.types.endpoint_configuration.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "policy" in value:
        out["policy"] = value["policy"]
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    if "disable_execute_api_endpoint" in value:
        out["disableExecuteApiEndpoint"] = value["disable_execute_api_endpoint"]
    if "security_policy" in value:
        import capo_api_gateway.types.security_policy

        out["securityPolicy"] = capo_api_gateway.types.security_policy.serialize_json(
            value["security_policy"]
        )
    if "endpoint_access_mode" in value:
        import capo_api_gateway.types.endpoint_access_mode

        out["endpointAccessMode"] = (
            capo_api_gateway.types.endpoint_access_mode.serialize_json(
                value["endpoint_access_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRestApiRequest:
    out: CreateRestApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRestApiRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("cloneFrom") is not None:
        out["clone_from"] = data["cloneFrom"]
    if data.get("binaryMediaTypes") is not None:
        import capo_api_gateway.types.list_of_string

        out["binary_media_types"] = (
            capo_api_gateway.types.list_of_string.deserialize_json(
                data["binaryMediaTypes"]
            )
        )
    if data.get("minimumCompressionSize") is not None:
        out["minimum_compression_size"] = data["minimumCompressionSize"]
    if data.get("apiKeySource") is not None:
        import capo_api_gateway.types.api_key_source_type

        out["api_key_source"] = (
            capo_api_gateway.types.api_key_source_type.deserialize_json(
                data["apiKeySource"]
            )
        )
    if data.get("endpointConfiguration") is not None:
        import capo_api_gateway.types.endpoint_configuration

        out["endpoint_configuration"] = (
            capo_api_gateway.types.endpoint_configuration.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    if data.get("disableExecuteApiEndpoint") is not None:
        out["disable_execute_api_endpoint"] = data["disableExecuteApiEndpoint"]
    if data.get("securityPolicy") is not None:
        import capo_api_gateway.types.security_policy

        out["security_policy"] = (
            capo_api_gateway.types.security_policy.deserialize_json(
                data["securityPolicy"]
            )
        )
    if data.get("endpointAccessMode") is not None:
        import capo_api_gateway.types.endpoint_access_mode

        out["endpoint_access_mode"] = (
            capo_api_gateway.types.endpoint_access_mode.deserialize_json(
                data["endpointAccessMode"]
            )
        )
    return out
