"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetConsentPortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_identifier


class GetConsentPortalRequest(TypedDict, closed=True):
    consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier"
    """<p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConsentPortalRequest) -> dict:
    out: dict = {}
    out["consentPortalIdentifier"] = value["consent_portal_identifier"]
    return out


def deserialize_json(data: dict) -> GetConsentPortalRequest:
    out: GetConsentPortalRequest = {}  # type: ignore[typeddict-item]
    if data.get("consentPortalIdentifier") is not None:
        out["consent_portal_identifier"] = data["consentPortalIdentifier"]
    else:
        out["consent_portal_identifier"] = ""
    return out
