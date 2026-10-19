"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListAccessProfilesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.next_token
    import capo_cloudwatchomni.types.space_id


class ListAccessProfilesInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of access profiles to return per page. Defaults to 100."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAccessProfilesInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListAccessProfilesInput:
    out: ListAccessProfilesInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
