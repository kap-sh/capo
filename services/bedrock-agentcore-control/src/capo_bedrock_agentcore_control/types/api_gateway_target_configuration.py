"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_configuration


class ApiGatewayTargetConfiguration(TypedDict, closed=True):
    rest_api_id: "str"
    """<p>The ID of the API Gateway REST API.</p>"""
    stage: "str"
    """<p>The ID of the stage of the REST API to add as a target.</p>"""
    api_gateway_tool_configuration: "capo_bedrock_agentcore_control.types.api_gateway_tool_configuration.ApiGatewayToolConfiguration"
    """<p>The configuration for defining REST API tool filters and overrides for the gateway target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayTargetConfiguration) -> dict:
    out: dict = {}
    out["restApiId"] = value["rest_api_id"]
    out["stage"] = value["stage"]
    import capo_bedrock_agentcore_control.types.api_gateway_tool_configuration

    out["apiGatewayToolConfiguration"] = (
        capo_bedrock_agentcore_control.types.api_gateway_tool_configuration.serialize_json(
            value["api_gateway_tool_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiGatewayTargetConfiguration:
    out: ApiGatewayTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("restApiId") is not None:
        out["rest_api_id"] = data["restApiId"]
    else:
        out["rest_api_id"] = ""
    if data.get("stage") is not None:
        out["stage"] = data["stage"]
    else:
        out["stage"] = ""
    if data.get("apiGatewayToolConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.api_gateway_tool_configuration

        out["api_gateway_tool_configuration"] = (
            capo_bedrock_agentcore_control.types.api_gateway_tool_configuration.deserialize_json(
                data["apiGatewayToolConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ApiGatewayTargetConfiguration.api_gateway_tool_configuration required"
        )
    return out
