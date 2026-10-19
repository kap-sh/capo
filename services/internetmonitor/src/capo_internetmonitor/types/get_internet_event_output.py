"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetInternetEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.arn
    import capo_internetmonitor.types.client_location
    import capo_internetmonitor.types.internet_event_id
    import capo_internetmonitor.types.internet_event_status
    import capo_internetmonitor.types.internet_event_type


class GetInternetEventOutput(TypedDict, closed=True):
    event_id: "capo_internetmonitor.types.internet_event_id.InternetEventId"
    """<p>The internally-generated identifier of an internet event.</p>"""
    event_arn: "capo_internetmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the internet event.</p>"""
    started_at: "datetime.datetime"
    """<p>The time when the internet event started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time when the internet event ended. If the event hasn't ended yet, this value is empty.</p>"""
    client_location: "capo_internetmonitor.types.client_location.ClientLocation"
    """<p>The impacted location, such as a city, where clients access Amazon Web Services application resources.</p>"""
    event_type: "capo_internetmonitor.types.internet_event_type.InternetEventType"
    """<p>The type of network impairment.</p>"""
    event_status: "capo_internetmonitor.types.internet_event_status.InternetEventStatus"
    """<p>The status of the internet event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInternetEventOutput) -> dict:
    out: dict = {}
    out["EventId"] = value["event_id"]
    out["EventArn"] = value["event_arn"]
    import capo_internetmonitor._protocol.serialize

    out["StartedAt"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_internetmonitor._protocol.serialize

        out["EndedAt"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    import capo_internetmonitor.types.client_location

    out["ClientLocation"] = capo_internetmonitor.types.client_location.serialize_json(
        value["client_location"]
    )
    out["EventType"] = value["event_type"]
    out["EventStatus"] = value["event_status"]
    return out


def deserialize_json(data: dict) -> GetInternetEventOutput:
    out: GetInternetEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    else:
        out["event_id"] = ""
    if data.get("EventArn") is not None:
        out["event_arn"] = data["EventArn"]
    else:
        out["event_arn"] = ""
    if data.get("StartedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["StartedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["EndedAt"].replace("Z", "+00:00")
        )
    if data.get("ClientLocation") is not None:
        import capo_internetmonitor.types.client_location

        out["client_location"] = (
            capo_internetmonitor.types.client_location.deserialize_json(
                data["ClientLocation"]
            )
        )
    else:
        raise DeserializationError("GetInternetEventOutput.client_location required")
    if data.get("EventType") is not None:
        out["event_type"] = data["EventType"]
    else:
        out["event_type"] = ""
    if data.get("EventStatus") is not None:
        out["event_status"] = data["EventStatus"]
    else:
        out["event_status"] = ""
    return out
