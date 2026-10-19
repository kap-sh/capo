"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteTimelineEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.uuid


class DeleteTimelineEventInput(TypedDict, closed=True):
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>"""
    event_id: "capo_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the event to update. You can use <code>ListTimelineEvents</code> to find an event's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTimelineEventInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> DeleteTimelineEventInput:
    out: DeleteTimelineEventInput = {}  # type: ignore[typeddict-item]
    if data.get("incidentRecordArn") is not None:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        out["incident_record_arn"] = ""
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    return out
