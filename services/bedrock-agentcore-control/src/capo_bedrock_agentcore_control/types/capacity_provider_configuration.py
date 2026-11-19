"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_arn
    import capo_bedrock_agentcore_control.types.operating_system_configuration


class CapacityProviderConfiguration(TypedDict, closed=True):
    capacity_provider_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_provider_arn.CapacityProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the capacity provider to use for the AgentCore Runtime.</p>"""
    operating_system_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.operating_system_configuration.OperatingSystemConfiguration"
    ]
    """<p>The operating system configuration of the agents that Amazon Bedrock AgentCore Runtime runs on the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderConfiguration) -> dict:
    out: dict = {}
    if "capacity_provider_arn" in value:
        out["capacityProviderArn"] = value["capacity_provider_arn"]
    if "operating_system_configuration" in value:
        import capo_bedrock_agentcore_control.types.operating_system_configuration

        out["operatingSystemConfiguration"] = (
            capo_bedrock_agentcore_control.types.operating_system_configuration.serialize_json(
                value["operating_system_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityProviderConfiguration:
    out: CapacityProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["capacityProviderArn"]
    if data.get("operatingSystemConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.operating_system_configuration

        out["operating_system_configuration"] = (
            capo_bedrock_agentcore_control.types.operating_system_configuration.deserialize_json(
                data["operatingSystemConfiguration"]
            )
        )
    return out
