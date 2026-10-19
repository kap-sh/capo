"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateTimelineEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.event_data
    import capo_ssm_incidents.types.event_reference_list
    import capo_ssm_incidents.types.timeline_event_type
    import capo_ssm_incidents.types.uuid


class UpdateTimelineEventInput(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the operation only once with the specified details.</p>"""
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>"""
    event_id: "capo_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the event to update. You can use <code>ListTimelineEvents</code> to find an event's ID.</p>"""
    event_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the event occurred.</p>"""
    event_type: NotRequired[
        "capo_ssm_incidents.types.timeline_event_type.TimelineEventType"
    ]
    """<p>The type of event. You can update events of type <code>Custom Event</code> and <code>Note</code>.</p>"""
    event_data: NotRequired["capo_ssm_incidents.types.event_data.EventData"]
    """<p>A short description of the event.</p>"""
    event_references: NotRequired[
        "capo_ssm_incidents.types.event_reference_list.EventReferenceList"
    ]
    """<p>Updates all existing references in a <code>TimelineEvent</code>. A reference is an Amazon Web Services resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with that resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use its ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.</p> <important> <p>This update action overrides all existing references. If you want to keep existing references, you must specify them in the call. If you don't, this action removes any existing references and enters only new references.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTimelineEventInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    if "event_time" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        out["eventTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["event_time"]
        )
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "event_data" in value:
        out["eventData"] = value["event_data"]
    if "event_references" in value:
        import capo_ssm_incidents.types.event_reference_list

        out["eventReferences"] = (
            capo_ssm_incidents.types.event_reference_list.serialize_json(
                value["event_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTimelineEventInput:
    out: UpdateTimelineEventInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    if data.get("eventData") is not None:
        out["event_data"] = data["eventData"]
    if data.get("eventReferences") is not None:
        import capo_ssm_incidents.types.event_reference_list

        out["event_references"] = (
            capo_ssm_incidents.types.event_reference_list.deserialize_json(
                data["eventReferences"]
            )
        )
    return out
