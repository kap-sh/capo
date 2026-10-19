"""Generated from Smithy shape ``com.amazonaws.swf#History``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.history_event_list
    import capo_swf.types.page_token


class History(TypedDict, closed=True):
    events: "capo_swf.types.history_event_list.HistoryEventList"
    """<p>The list of history events.</p>"""
    next_page_token: NotRequired["capo_swf.types.page_token.PageToken"]
    """<p>If a <code>NextPageToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>nextPageToken</code>. Keep all other arguments unchanged.</p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: History) -> dict:
    out: dict = {}
    import capo_swf.types.history_event_list

    out["events"] = capo_swf.types.history_event_list.serialize_aws_json_1_0(
        value["events"]
    )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> History:
    out: History = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_swf.types.history_event_list

        out["events"] = capo_swf.types.history_event_list.deserialize_aws_json_1_0(
            data["events"]
        )
    else:
        out["events"] = []
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    return out
