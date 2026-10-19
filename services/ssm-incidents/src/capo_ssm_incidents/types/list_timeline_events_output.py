"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListTimelineEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.event_summary_list
    import capo_ssm_incidents.types.next_token


class ListTimelineEventsOutput(TypedDict, closed=True):
    event_summaries: "capo_ssm_incidents.types.event_summary_list.EventSummaryList"
    """<p>Details about each event that occurred during the incident.</p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimelineEventsOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.event_summary_list

    out["eventSummaries"] = capo_ssm_incidents.types.event_summary_list.serialize_json(
        value["event_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTimelineEventsOutput:
    out: ListTimelineEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("eventSummaries") is not None:
        import capo_ssm_incidents.types.event_summary_list

        out["event_summaries"] = (
            capo_ssm_incidents.types.event_summary_list.deserialize_json(
                data["eventSummaries"]
            )
        )
    else:
        out["event_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
