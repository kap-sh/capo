"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListEventLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.timestamp


class ListEventLogsRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    start_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time when you want to start retrieving events, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    end_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The time after which you do not want any events retrieved, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    event_name: NotRequired["str"]
    """<p>The name of the event.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventLogsRequest) -> dict:
    out: dict = {}
    import capo_codecatalyst._protocol.serialize

    out["startTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_codecatalyst._protocol.serialize

    out["endTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    if "event_name" in value:
        out["eventName"] = value["event_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListEventLogsRequest:
    out: ListEventLogsRequest = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("ListEventLogsRequest.start_time required")
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("ListEventLogsRequest.end_time required")
    if data.get("eventName") is not None:
        out["event_name"] = data["eventName"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
