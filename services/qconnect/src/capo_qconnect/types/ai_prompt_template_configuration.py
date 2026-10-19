"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptTemplateConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.text_full_ai_prompt_edit_template_configuration


class _AIPromptTemplateConfiguration_textFullAIPromptEditTemplateConfiguration(
    TypedDict, closed=True
):
    textFullAIPromptEditTemplateConfiguration: "capo_qconnect.types.text_full_ai_prompt_edit_template_configuration.TextFullAIPromptEditTemplateConfiguration"


AIPromptTemplateConfiguration: TypeAlias = (
    _AIPromptTemplateConfiguration_textFullAIPromptEditTemplateConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptTemplateConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AIPromptTemplateConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "textFullAIPromptEditTemplateConfiguration" in value:
        import capo_qconnect.types.text_full_ai_prompt_edit_template_configuration

        return {
            "textFullAIPromptEditTemplateConfiguration": capo_qconnect.types.text_full_ai_prompt_edit_template_configuration.serialize_json(
                value["textFullAIPromptEditTemplateConfiguration"]
            )
        }
    else:
        raise SerializationError("AIPromptTemplateConfiguration: no variant present")


def deserialize_json(data: dict) -> AIPromptTemplateConfiguration:
    if data.get("textFullAIPromptEditTemplateConfiguration") is not None:
        import capo_qconnect.types.text_full_ai_prompt_edit_template_configuration

        return {
            "textFullAIPromptEditTemplateConfiguration": capo_qconnect.types.text_full_ai_prompt_edit_template_configuration.deserialize_json(
                data["textFullAIPromptEditTemplateConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AIPromptTemplateConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: AIPromptTemplateConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "textFullAIPromptEditTemplateConfiguration" in value:
        import capo_qconnect.types.text_full_ai_prompt_edit_template_configuration

        out["textFullAIPromptEditTemplateConfiguration"] = (
            capo_qconnect.types.text_full_ai_prompt_edit_template_configuration.redact_sensitive(
                value["textFullAIPromptEditTemplateConfiguration"]
            )
        )
    return out
