"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_interception_points
    import capo_bedrock_agentcore_control.types.interceptor_configuration
    import capo_bedrock_agentcore_control.types.interceptor_input_configuration


class GatewayInterceptorConfiguration(TypedDict, closed=True):
    interceptor: "capo_bedrock_agentcore_control.types.interceptor_configuration.InterceptorConfiguration"
    """<p>The infrastructure settings of an interceptor configuration. This structure defines how the interceptor can be invoked.</p>"""
    interception_points: "capo_bedrock_agentcore_control.types.gateway_interception_points.GatewayInterceptionPoints"
    """<p>The supported points of interception. This field specifies which points during the gateway invocation to invoke the interceptor</p>"""
    input_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.interceptor_input_configuration.InterceptorInputConfiguration"
    ]
    """<p>The configuration for the input of the interceptor. This field specifies how the input to the interceptor is constructed</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayInterceptorConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.interceptor_configuration

    out["interceptor"] = (
        capo_bedrock_agentcore_control.types.interceptor_configuration.serialize_json(
            value["interceptor"]
        )
    )
    import capo_bedrock_agentcore_control.types.gateway_interception_points

    out["interceptionPoints"] = (
        capo_bedrock_agentcore_control.types.gateway_interception_points.serialize_json(
            value["interception_points"]
        )
    )
    if "input_configuration" in value:
        import capo_bedrock_agentcore_control.types.interceptor_input_configuration

        out["inputConfiguration"] = (
            capo_bedrock_agentcore_control.types.interceptor_input_configuration.serialize_json(
                value["input_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GatewayInterceptorConfiguration:
    out: GatewayInterceptorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("interceptor") is not None:
        import capo_bedrock_agentcore_control.types.interceptor_configuration

        out["interceptor"] = (
            capo_bedrock_agentcore_control.types.interceptor_configuration.deserialize_json(
                data["interceptor"]
            )
        )
    else:
        out["interceptor"] = {"$unknown": {"name": ""}}
    if data.get("interceptionPoints") is not None:
        import capo_bedrock_agentcore_control.types.gateway_interception_points

        out["interception_points"] = (
            capo_bedrock_agentcore_control.types.gateway_interception_points.deserialize_json(
                data["interceptionPoints"]
            )
        )
    else:
        out["interception_points"] = []
    if data.get("inputConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.interceptor_input_configuration

        out["input_configuration"] = (
            capo_bedrock_agentcore_control.types.interceptor_input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    return out
