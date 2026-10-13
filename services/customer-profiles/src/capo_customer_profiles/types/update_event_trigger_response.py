"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateEventTriggerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_trigger_conditions
    import capo_customer_profiles.types.event_trigger_limits
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class UpdateEventTriggerResponse(TypedDict, closed=True):
    event_trigger_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the event trigger.</p>"""
    object_type_name: NotRequired["capo_customer_profiles.types.type_name.typeName"]
    """<p>The unique name of the object type.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the event trigger.</p>"""
    event_trigger_conditions: NotRequired[
        "capo_customer_profiles.types.event_trigger_conditions.EventTriggerConditions"
    ]
    """<p>A list of conditions that determine when an event should trigger the destination.</p>"""
    segment_filter: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The destination is triggered only for profiles that meet the criteria of a segment definition.</p>"""
    event_trigger_limits: NotRequired[
        "capo_customer_profiles.types.event_trigger_limits.EventTriggerLimits"
    ]
    """<p>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the event trigger was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the event trigger was most recently updated.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>An array of key-value pairs to apply to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventTriggerResponse) -> dict:
    out: dict = {}
    if "event_trigger_name" in value:
        out["EventTriggerName"] = value["event_trigger_name"]
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_trigger_conditions" in value:
        import capo_customer_profiles.types.event_trigger_conditions

        out["EventTriggerConditions"] = (
            capo_customer_profiles.types.event_trigger_conditions.serialize_json(
                value["event_trigger_conditions"]
            )
        )
    if "segment_filter" in value:
        out["SegmentFilter"] = value["segment_filter"]
    if "event_trigger_limits" in value:
        import capo_customer_profiles.types.event_trigger_limits

        out["EventTriggerLimits"] = (
            capo_customer_profiles.types.event_trigger_limits.serialize_json(
                value["event_trigger_limits"]
            )
        )
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateEventTriggerResponse:
    out: UpdateEventTriggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventTriggerName") is not None:
        out["event_trigger_name"] = data["EventTriggerName"]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EventTriggerConditions") is not None:
        import capo_customer_profiles.types.event_trigger_conditions

        out["event_trigger_conditions"] = (
            capo_customer_profiles.types.event_trigger_conditions.deserialize_json(
                data["EventTriggerConditions"]
            )
        )
    if data.get("SegmentFilter") is not None:
        out["segment_filter"] = data["SegmentFilter"]
    if data.get("EventTriggerLimits") is not None:
        import capo_customer_profiles.types.event_trigger_limits

        out["event_trigger_limits"] = (
            capo_customer_profiles.types.event_trigger_limits.deserialize_json(
                data["EventTriggerLimits"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: UpdateEventTriggerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "event_trigger_conditions" in value:
        out["event_trigger_conditions"] = "*** Sensitive Data Redacted ***"
    return out
