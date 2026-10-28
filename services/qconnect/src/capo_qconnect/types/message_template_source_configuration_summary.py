"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSourceConfigurationSummary``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.whats_app_message_template_source_configuration_summary


class MessageTemplateSourceConfigurationSummaryWhatsAppMember(TypedDict, closed=True):
    whatsApp: "capo_qconnect.types.whats_app_message_template_source_configuration_summary.WhatsAppMessageTemplateSourceConfigurationSummary"


MessageTemplateSourceConfigurationSummary: TypeAlias = (
    MessageTemplateSourceConfigurationSummaryWhatsAppMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSourceConfigurationSummary) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MessageTemplateSourceConfigurationSummary: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "whatsApp" in value:
        import capo_qconnect.types.whats_app_message_template_source_configuration_summary

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_source_configuration_summary.serialize_json(
                value["whatsApp"]
            )
        }
    else:
        raise SerializationError(
            "MessageTemplateSourceConfigurationSummary: no variant present"
        )


def deserialize_json(data: dict) -> MessageTemplateSourceConfigurationSummary:
    if data.get("whatsApp") is not None:
        import capo_qconnect.types.whats_app_message_template_source_configuration_summary

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_source_configuration_summary.deserialize_json(
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
            "MessageTemplateSourceConfigurationSummary: no recognized variant key"
        )


def redact_sensitive(
    value: MessageTemplateSourceConfigurationSummary,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "whatsApp" in value:
        import capo_qconnect.types.whats_app_message_template_source_configuration_summary

        out["whatsApp"] = (
            capo_qconnect.types.whats_app_message_template_source_configuration_summary.redact_sensitive(
                value["whatsApp"]
            )
        )
    return out
