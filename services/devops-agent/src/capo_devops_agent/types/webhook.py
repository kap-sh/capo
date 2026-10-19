"""Generated from Smithy shape ``com.amazonaws.devopsagent#Webhook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.webhook_type


class Webhook(TypedDict, closed=True):
    webhook_url: "str"
    """<p>Webhook endpoint URL.</p>"""
    webhook_type: NotRequired["capo_devops_agent.types.webhook_type.WebhookType"]
    """<p>Webhook authentication type.</p>"""
    webhook_id: "str"
    """<p>The unique identifier of the Webhook</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Webhook) -> dict:
    out: dict = {}
    out["webhookUrl"] = value["webhook_url"]
    if "webhook_type" in value:
        import capo_devops_agent.types.webhook_type

        out["webhookType"] = capo_devops_agent.types.webhook_type.serialize_json(
            value["webhook_type"]
        )
    out["webhookId"] = value["webhook_id"]
    return out


def deserialize_json(data: dict) -> Webhook:
    out: Webhook = {}  # type: ignore[typeddict-item]
    if data.get("webhookUrl") is not None:
        out["webhook_url"] = data["webhookUrl"]
    else:
        out["webhook_url"] = ""
    if data.get("webhookType") is not None:
        import capo_devops_agent.types.webhook_type

        out["webhook_type"] = capo_devops_agent.types.webhook_type.deserialize_json(
            data["webhookType"]
        )
    if data.get("webhookId") is not None:
        out["webhook_id"] = data["webhookId"]
    else:
        out["webhook_id"] = ""
    return out
