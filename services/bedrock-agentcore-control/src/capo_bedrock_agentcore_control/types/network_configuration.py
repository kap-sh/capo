"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.network_mode
    import capo_bedrock_agentcore_control.types.vpc_config


class NetworkConfiguration(TypedDict, closed=True):
    network_mode: "capo_bedrock_agentcore_control.types.network_mode.NetworkMode"
    """<p>The network mode for the AgentCore Runtime.</p>"""
    network_mode_config: NotRequired[
        "capo_bedrock_agentcore_control.types.vpc_config.VpcConfig"
    ]
    """<p>The network mode configuration for the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.network_mode

    out["networkMode"] = (
        capo_bedrock_agentcore_control.types.network_mode.serialize_json(
            value["network_mode"]
        )
    )
    if "network_mode_config" in value:
        import capo_bedrock_agentcore_control.types.vpc_config

        out["networkModeConfig"] = (
            capo_bedrock_agentcore_control.types.vpc_config.serialize_json(
                value["network_mode_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("networkMode") is not None:
        import capo_bedrock_agentcore_control.types.network_mode

        out["network_mode"] = (
            capo_bedrock_agentcore_control.types.network_mode.deserialize_json(
                data["networkMode"]
            )
        )
    else:
        import typing

        out["network_mode"] = typing.cast(
            "capo_bedrock_agentcore_control.types.network_mode.NetworkMode", ""
        )
    if data.get("networkModeConfig") is not None:
        import capo_bedrock_agentcore_control.types.vpc_config

        out["network_mode_config"] = (
            capo_bedrock_agentcore_control.types.vpc_config.deserialize_json(
                data["networkModeConfig"]
            )
        )
    return out
