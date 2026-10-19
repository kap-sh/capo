"""Generated from Smithy shape ``com.amazonaws.frauddetector#SendEventRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.event_variable_map
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.list_of_entities
    import capo_frauddetector.types.utc_timestamp_iso8601


class SendEventRequest(TypedDict, closed=True):
    event_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The event ID to upload.</p>"""
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The event type name of the event.</p>"""
    event_timestamp: (
        "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
    )
    """<p>The timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.</p>"""
    event_variables: "capo_frauddetector.types.event_variable_map.EventVariableMap"
    """<p>Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.</p>"""
    assigned_label: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The label to associate with the event. Required if specifying <code>labelTimestamp</code>.</p>"""
    label_timestamp: NotRequired[
        "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
    ]
    """<p>The timestamp associated with the label. Required if specifying <code>assignedLabel</code>.</p>"""
    entities: "capo_frauddetector.types.list_of_entities.listOfEntities"
    """<p>An array of entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    out["eventTimestamp"] = value["event_timestamp"]
    import capo_frauddetector.types.event_variable_map

    out["eventVariables"] = (
        capo_frauddetector.types.event_variable_map.serialize_aws_json_1_1(
            value["event_variables"]
        )
    )
    if "assigned_label" in value:
        out["assignedLabel"] = value["assigned_label"]
    if "label_timestamp" in value:
        out["labelTimestamp"] = value["label_timestamp"]
    import capo_frauddetector.types.list_of_entities

    out["entities"] = capo_frauddetector.types.list_of_entities.serialize_aws_json_1_1(
        value["entities"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendEventRequest:
    out: SendEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        out["event_type_name"] = ""
    if data.get("eventTimestamp") is not None:
        out["event_timestamp"] = data["eventTimestamp"]
    else:
        out["event_timestamp"] = ""
    if data.get("eventVariables") is not None:
        import capo_frauddetector.types.event_variable_map

        out["event_variables"] = (
            capo_frauddetector.types.event_variable_map.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    else:
        out["event_variables"] = {}
    if data.get("assignedLabel") is not None:
        out["assigned_label"] = data["assignedLabel"]
    if data.get("labelTimestamp") is not None:
        out["label_timestamp"] = data["labelTimestamp"]
    if data.get("entities") is not None:
        import capo_frauddetector.types.list_of_entities

        out["entities"] = (
            capo_frauddetector.types.list_of_entities.deserialize_aws_json_1_1(
                data["entities"]
            )
        )
    else:
        out["entities"] = []
    return out


def redact_sensitive(value: SendEventRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event_variables" in value:
        import capo_frauddetector.types.event_variable_map

        out["event_variables"] = (
            capo_frauddetector.types.event_variable_map.redact_sensitive(
                value["event_variables"]
            )
        )
    if "entities" in value:
        import capo_frauddetector.types.list_of_entities

        out["entities"] = capo_frauddetector.types.list_of_entities.redact_sensitive(
            value["entities"]
        )
    return out
