"""Generated from Smithy shape ``com.amazonaws.opensearch#StartServiceSoftwareUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.long
    import capo_opensearch.types.schedule_at


class StartServiceSoftwareUpdateRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain that you want to update to the latest service software.</p>"""
    schedule_at: NotRequired["capo_opensearch.types.schedule_at.ScheduleAt"]
    """<p>When to start the service software update.</p> <ul> <li> <p> <code>NOW</code> - Immediately schedules the update to happen in the current hour if there's capacity available.</p> </li> <li> <p> <code>TIMESTAMP</code> - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for <code>DesiredStartTime</code>.</p> </li> <li> <p> <code>OFF_PEAK_WINDOW</code> - Marks the update to be picked up during an upcoming off-peak window. There's no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days.</p> </li> </ul> <p>Default: <code>NOW</code> if you don't specify a value for <code>DesiredStartTime</code>, and <code>TIMESTAMP</code> if you do.</p>"""
    desired_start_time: NotRequired["capo_opensearch.types.long.Long"]
    """<p>The Epoch timestamp when you want the service software update to start. You only need to specify this parameter if you set <code>ScheduleAt</code> to <code>TIMESTAMP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartServiceSoftwareUpdateRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "schedule_at" in value:
        import capo_opensearch.types.schedule_at

        out["ScheduleAt"] = capo_opensearch.types.schedule_at.serialize_json(
            value["schedule_at"]
        )
    if "desired_start_time" in value:
        out["DesiredStartTime"] = value["desired_start_time"]
    return out


def deserialize_json(data: dict) -> StartServiceSoftwareUpdateRequest:
    out: StartServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("ScheduleAt") is not None:
        import capo_opensearch.types.schedule_at

        out["schedule_at"] = capo_opensearch.types.schedule_at.deserialize_json(
            data["ScheduleAt"]
        )
    if data.get("DesiredStartTime") is not None:
        out["desired_start_time"] = data["DesiredStartTime"]
    return out
