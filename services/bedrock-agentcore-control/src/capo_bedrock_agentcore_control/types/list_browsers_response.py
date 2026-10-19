"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListBrowsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_summaries
    import capo_bedrock_agentcore_control.types.next_token


class ListBrowsersResponse(TypedDict, closed=True):
    browser_summaries: (
        "capo_bedrock_agentcore_control.types.browser_summaries.BrowserSummaries"
    )
    """<p>The list of browser summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowsersResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.browser_summaries

    out["browserSummaries"] = (
        capo_bedrock_agentcore_control.types.browser_summaries.serialize_json(
            value["browser_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowsersResponse:
    out: ListBrowsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserSummaries") is not None:
        import capo_bedrock_agentcore_control.types.browser_summaries

        out["browser_summaries"] = (
            capo_bedrock_agentcore_control.types.browser_summaries.deserialize_json(
                data["browserSummaries"]
            )
        )
    else:
        out["browser_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListBrowsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "browser_summaries" in value:
        import capo_bedrock_agentcore_control.types.browser_summaries

        out["browser_summaries"] = (
            capo_bedrock_agentcore_control.types.browser_summaries.redact_sensitive(
                value["browser_summaries"]
            )
        )
    return out
