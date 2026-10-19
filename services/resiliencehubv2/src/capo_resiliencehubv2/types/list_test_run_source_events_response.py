"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunSourceEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_source_event_list


class ListTestRunSourceEventsResponse(TypedDict, closed=True):
    test_run_source_events: (
        "capo_resiliencehubv2.types.test_run_source_event_list.TestRunSourceEventList"
    )
    """<p>The list of source events, in chronological order.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunSourceEventsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run_source_event_list

    out["testRunSourceEvents"] = (
        capo_resiliencehubv2.types.test_run_source_event_list.serialize_json(
            value["test_run_source_events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestRunSourceEventsResponse:
    out: ListTestRunSourceEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("testRunSourceEvents") is not None:
        import capo_resiliencehubv2.types.test_run_source_event_list

        out["test_run_source_events"] = (
            capo_resiliencehubv2.types.test_run_source_event_list.deserialize_json(
                data["testRunSourceEvents"]
            )
        )
    else:
        out["test_run_source_events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
