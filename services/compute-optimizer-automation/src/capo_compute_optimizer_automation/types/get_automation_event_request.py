"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#GetAutomationEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.event_id


class GetAutomationEventRequest(TypedDict, closed=True):
    event_id: "capo_compute_optimizer_automation.types.event_id.EventId"
    """<p> The ID of the automation event to retrieve. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutomationEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutomationEventRequest:
    out: GetAutomationEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    return out
