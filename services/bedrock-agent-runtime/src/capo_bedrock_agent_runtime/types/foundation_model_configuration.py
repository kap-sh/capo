"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FoundationModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_foundation_model_configuration
    import capo_bedrock_agent_runtime.types.foundation_model_configuration_type
    import capo_bedrock_agent_runtime.types.mantle_foundation_model_configuration


class FoundationModelConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.foundation_model_configuration_type.FoundationModelConfigurationType"
    """<p>The type of foundation model configuration.</p>"""
    bedrock_foundation_model_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.bedrock_foundation_model_configuration.BedrockFoundationModelConfiguration"
    ]
    """<p>The Bedrock foundation model configuration.</p>"""
    mantle_foundation_model_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.mantle_foundation_model_configuration.MantleFoundationModelConfiguration"
    ]
    """<p>The Mantle foundation model configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.foundation_model_configuration_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.foundation_model_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "bedrock_foundation_model_configuration" in value:
        import capo_bedrock_agent_runtime.types.bedrock_foundation_model_configuration

        out["bedrockFoundationModelConfiguration"] = (
            capo_bedrock_agent_runtime.types.bedrock_foundation_model_configuration.serialize_json(
                value["bedrock_foundation_model_configuration"]
            )
        )
    if "mantle_foundation_model_configuration" in value:
        import capo_bedrock_agent_runtime.types.mantle_foundation_model_configuration

        out["mantleFoundationModelConfiguration"] = (
            capo_bedrock_agent_runtime.types.mantle_foundation_model_configuration.serialize_json(
                value["mantle_foundation_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FoundationModelConfiguration:
    out: FoundationModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.foundation_model_configuration_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.foundation_model_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("FoundationModelConfiguration.type required")
    if data.get("bedrockFoundationModelConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.bedrock_foundation_model_configuration

        out["bedrock_foundation_model_configuration"] = (
            capo_bedrock_agent_runtime.types.bedrock_foundation_model_configuration.deserialize_json(
                data["bedrockFoundationModelConfiguration"]
            )
        )
    if data.get("mantleFoundationModelConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.mantle_foundation_model_configuration

        out["mantle_foundation_model_configuration"] = (
            capo_bedrock_agent_runtime.types.mantle_foundation_model_configuration.deserialize_json(
                data["mantleFoundationModelConfiguration"]
            )
        )
    return out
