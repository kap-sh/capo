"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SystemPromptConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.system_prompt_configuration_bundle
    import capo_bedrock_agentcore.types.system_prompt_text


class SystemPromptConfigTextMember(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.system_prompt_text.SystemPromptText"


class SystemPromptConfigConfigurationBundleMember(TypedDict, closed=True):
    configurationBundle: "capo_bedrock_agentcore.types.system_prompt_configuration_bundle.SystemPromptConfigurationBundle"


SystemPromptConfig: TypeAlias = (
    SystemPromptConfigTextMember
    | SystemPromptConfigConfigurationBundleMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SystemPromptConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SystemPromptConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "configurationBundle" in value:
        import capo_bedrock_agentcore.types.system_prompt_configuration_bundle

        return {
            "configurationBundle": capo_bedrock_agentcore.types.system_prompt_configuration_bundle.serialize_json(
                value["configurationBundle"]
            )
        }
    else:
        raise SerializationError("SystemPromptConfig: no variant present")


def deserialize_json(data: dict) -> SystemPromptConfig:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("configurationBundle") is not None:
        import capo_bedrock_agentcore.types.system_prompt_configuration_bundle

        return {
            "configurationBundle": capo_bedrock_agentcore.types.system_prompt_configuration_bundle.deserialize_json(
                data["configurationBundle"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SystemPromptConfig: no recognized variant key")


def redact_sensitive(value: SystemPromptConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
