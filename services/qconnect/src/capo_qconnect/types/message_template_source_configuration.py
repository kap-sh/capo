"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.whats_app_message_template_source_configuration


class MessageTemplateSourceConfigurationWhatsAppMember(TypedDict, closed=True):
    whatsApp: "capo_qconnect.types.whats_app_message_template_source_configuration.WhatsAppMessageTemplateSourceConfiguration"


MessageTemplateSourceConfiguration: TypeAlias = (
    MessageTemplateSourceConfigurationWhatsAppMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MessageTemplateSourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "whatsApp" in value:
        import capo_qconnect.types.whats_app_message_template_source_configuration

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_source_configuration.serialize_json(
                value["whatsApp"]
            )
        }
    else:
        raise SerializationError(
            "MessageTemplateSourceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MessageTemplateSourceConfiguration:
    if data.get("whatsApp") is not None:
        import capo_qconnect.types.whats_app_message_template_source_configuration

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_source_configuration.deserialize_json(
                data["whatsApp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MessageTemplateSourceConfiguration: no recognized variant key"
        )
