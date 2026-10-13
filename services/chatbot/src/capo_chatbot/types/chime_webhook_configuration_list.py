"""Generated from Smithy shape ``com.amazonaws.chatbot#ChimeWebhookConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.chime_webhook_configuration

ChimeWebhookConfigurationList: TypeAlias = list[
    "capo_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChimeWebhookConfigurationList) -> list:
    import capo_chatbot.types.chime_webhook_configuration

    out: list = []
    for item in value:
        out.append(capo_chatbot.types.chime_webhook_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChimeWebhookConfigurationList:
    import capo_chatbot.types.chime_webhook_configuration

    out: ChimeWebhookConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chatbot.types.chime_webhook_configuration.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ChimeWebhookConfigurationList) -> list[Any]:
    import capo_chatbot.types.chime_webhook_configuration

    return [
        capo_chatbot.types.chime_webhook_configuration.redact_sensitive(item)
        for item in value
    ]
