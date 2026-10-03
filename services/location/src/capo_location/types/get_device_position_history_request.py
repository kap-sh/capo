"""Generated from Smithy shape ``com.amazonaws.location#GetDevicePositionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.id
    import capo_location.types.resource_name
    import capo_location.types.timestamp
    import capo_location.types.token


class GetDevicePositionHistoryRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The tracker resource receiving the request for the device position history.</p>"""
    device_id: "capo_location.types.id.Id"
    """<p>The device whose position history you want to retrieve.</p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>"""
    start_time_inclusive: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Specify the start time for the position history in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. By default, the value will be 24 hours prior to the time that the request is made.</p> <p>Requirement:</p> <ul> <li> <p>The time specified for <code>StartTimeInclusive</code> must be before <code>EndTimeExclusive</code>.</p> </li> </ul>"""
    end_time_exclusive: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Specify the end time for the position history in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. By default, the value will be the time that the request is made.</p> <p>Requirement:</p> <ul> <li> <p>The time specified for <code>EndTimeExclusive</code> must be after the time for <code>StartTimeInclusive</code>.</p> </li> </ul>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of device positions returned in a single call.</p> <p>Default value: <code>100</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicePositionHistoryRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "start_time_inclusive" in value:
        import capo_location.types.timestamp

        out["StartTimeInclusive"] = capo_location.types.timestamp.serialize_json(
            value["start_time_inclusive"]
        )
    if "end_time_exclusive" in value:
        import capo_location.types.timestamp

        out["EndTimeExclusive"] = capo_location.types.timestamp.serialize_json(
            value["end_time_exclusive"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetDevicePositionHistoryRequest:
    out: GetDevicePositionHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("StartTimeInclusive") is not None:
        import capo_location.types.timestamp

        out["start_time_inclusive"] = capo_location.types.timestamp.deserialize_json(
            data["StartTimeInclusive"]
        )
    if data.get("EndTimeExclusive") is not None:
        import capo_location.types.timestamp

        out["end_time_exclusive"] = capo_location.types.timestamp.deserialize_json(
            data["EndTimeExclusive"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
