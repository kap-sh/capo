"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_summary_list
    import capo_opensearchmemory.types.pagination_token


class ListEventsOutput(TypedDict, closed=True):
    events: "capo_opensearchmemory.types.event_summary_list.EventSummaryList"
    """<p>The events, without their payloads. Call <code>GetEvent</code> for an event's payload.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Absent when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEventsOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.event_summary_list

    out["events"] = (
        capo_opensearchmemory.types.event_summary_list.serialize_aws_json_1_0(
            value["events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEventsOutput:
    out: ListEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_opensearchmemory.types.event_summary_list

        out["events"] = (
            capo_opensearchmemory.types.event_summary_list.deserialize_aws_json_1_0(
                data["events"]
            )
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
