"""Generated from Smithy shape ``com.amazonaws.deadline#ListFleetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.fleet_summaries
    import capo_deadline.types.next_token


class ListFleetsResponse(TypedDict, closed=True):
    fleets: "capo_deadline.types.fleet_summaries.FleetSummaries"
    """The fleets on the list."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: ListFleetsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.fleet_summaries

    out["fleets"] = capo_deadline.types.fleet_summaries.serialize_json(value["fleets"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFleetsResponse:
    out: ListFleetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("fleets") is not None:
        import capo_deadline.types.fleet_summaries

        out["fleets"] = capo_deadline.types.fleet_summaries.deserialize_json(
            data["fleets"]
        )
    else:
        out["fleets"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
