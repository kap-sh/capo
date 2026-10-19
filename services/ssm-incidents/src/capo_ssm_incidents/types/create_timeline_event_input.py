"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateTimelineEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.event_data
    import capo_ssm_incidents.types.event_reference_list
    import capo_ssm_incidents.types.timeline_event_type


class CreateTimelineEventInput(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the action only once with the specified details.</p>"""
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record that the action adds the incident to.</p>"""
    event_time: "datetime.datetime"
    """<p>The timestamp for when the event occurred.</p>"""
    event_type: "capo_ssm_incidents.types.timeline_event_type.TimelineEventType"
    """<p>The type of event. You can create timeline events of type <code>Custom Event</code> and <code>Note</code>.</p> <p>To make a Note-type event appear on the <i>Incident notes</i> panel in the console, specify <code>eventType</code> as <code>Note</code>and enter the Amazon Resource Name (ARN) of the incident as the value for <code>eventReference</code>.</p>"""
    event_data: "capo_ssm_incidents.types.event_data.EventData"
    """<p>A short description of the event.</p>"""
    event_references: NotRequired[
        "capo_ssm_incidents.types.event_reference_list.EventReferenceList"
    ]
    """<p>Adds one or more references to the <code>TimelineEvent</code>. A reference is an Amazon Web Services resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with a resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use the table's ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTimelineEventInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["incidentRecordArn"] = value["incident_record_arn"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["eventTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["event_time"]
    )
    out["eventType"] = value["event_type"]
    out["eventData"] = value["event_data"]
    if "event_references" in value:
        import capo_ssm_incidents.types.event_reference_list

        out["eventReferences"] = (
            capo_ssm_incidents.types.event_reference_list.serialize_json(
                value["event_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTimelineEventInput:
    out: CreateTimelineEventInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("incidentRecordArn") is not None:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        out["incident_record_arn"] = ""
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
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("eventData") is not None:
        out["event_data"] = data["eventData"]
    else:
        out["event_data"] = ""
    if data.get("eventReferences") is not None:
        import capo_ssm_incidents.types.event_reference_list

        out["event_references"] = (
            capo_ssm_incidents.types.event_reference_list.deserialize_json(
                data["eventReferences"]
            )
        )
    return out
