"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chime_webhook_configuration


class CreateChimeWebhookConfigurationResult(TypedDict, closed=True):
    webhook_configuration: NotRequired[
        "capo_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration"
    ]
    """<p>An Amazon Chime webhook configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChimeWebhookConfigurationResult) -> dict:
    out: dict = {}
    if "webhook_configuration" in value:
        import capo_chatbot.types.chime_webhook_configuration

        out["WebhookConfiguration"] = (
            capo_chatbot.types.chime_webhook_configuration.serialize_json(
                value["webhook_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateChimeWebhookConfigurationResult:
    out: CreateChimeWebhookConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("WebhookConfiguration") is not None:
        import capo_chatbot.types.chime_webhook_configuration

        out["webhook_configuration"] = (
            capo_chatbot.types.chime_webhook_configuration.deserialize_json(
                data["WebhookConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateChimeWebhookConfigurationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "webhook_configuration" in value:
        import capo_chatbot.types.chime_webhook_configuration

        out["webhook_configuration"] = (
            capo_chatbot.types.chime_webhook_configuration.redact_sensitive(
                value["webhook_configuration"]
            )
        )
    return out
