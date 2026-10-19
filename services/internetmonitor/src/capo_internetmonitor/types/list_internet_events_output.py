"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListInternetEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.internet_events_list


class ListInternetEventsOutput(TypedDict, closed=True):
    internet_events: (
        "capo_internetmonitor.types.internet_events_list.InternetEventsList"
    )
    """<p>A set of internet events returned for the list operation.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInternetEventsOutput) -> dict:
    out: dict = {}
    import capo_internetmonitor.types.internet_events_list

    out["InternetEvents"] = (
        capo_internetmonitor.types.internet_events_list.serialize_json(
            value["internet_events"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInternetEventsOutput:
    out: ListInternetEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("InternetEvents") is not None:
        import capo_internetmonitor.types.internet_events_list

        out["internet_events"] = (
            capo_internetmonitor.types.internet_events_list.deserialize_json(
                data["InternetEvents"]
            )
        )
    else:
        out["internet_events"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
