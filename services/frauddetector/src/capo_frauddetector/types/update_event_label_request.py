"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateEventLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.utc_timestamp_iso8601


class UpdateEventLabelRequest(TypedDict, closed=True):
    event_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The ID of the event associated with the label to update.</p>"""
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The event type of the event associated with the label to update.</p>"""
    assigned_label: "capo_frauddetector.types.identifier.identifier"
    """<p>The new label to assign to the event.</p>"""
    label_timestamp: (
        "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
    )
    """<p>The timestamp associated with the label. The timestamp must be specified using ISO 8601 standard in UTC. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEventLabelRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    out["assignedLabel"] = value["assigned_label"]
    out["labelTimestamp"] = value["label_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEventLabelRequest:
    out: UpdateEventLabelRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        out["event_type_name"] = ""
    if data.get("assignedLabel") is not None:
        out["assigned_label"] = data["assignedLabel"]
    else:
        out["assigned_label"] = ""
    if data.get("labelTimestamp") is not None:
        out["label_timestamp"] = data["labelTimestamp"]
    else:
        out["label_timestamp"] = ""
    return out
