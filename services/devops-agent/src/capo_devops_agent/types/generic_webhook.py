"""Generated from Smithy shape ``com.amazonaws.devopsagent#GenericWebhook``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.api_key_value
    import capo_devops_agent.types.webhook_secret
    import capo_devops_agent.types.webhook_type


class GenericWebhook(TypedDict, closed=True):
    webhook_url: NotRequired["str"]
    """<p>The webhook URL endpoint</p>"""
    webhook_id: NotRequired["str"]
    """<p>The unique webhook identifier</p>"""
    webhook_type: NotRequired["capo_devops_agent.types.webhook_type.WebhookType"]
    """<p>The webhook authentication type</p>"""
    webhook_secret: NotRequired["capo_devops_agent.types.webhook_secret.WebhookSecret"]
    """<p>The webhook secret for authentication</p>"""
    api_key: NotRequired["capo_devops_agent.types.api_key_value.ApiKeyValue"]
    """<p>API Key for API Key webhook authentication</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenericWebhook) -> dict:
    out: dict = {}
    if "webhook_url" in value:
        out["webhookUrl"] = value["webhook_url"]
    if "webhook_id" in value:
        out["webhookId"] = value["webhook_id"]
    if "webhook_type" in value:
        import capo_devops_agent.types.webhook_type

        out["webhookType"] = capo_devops_agent.types.webhook_type.serialize_json(
            value["webhook_type"]
        )
    if "webhook_secret" in value:
        out["webhookSecret"] = value["webhook_secret"]
    if "api_key" in value:
        out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> GenericWebhook:
    out: GenericWebhook = {}  # type: ignore[typeddict-item]
    if data.get("webhookUrl") is not None:
        out["webhook_url"] = data["webhookUrl"]
    if data.get("webhookId") is not None:
        out["webhook_id"] = data["webhookId"]
    if data.get("webhookType") is not None:
        import capo_devops_agent.types.webhook_type

        out["webhook_type"] = capo_devops_agent.types.webhook_type.deserialize_json(
            data["webhookType"]
        )
    if data.get("webhookSecret") is not None:
        out["webhook_secret"] = data["webhookSecret"]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    return out


def redact_sensitive(value: GenericWebhook) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "webhook_secret" in value:
        out["webhook_secret"] = "*** Sensitive Data Redacted ***"
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    return out
