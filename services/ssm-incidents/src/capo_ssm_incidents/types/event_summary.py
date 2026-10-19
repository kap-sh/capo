"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.event_reference_list
    import capo_ssm_incidents.types.timeline_event_type
    import capo_ssm_incidents.types.uuid


class EventSummary(TypedDict, closed=True):
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that the event happened during.</p>"""
    event_id: "capo_ssm_incidents.types.uuid.UUID"
    """<p>The timeline event ID.</p>"""
    event_time: "datetime.datetime"
    """<p>The timestamp for when the event occurred.</p>"""
    event_updated_time: "datetime.datetime"
    """<p>The timestamp for when the timeline event was last updated.</p>"""
    event_type: "capo_ssm_incidents.types.timeline_event_type.TimelineEventType"
    """<p>The type of event. The timeline event must be <code>Custom Event</code> or <code>Note</code>.</p>"""
    event_references: NotRequired[
        "capo_ssm_incidents.types.event_reference_list.EventReferenceList"
    ]
    """<p>A list of references in a <code>TimelineEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSummary) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["eventTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["event_time"]
    )
    import capo_ssm_incidents.types._prelude.timestamp

    out["eventUpdatedTime"] = (
        capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["event_updated_time"]
        )
    )
    out["eventType"] = value["event_type"]
    if "event_references" in value:
        import capo_ssm_incidents.types.event_reference_list

        out["eventReferences"] = (
            capo_ssm_incidents.types.event_reference_list.serialize_json(
                value["event_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventSummary:
    out: EventSummary = {}  # type: ignore[typeddict-item]
    if data.get("incidentRecordArn") is not None:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        out["incident_record_arn"] = ""
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["event_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["eventTime"]
            )
        )
    else:
        import datetime

        out["event_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("eventUpdatedTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["event_updated_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["eventUpdatedTime"]
            )
        )
    else:
        import datetime

        out["event_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("eventReferences") is not None:
        import capo_ssm_incidents.types.event_reference_list

        out["event_references"] = (
            capo_ssm_incidents.types.event_reference_list.deserialize_json(
                data["eventReferences"]
            )
        )
    return out
