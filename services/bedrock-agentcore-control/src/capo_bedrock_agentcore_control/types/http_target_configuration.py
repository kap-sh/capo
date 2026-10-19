"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpTargetConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_connector_target_configuration
    import capo_bedrock_agentcore_control.types.passthrough_target_configuration
    import capo_bedrock_agentcore_control.types.runtime_target_configuration


class _HttpTargetConfiguration_agentcoreRuntime(TypedDict, closed=True):
    agentcoreRuntime: "capo_bedrock_agentcore_control.types.runtime_target_configuration.RuntimeTargetConfiguration"


class _HttpTargetConfiguration_passthrough(TypedDict, closed=True):
    passthrough: "capo_bedrock_agentcore_control.types.passthrough_target_configuration.PassthroughTargetConfiguration"


class _HttpTargetConfiguration_connector(TypedDict, closed=True):
    connector: "capo_bedrock_agentcore_control.types.http_connector_target_configuration.HttpConnectorTargetConfiguration"


HttpTargetConfiguration: TypeAlias = (
    _HttpTargetConfiguration_agentcoreRuntime
    | _HttpTargetConfiguration_passthrough
    | _HttpTargetConfiguration_connector
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HttpTargetConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HttpTargetConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "agentcoreRuntime" in value:
        import capo_bedrock_agentcore_control.types.runtime_target_configuration

        return {
            "agentcoreRuntime": capo_bedrock_agentcore_control.types.runtime_target_configuration.serialize_json(
                value["agentcoreRuntime"]
            )
        }
    elif "passthrough" in value:
        import capo_bedrock_agentcore_control.types.passthrough_target_configuration

        return {
            "passthrough": capo_bedrock_agentcore_control.types.passthrough_target_configuration.serialize_json(
                value["passthrough"]
            )
        }
    elif "connector" in value:
        import capo_bedrock_agentcore_control.types.http_connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.http_connector_target_configuration.serialize_json(
                value["connector"]
            )
        }
    else:
        raise SerializationError("HttpTargetConfiguration: no variant present")


def deserialize_json(data: dict) -> HttpTargetConfiguration:
    if data.get("agentcoreRuntime") is not None:
        import capo_bedrock_agentcore_control.types.runtime_target_configuration

        return {
            "agentcoreRuntime": capo_bedrock_agentcore_control.types.runtime_target_configuration.deserialize_json(
                data["agentcoreRuntime"]
            )
        }
    elif data.get("passthrough") is not None:
        import capo_bedrock_agentcore_control.types.passthrough_target_configuration

        return {
            "passthrough": capo_bedrock_agentcore_control.types.passthrough_target_configuration.deserialize_json(
                data["passthrough"]
            )
        }
    elif data.get("connector") is not None:
        import capo_bedrock_agentcore_control.types.http_connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.http_connector_target_configuration.deserialize_json(
                data["connector"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("HttpTargetConfiguration: no recognized variant key")


def redact_sensitive(
    value: HttpTargetConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "agentcoreRuntime" in value:
        import capo_bedrock_agentcore_control.types.runtime_target_configuration

        out["agentcoreRuntime"] = (
            capo_bedrock_agentcore_control.types.runtime_target_configuration.redact_sensitive(
                value["agentcoreRuntime"]
            )
        )
    if "passthrough" in value:
        import capo_bedrock_agentcore_control.types.passthrough_target_configuration

        out["passthrough"] = (
            capo_bedrock_agentcore_control.types.passthrough_target_configuration.redact_sensitive(
                value["passthrough"]
            )
        )
    return out
