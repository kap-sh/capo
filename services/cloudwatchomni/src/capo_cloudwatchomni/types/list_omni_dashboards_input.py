"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListOmniDashboardsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.next_token
    import capo_cloudwatchomni.types.space_id


class ListOmniDashboardsInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    name_prefix: NotRequired["str"]
    """Filter to dashboards whose name starts with this prefix."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of dashboards to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOmniDashboardsInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "name_prefix" in value:
        out["namePrefix"] = value["name_prefix"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListOmniDashboardsInput:
    out: ListOmniDashboardsInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("namePrefix") is not None:
        out["name_prefix"] = data["namePrefix"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
