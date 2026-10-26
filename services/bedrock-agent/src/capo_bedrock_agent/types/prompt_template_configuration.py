"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptTemplateConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.chat_prompt_template_configuration
    import capo_bedrock_agent.types.text_prompt_template_configuration


class _PromptTemplateConfiguration_text(TypedDict, closed=True):
    text: "capo_bedrock_agent.types.text_prompt_template_configuration.TextPromptTemplateConfiguration"


class _PromptTemplateConfiguration_chat(TypedDict, closed=True):
    chat: "capo_bedrock_agent.types.chat_prompt_template_configuration.ChatPromptTemplateConfiguration"


PromptTemplateConfiguration: TypeAlias = (
    _PromptTemplateConfiguration_text
    | _PromptTemplateConfiguration_chat
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PromptTemplateConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PromptTemplateConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        import capo_bedrock_agent.types.text_prompt_template_configuration

        return {
            "text": capo_bedrock_agent.types.text_prompt_template_configuration.serialize_json(
                value["text"]
            )
        }
    elif "chat" in value:
        import capo_bedrock_agent.types.chat_prompt_template_configuration

        return {
            "chat": capo_bedrock_agent.types.chat_prompt_template_configuration.serialize_json(
                value["chat"]
            )
        }
    else:
        raise SerializationError("PromptTemplateConfiguration: no variant present")


def deserialize_json(data: dict) -> PromptTemplateConfiguration:
    if data.get("text") is not None:
        import capo_bedrock_agent.types.text_prompt_template_configuration

        return {
            "text": capo_bedrock_agent.types.text_prompt_template_configuration.deserialize_json(
                data["text"]
            )
        }
    elif data.get("chat") is not None:
        import capo_bedrock_agent.types.chat_prompt_template_configuration

        return {
            "chat": capo_bedrock_agent.types.chat_prompt_template_configuration.deserialize_json(
                data["chat"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PromptTemplateConfiguration: no recognized variant key"
        )


def redact_sensitive(value: PromptTemplateConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "chat" in value:
        out["chat"] = "*** Sensitive Data Redacted ***"
    return out
