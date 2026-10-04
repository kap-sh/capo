"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.integration_id
    import capo_securityagent.types.webhook_secret


class UpdateIntegrationOutput(TypedDict, closed=True):
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The ID of the integration.</p>"""
    webhook_url: NotRequired["str"]
    """<p>The payload URL to configure on your provider instance. Returned when a webhook is created; unchanged by a rotate.</p>"""
    secret: NotRequired["capo_securityagent.types.webhook_secret.WebhookSecret"]
    """<p>The HMAC signing secret for the webhook. Returned only once, in this response; it is never returned again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationOutput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    if "webhook_url" in value:
        out["webhookUrl"] = value["webhook_url"]
    if "secret" in value:
        out["secret"] = value["secret"]
    return out


def deserialize_json(data: dict) -> UpdateIntegrationOutput:
    out: UpdateIntegrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("UpdateIntegrationOutput.integration_id required")
    if data.get("webhookUrl") is not None:
        out["webhook_url"] = data["webhookUrl"]
    if data.get("secret") is not None:
        out["secret"] = data["secret"]
    return out
