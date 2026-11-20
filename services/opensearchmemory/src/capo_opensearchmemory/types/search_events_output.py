"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SearchEventsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_search_summary_list
    import capo_opensearchmemory.types.pagination_token


class SearchEventsOutput(TypedDict, closed=True):
    events: (
        "capo_opensearchmemory.types.event_search_summary_list.EventSearchSummaryList"
    )
    """<p>The matching event chunks, in the order <code>sort</code> requests, or most relevant first when it has none. Empty when nothing matches. Each result is the matching chunk of an event. Call <code>GetEvent</code> for the whole event.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Absent when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchEventsOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.event_search_summary_list

    out["events"] = (
        capo_opensearchmemory.types.event_search_summary_list.serialize_aws_json_1_0(
            value["events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchEventsOutput:
    out: SearchEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_opensearchmemory.types.event_search_summary_list

        out["events"] = (
            capo_opensearchmemory.types.event_search_summary_list.deserialize_aws_json_1_0(
                data["events"]
            )
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchEventsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        import capo_opensearchmemory.types.event_search_summary_list

        out["events"] = (
            capo_opensearchmemory.types.event_search_summary_list.redact_sensitive(
                value["events"]
            )
        )
    return out
