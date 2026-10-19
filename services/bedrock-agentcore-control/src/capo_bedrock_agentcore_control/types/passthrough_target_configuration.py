"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PassthroughTargetConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_api_schema_configuration
    import capo_bedrock_agentcore_control.types.passthrough_endpoint
    import capo_bedrock_agentcore_control.types.passthrough_protocol_type
    import capo_bedrock_agentcore_control.types.static_query_parameter_conflict_resolution
    import capo_bedrock_agentcore_control.types.static_query_parameters
    import capo_bedrock_agentcore_control.types.stickiness_configuration


class PassthroughTargetConfiguration(TypedDict, closed=True):
    endpoint: (
        "capo_bedrock_agentcore_control.types.passthrough_endpoint.PassthroughEndpoint"
    )
    """<p>The HTTPS endpoint that the gateway forwards requests to for this passthrough target.</p>"""
    protocol_type: "capo_bedrock_agentcore_control.types.passthrough_protocol_type.PassthroughProtocolType"
    """<p>The application protocol that the passthrough target implements. This value is required for passthrough targets:</p> <ul> <li> <p> <code>MCP</code> - The Model Context Protocol.</p> </li> <li> <p> <code>A2A</code> - The Agent-to-Agent protocol.</p> </li> <li> <p> <code>INFERENCE</code> - The protocol for routing requests to a large language model (LLM) provider.</p> </li> <li> <p> <code>CUSTOM</code> - A custom application protocol.</p> </li> </ul>"""
    schema: NotRequired[
        "capo_bedrock_agentcore_control.types.http_api_schema_configuration.HttpApiSchemaConfiguration"
    ]
    """<p>The API schema configuration that defines the structure of the passthrough target's API.</p>"""
    stickiness_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.stickiness_configuration.StickinessConfiguration"
    ]
    """<p>The session stickiness configuration for the passthrough target. This configuration routes requests within the same session to the same target.</p>"""
    static_query_parameters: NotRequired[
        "capo_bedrock_agentcore_control.types.static_query_parameters.StaticQueryParameters"
    ]
    """<p>A map of static query parameters that the gateway always appends to the outbound URL when forwarding requests to the target. The total outbound URL length, which includes the endpoint and the percent-encoded query parameters, is enforced by the service.</p>"""
    static_query_parameter_conflict_resolution: NotRequired[
        "capo_bedrock_agentcore_control.types.static_query_parameter_conflict_resolution.StaticQueryParameterConflictResolution"
    ]
    """<p>Controls precedence when a client request supplies a query parameter whose name matches a configured static query parameter. If not set, defaults to <code>CLIENT_OVERRIDE</code>:</p> <ul> <li> <p> <code>CLIENT_OVERRIDE</code> - The client-supplied value overrides the configured static value for that parameter name.</p> </li> <li> <p> <code>STATIC_OVERRIDE</code> - The configured static value is retained, overriding the client-supplied value for that parameter name.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PassthroughTargetConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    import capo_bedrock_agentcore_control.types.passthrough_protocol_type

    out["protocolType"] = (
        capo_bedrock_agentcore_control.types.passthrough_protocol_type.serialize_json(
            value["protocol_type"]
        )
    )
    if "schema" in value:
        import capo_bedrock_agentcore_control.types.http_api_schema_configuration

        out["schema"] = (
            capo_bedrock_agentcore_control.types.http_api_schema_configuration.serialize_json(
                value["schema"]
            )
        )
    if "stickiness_configuration" in value:
        import capo_bedrock_agentcore_control.types.stickiness_configuration

        out["stickinessConfiguration"] = (
            capo_bedrock_agentcore_control.types.stickiness_configuration.serialize_json(
                value["stickiness_configuration"]
            )
        )
    if "static_query_parameters" in value:
        import capo_bedrock_agentcore_control.types.static_query_parameters

        out["staticQueryParameters"] = (
            capo_bedrock_agentcore_control.types.static_query_parameters.serialize_json(
                value["static_query_parameters"]
            )
        )
    if "static_query_parameter_conflict_resolution" in value:
        import capo_bedrock_agentcore_control.types.static_query_parameter_conflict_resolution

        out["staticQueryParameterConflictResolution"] = (
            capo_bedrock_agentcore_control.types.static_query_parameter_conflict_resolution.serialize_json(
                value["static_query_parameter_conflict_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> PassthroughTargetConfiguration:
    out: PassthroughTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("protocolType") is not None:
        import capo_bedrock_agentcore_control.types.passthrough_protocol_type

        out["protocol_type"] = (
            capo_bedrock_agentcore_control.types.passthrough_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    else:
        import typing

        out["protocol_type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.passthrough_protocol_type.PassthroughProtocolType",
            "",
        )
    if data.get("schema") is not None:
        import capo_bedrock_agentcore_control.types.http_api_schema_configuration

        out["schema"] = (
            capo_bedrock_agentcore_control.types.http_api_schema_configuration.deserialize_json(
                data["schema"]
            )
        )
    if data.get("stickinessConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.stickiness_configuration

        out["stickiness_configuration"] = (
            capo_bedrock_agentcore_control.types.stickiness_configuration.deserialize_json(
                data["stickinessConfiguration"]
            )
        )
    if data.get("staticQueryParameters") is not None:
        import capo_bedrock_agentcore_control.types.static_query_parameters

        out["static_query_parameters"] = (
            capo_bedrock_agentcore_control.types.static_query_parameters.deserialize_json(
                data["staticQueryParameters"]
            )
        )
    if data.get("staticQueryParameterConflictResolution") is not None:
        import capo_bedrock_agentcore_control.types.static_query_parameter_conflict_resolution

        out["static_query_parameter_conflict_resolution"] = (
            capo_bedrock_agentcore_control.types.static_query_parameter_conflict_resolution.deserialize_json(
                data["staticQueryParameterConflictResolution"]
            )
        )
    return out


def redact_sensitive(value: PassthroughTargetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "schema" in value:
        import capo_bedrock_agentcore_control.types.http_api_schema_configuration

        out["schema"] = (
            capo_bedrock_agentcore_control.types.http_api_schema_configuration.redact_sensitive(
                value["schema"]
            )
        )
    if "static_query_parameters" in value:
        import capo_bedrock_agentcore_control.types.static_query_parameters

        out["static_query_parameters"] = (
            capo_bedrock_agentcore_control.types.static_query_parameters.redact_sensitive(
                value["static_query_parameters"]
            )
        )
    return out
