"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.integration_id


class CreateIntegrationOutput(TypedDict, closed=True):
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the created integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationOutput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationOutput:
    out: CreateIntegrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    return out
