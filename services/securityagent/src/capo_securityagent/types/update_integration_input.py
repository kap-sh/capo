"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.integration_id
    import capo_securityagent.types.webhook_action


class UpdateIntegrationInput(TypedDict, closed=True):
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The ID of the integration whose webhook you want to create or rotate.</p>"""
    webhook_action: "capo_securityagent.types.webhook_action.WebhookAction"
    """<p>The action to perform on the integration's webhook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationInput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    import capo_securityagent.types.webhook_action

    out["webhookAction"] = capo_securityagent.types.webhook_action.serialize_json(
        value["webhook_action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIntegrationInput:
    out: UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("UpdateIntegrationInput.integration_id required")
    if data.get("webhookAction") is not None:
        import capo_securityagent.types.webhook_action

        out["webhook_action"] = (
            capo_securityagent.types.webhook_action.deserialize_json(
                data["webhookAction"]
            )
        )
    else:
        raise DeserializationError("UpdateIntegrationInput.webhook_action required")
    return out
