"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServiceEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.service_event_list


class ListServiceEventsResponse(TypedDict, closed=True):
    events: "capo_resiliencehubv2.types.service_event_list.ServiceEventList"
    """<p>The list of service events.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceEventsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.service_event_list

    out["events"] = capo_resiliencehubv2.types.service_event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceEventsResponse:
    out: ListServiceEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_resiliencehubv2.types.service_event_list

        out["events"] = capo_resiliencehubv2.types.service_event_list.deserialize_json(
            data["events"]
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
