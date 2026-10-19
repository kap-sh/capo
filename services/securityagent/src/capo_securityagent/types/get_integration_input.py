"""Generated from Smithy shape ``com.amazonaws.securityagent#GetIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.integration_id


class GetIntegrationInput(TypedDict, closed=True):
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationInput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    return out


def deserialize_json(data: dict) -> GetIntegrationInput:
    out: GetIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    return out
