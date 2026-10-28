"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_target_configuration
    import capo_bedrock_agentcore_control.types.inference_target_configuration
    import capo_bedrock_agentcore_control.types.mcp_target_configuration


class TargetConfigurationMcpMember(TypedDict, closed=True):
    mcp: "capo_bedrock_agentcore_control.types.mcp_target_configuration.McpTargetConfiguration"


class TargetConfigurationHttpMember(TypedDict, closed=True):
    http: "capo_bedrock_agentcore_control.types.http_target_configuration.HttpTargetConfiguration"


class TargetConfigurationInferenceMember(TypedDict, closed=True):
    inference: "capo_bedrock_agentcore_control.types.inference_target_configuration.InferenceTargetConfiguration"


TargetConfiguration: TypeAlias = (
    TargetConfigurationMcpMember
    | TargetConfigurationHttpMember
    | TargetConfigurationInferenceMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TargetConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TargetConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "mcp" in value:
        import capo_bedrock_agentcore_control.types.mcp_target_configuration

        return {
            "mcp": capo_bedrock_agentcore_control.types.mcp_target_configuration.serialize_json(
                value["mcp"]
            )
        }
    elif "http" in value:
        import capo_bedrock_agentcore_control.types.http_target_configuration

        return {
            "http": capo_bedrock_agentcore_control.types.http_target_configuration.serialize_json(
                value["http"]
            )
        }
    elif "inference" in value:
        import capo_bedrock_agentcore_control.types.inference_target_configuration

        return {
            "inference": capo_bedrock_agentcore_control.types.inference_target_configuration.serialize_json(
                value["inference"]
            )
        }
    else:
        raise SerializationError("TargetConfiguration: no variant present")


def deserialize_json(data: dict) -> TargetConfiguration:
    if data.get("mcp") is not None:
        import capo_bedrock_agentcore_control.types.mcp_target_configuration

        return {
            "mcp": capo_bedrock_agentcore_control.types.mcp_target_configuration.deserialize_json(
                data["mcp"]
            )
        }
    elif data.get("http") is not None:
        import capo_bedrock_agentcore_control.types.http_target_configuration

        return {
            "http": capo_bedrock_agentcore_control.types.http_target_configuration.deserialize_json(
                data["http"]
            )
        }
    elif data.get("inference") is not None:
        import capo_bedrock_agentcore_control.types.inference_target_configuration

        return {
            "inference": capo_bedrock_agentcore_control.types.inference_target_configuration.deserialize_json(
                data["inference"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TargetConfiguration: no recognized variant key")


def redact_sensitive(value: TargetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mcp" in value:
        import capo_bedrock_agentcore_control.types.mcp_target_configuration

        out["mcp"] = (
            capo_bedrock_agentcore_control.types.mcp_target_configuration.redact_sensitive(
                value["mcp"]
            )
        )
    if "http" in value:
        import capo_bedrock_agentcore_control.types.http_target_configuration

        out["http"] = (
            capo_bedrock_agentcore_control.types.http_target_configuration.redact_sensitive(
                value["http"]
            )
        )
    return out
