"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListBrowserProfilesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_summaries
    import capo_bedrock_agentcore_control.types.next_token


class ListBrowserProfilesResponse(TypedDict, closed=True):
    profile_summaries: "capo_bedrock_agentcore_control.types.browser_profile_summaries.BrowserProfileSummaries"
    """<p>The list of browser profile summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserProfilesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.browser_profile_summaries

    out["profileSummaries"] = (
        capo_bedrock_agentcore_control.types.browser_profile_summaries.serialize_json(
            value["profile_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowserProfilesResponse:
    out: ListBrowserProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileSummaries") is not None:
        import capo_bedrock_agentcore_control.types.browser_profile_summaries

        out["profile_summaries"] = (
            capo_bedrock_agentcore_control.types.browser_profile_summaries.deserialize_json(
                data["profileSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListBrowserProfilesResponse.profile_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListBrowserProfilesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "profile_summaries" in value:
        import capo_bedrock_agentcore_control.types.browser_profile_summaries

        out["profile_summaries"] = (
            capo_bedrock_agentcore_control.types.browser_profile_summaries.redact_sensitive(
                value["profile_summaries"]
            )
        )
    return out
