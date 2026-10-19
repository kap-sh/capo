"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_filters
    import capo_bedrock_agentcore_control.types.api_gateway_tool_overrides


class ApiGatewayToolConfiguration(TypedDict, closed=True):
    tool_overrides: NotRequired[
        "capo_bedrock_agentcore_control.types.api_gateway_tool_overrides.ApiGatewayToolOverrides"
    ]
    """<p>A list of explicit tool definitions with optional custom names and descriptions.</p>"""
    tool_filters: "capo_bedrock_agentcore_control.types.api_gateway_tool_filters.ApiGatewayToolFilters"
    """<p>A list of path and method patterns to expose as tools using metadata from the REST API's OpenAPI specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolConfiguration) -> dict:
    out: dict = {}
    if "tool_overrides" in value:
        import capo_bedrock_agentcore_control.types.api_gateway_tool_overrides

        out["toolOverrides"] = (
            capo_bedrock_agentcore_control.types.api_gateway_tool_overrides.serialize_json(
                value["tool_overrides"]
            )
        )
    import capo_bedrock_agentcore_control.types.api_gateway_tool_filters

    out["toolFilters"] = (
        capo_bedrock_agentcore_control.types.api_gateway_tool_filters.serialize_json(
            value["tool_filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiGatewayToolConfiguration:
    out: ApiGatewayToolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("toolOverrides") is not None:
        import capo_bedrock_agentcore_control.types.api_gateway_tool_overrides

        out["tool_overrides"] = (
            capo_bedrock_agentcore_control.types.api_gateway_tool_overrides.deserialize_json(
                data["toolOverrides"]
            )
        )
    if data.get("toolFilters") is not None:
        import capo_bedrock_agentcore_control.types.api_gateway_tool_filters

        out["tool_filters"] = (
            capo_bedrock_agentcore_control.types.api_gateway_tool_filters.deserialize_json(
                data["toolFilters"]
            )
        )
    else:
        out["tool_filters"] = []
    return out
