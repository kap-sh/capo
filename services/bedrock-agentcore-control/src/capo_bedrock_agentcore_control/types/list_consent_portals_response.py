"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListConsentPortalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_summaries


class ListConsentPortalsResponse(TypedDict, closed=True):
    consent_portals: "capo_bedrock_agentcore_control.types.consent_portal_summaries.ConsentPortalSummaries"
    """<p>The list of consent portals.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConsentPortalsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.consent_portal_summaries

    out["consentPortals"] = (
        capo_bedrock_agentcore_control.types.consent_portal_summaries.serialize_json(
            value["consent_portals"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConsentPortalsResponse:
    out: ListConsentPortalsResponse = {}  # type: ignore[typeddict-item]
    if data.get("consentPortals") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_summaries

        out["consent_portals"] = (
            capo_bedrock_agentcore_control.types.consent_portal_summaries.deserialize_json(
                data["consentPortals"]
            )
        )
    else:
        out["consent_portals"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
