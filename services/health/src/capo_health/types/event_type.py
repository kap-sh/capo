"""Generated from Smithy shape ``com.amazonaws.health#EventType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_type_actionability
    import capo_health.types.event_type_category
    import capo_health.types.event_type_code
    import capo_health.types.event_type_persona_list
    import capo_health.types.service


class EventType(TypedDict, closed=True):
    service: NotRequired["capo_health.types.service.service"]
    """<p>The Amazon Web Services service that is affected by the event. For example, <code>EC2</code>, <code>RDS</code>.</p>"""
    code: NotRequired["capo_health.types.event_type_code.eventTypeCode"]
    """<p>The unique identifier for the event type. The format is <code>AWS_<i>SERVICE</i>_<i>DESCRIPTION</i> </code>; for example, <code>AWS_EC2_SYSTEM_MAINTENANCE_EVENT</code>.</p>"""
    category: NotRequired["capo_health.types.event_type_category.eventTypeCategory"]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    actionability: NotRequired[
        "capo_health.types.event_type_actionability.EventTypeActionability"
    ]
    """<p>The actionability classification of the event. Possible values are <code>ACTION_REQUIRED</code>, <code>ACTION_MAY_BE_REQUIRED</code> and <code>INFORMATIONAL</code>. Events with <code>ACTION_REQUIRED</code> actionability require customer action to resolve or mitigate the event. Events with <code>ACTION_MAY_BE_REQUIRED</code> actionability indicates that the current status is unknown or conditional and inspection is needed to determine if action is required. Events with <code>INFORMATIONAL</code> actionability are provided for awareness and do not require immediate action.</p>"""
    personas: NotRequired[
        "capo_health.types.event_type_persona_list.EventTypePersonaList"
    ]
    """<p>A list of persona classifications that indicate the target audience for the event. Possible values are <code>OPERATIONS</code>, <code>SECURITY</code>, and <code>BILLING</code>. Events can be associated with multiple personas to indicate relevance to different teams or roles within an organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventType) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "code" in value:
        out["code"] = value["code"]
    if "category" in value:
        import capo_health.types.event_type_category

        out["category"] = capo_health.types.event_type_category.serialize_aws_json_1_1(
            value["category"]
        )
    if "actionability" in value:
        import capo_health.types.event_type_actionability

        out["actionability"] = (
            capo_health.types.event_type_actionability.serialize_aws_json_1_1(
                value["actionability"]
            )
        )
    if "personas" in value:
        import capo_health.types.event_type_persona_list

        out["personas"] = (
            capo_health.types.event_type_persona_list.serialize_aws_json_1_1(
                value["personas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventType:
    out: EventType = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("category") is not None:
        import capo_health.types.event_type_category

        out["category"] = (
            capo_health.types.event_type_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    if data.get("actionability") is not None:
        import capo_health.types.event_type_actionability

        out["actionability"] = (
            capo_health.types.event_type_actionability.deserialize_aws_json_1_1(
                data["actionability"]
            )
        )
    if data.get("personas") is not None:
        import capo_health.types.event_type_persona_list

        out["personas"] = (
            capo_health.types.event_type_persona_list.deserialize_aws_json_1_1(
                data["personas"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventType) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "code" in value:
        out["code"] = value["code"]
    if "category" in value:
        import capo_health.types.event_type_category

        out["category"] = capo_health.types.event_type_category.serialize_cbor(
            value["category"]
        )
    if "actionability" in value:
        import capo_health.types.event_type_actionability

        out["actionability"] = (
            capo_health.types.event_type_actionability.serialize_cbor(
                value["actionability"]
            )
        )
    if "personas" in value:
        import capo_health.types.event_type_persona_list

        out["personas"] = capo_health.types.event_type_persona_list.serialize_cbor(
            value["personas"]
        )
    return out


def deserialize_cbor(data: dict) -> EventType:
    out: EventType = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("category") is not None:
        import capo_health.types.event_type_category

        out["category"] = capo_health.types.event_type_category.deserialize_cbor(
            data["category"]
        )
    if data.get("actionability") is not None:
        import capo_health.types.event_type_actionability

        out["actionability"] = (
            capo_health.types.event_type_actionability.deserialize_cbor(
                data["actionability"]
            )
        )
    if data.get("personas") is not None:
        import capo_health.types.event_type_persona_list

        out["personas"] = capo_health.types.event_type_persona_list.deserialize_cbor(
            data["personas"]
        )
    return out
