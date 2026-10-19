"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.events
    import capo_devops_guru.types.uuid_next_token


class ListEventsResponse(TypedDict, closed=True):
    events: "capo_devops_guru.types.events.Events"
    """<p> A list of the requested events. </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsResponse) -> dict:
    out: dict = {}
    import capo_devops_guru.types.events

    out["Events"] = capo_devops_guru.types.events.serialize_json(value["events"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventsResponse:
    out: ListEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Events") is not None:
        import capo_devops_guru.types.events

        out["events"] = capo_devops_guru.types.events.deserialize_json(data["Events"])
    else:
        out["events"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
