"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceTargetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_connector_target_configuration
    import capo_bedrock_agentcore_control.types.inference_provider_target_configuration


class _InferenceTargetConfiguration_connector(TypedDict, closed=True):
    connector: "capo_bedrock_agentcore_control.types.inference_connector_target_configuration.InferenceConnectorTargetConfiguration"


class _InferenceTargetConfiguration_provider(TypedDict, closed=True):
    provider: "capo_bedrock_agentcore_control.types.inference_provider_target_configuration.InferenceProviderTargetConfiguration"


InferenceTargetConfiguration: TypeAlias = (
    _InferenceTargetConfiguration_connector
    | _InferenceTargetConfiguration_provider
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: InferenceTargetConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"InferenceTargetConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "connector" in value:
        import capo_bedrock_agentcore_control.types.inference_connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.inference_connector_target_configuration.serialize_json(
                value["connector"]
            )
        }
    elif "provider" in value:
        import capo_bedrock_agentcore_control.types.inference_provider_target_configuration

        return {
            "provider": capo_bedrock_agentcore_control.types.inference_provider_target_configuration.serialize_json(
                value["provider"]
            )
        }
    else:
        raise SerializationError("InferenceTargetConfiguration: no variant present")


def deserialize_json(data: dict) -> InferenceTargetConfiguration:
    if data.get("connector") is not None:
        import capo_bedrock_agentcore_control.types.inference_connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.inference_connector_target_configuration.deserialize_json(
                data["connector"]
            )
        }
    elif data.get("provider") is not None:
        import capo_bedrock_agentcore_control.types.inference_provider_target_configuration

        return {
            "provider": capo_bedrock_agentcore_control.types.inference_provider_target_configuration.deserialize_json(
                data["provider"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "InferenceTargetConfiguration: no recognized variant key"
        )
