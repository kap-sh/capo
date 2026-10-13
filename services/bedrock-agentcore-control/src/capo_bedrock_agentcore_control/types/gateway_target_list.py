"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayTargetList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_target

GatewayTargetList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.gateway_target.GatewayTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayTargetList) -> list:
    import capo_bedrock_agentcore_control.types.gateway_target

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_target.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GatewayTargetList:
    import capo_bedrock_agentcore_control.types.gateway_target

    out: GatewayTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.gateway_target.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GatewayTargetList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.gateway_target

    return [
        capo_bedrock_agentcore_control.types.gateway_target.redact_sensitive(item)
        for item in value
    ]
