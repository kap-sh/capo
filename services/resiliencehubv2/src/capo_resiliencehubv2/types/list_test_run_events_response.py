"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_event_list


class ListTestRunEventsResponse(TypedDict, closed=True):
    events: "capo_resiliencehubv2.types.test_run_event_list.TestRunEventList"
    """<p>The list of test run events.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunEventsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run_event_list

    out["events"] = capo_resiliencehubv2.types.test_run_event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestRunEventsResponse:
    out: ListTestRunEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_resiliencehubv2.types.test_run_event_list

        out["events"] = capo_resiliencehubv2.types.test_run_event_list.deserialize_json(
            data["events"]
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
