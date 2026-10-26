"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.static_override
    import capo_bedrock_agentcore_control.types.weighted_override


class _ConfigurationBundleAction_staticOverride(TypedDict, closed=True):
    staticOverride: (
        "capo_bedrock_agentcore_control.types.static_override.StaticOverride"
    )


class _ConfigurationBundleAction_weightedOverride(TypedDict, closed=True):
    weightedOverride: (
        "capo_bedrock_agentcore_control.types.weighted_override.WeightedOverride"
    )


ConfigurationBundleAction: TypeAlias = (
    _ConfigurationBundleAction_staticOverride
    | _ConfigurationBundleAction_weightedOverride
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigurationBundleAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "staticOverride" in value:
        import capo_bedrock_agentcore_control.types.static_override

        return {
            "staticOverride": capo_bedrock_agentcore_control.types.static_override.serialize_json(
                value["staticOverride"]
            )
        }
    elif "weightedOverride" in value:
        import capo_bedrock_agentcore_control.types.weighted_override

        return {
            "weightedOverride": capo_bedrock_agentcore_control.types.weighted_override.serialize_json(
                value["weightedOverride"]
            )
        }
    else:
        raise SerializationError("ConfigurationBundleAction: no variant present")


def deserialize_json(data: dict) -> ConfigurationBundleAction:
    if data.get("staticOverride") is not None:
        import capo_bedrock_agentcore_control.types.static_override

        return {
            "staticOverride": capo_bedrock_agentcore_control.types.static_override.deserialize_json(
                data["staticOverride"]
            )
        }
    elif data.get("weightedOverride") is not None:
        import capo_bedrock_agentcore_control.types.weighted_override

        return {
            "weightedOverride": capo_bedrock_agentcore_control.types.weighted_override.deserialize_json(
                data["weightedOverride"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ConfigurationBundleAction: no recognized variant key"
        )
