"""Generated from Smithy shape ``com.amazonaws.oam#ListAttachedLinksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.list_attached_links_max_results
    import capo_oam.types.next_token
    import capo_oam.types.resource_identifier


class ListAttachedLinksInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_oam.types.list_attached_links_max_results.ListAttachedLinksMaxResults"
    ]
    """<p>Limits the number of returned links to the specified number.</p>"""
    next_token: NotRequired["capo_oam.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. You received this token from a previous call.</p>"""
    sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the sink that you want to retrieve links for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedLinksInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["SinkIdentifier"] = value["sink_identifier"]
    return out


def deserialize_json(data: dict) -> ListAttachedLinksInput:
    out: ListAttachedLinksInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SinkIdentifier") is not None:
        out["sink_identifier"] = data["SinkIdentifier"]
    else:
        out["sink_identifier"] = ""
    return out
