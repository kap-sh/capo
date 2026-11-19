"""Generated from Smithy shape ``com.amazonaws.health#EventTypeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_type_actionability_list
    import capo_health.types.event_type_category_list
    import capo_health.types.event_type_code_list
    import capo_health.types.event_type_persona_list
    import capo_health.types.service_list


class EventTypeFilter(TypedDict, closed=True):
    event_type_codes: NotRequired[
        "capo_health.types.event_type_code_list.EventTypeCodeList"
    ]
    """<p>A list of event type codes.</p>"""
    services: NotRequired["capo_health.types.service_list.serviceList"]
    """<p>The Amazon Web Services services associated with the event. For example, <code>EC2</code>, <code>RDS</code>.</p>"""
    event_type_categories: NotRequired[
        "capo_health.types.event_type_category_list.EventTypeCategoryList"
    ]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    actionabilities: NotRequired[
        "capo_health.types.event_type_actionability_list.EventTypeActionabilityList"
    ]
    """<p>A list of actionability values to filter event types. Possible values are <code>ACTION_REQUIRED</code>, <code>ACTION_MAY_BE_REQUIRED</code> and <code>INFORMATIONAL</code>.</p>"""
    personas: NotRequired[
        "capo_health.types.event_type_persona_list.EventTypePersonaList"
    ]
    """<p>A list of persona classifications to filter event types. Possible values are <code>OPERATIONS</code>, <code>SECURITY</code>, and <code>BILLING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeFilter) -> dict:
    out: dict = {}
    if "event_type_codes" in value:
        import capo_health.types.event_type_code_list

        out["eventTypeCodes"] = (
            capo_health.types.event_type_code_list.serialize_aws_json_1_1(
                value["event_type_codes"]
            )
        )
    if "services" in value:
        import capo_health.types.service_list

        out["services"] = capo_health.types.service_list.serialize_aws_json_1_1(
            value["services"]
        )
    if "event_type_categories" in value:
        import capo_health.types.event_type_category_list

        out["eventTypeCategories"] = (
            capo_health.types.event_type_category_list.serialize_aws_json_1_1(
                value["event_type_categories"]
            )
        )
    if "actionabilities" in value:
        import capo_health.types.event_type_actionability_list

        out["actionabilities"] = (
            capo_health.types.event_type_actionability_list.serialize_aws_json_1_1(
                value["actionabilities"]
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


def deserialize_aws_json_1_1(data: dict) -> EventTypeFilter:
    out: EventTypeFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventTypeCodes") is not None:
        import capo_health.types.event_type_code_list

        out["event_type_codes"] = (
            capo_health.types.event_type_code_list.deserialize_aws_json_1_1(
                data["eventTypeCodes"]
            )
        )
    if data.get("services") is not None:
        import capo_health.types.service_list

        out["services"] = capo_health.types.service_list.deserialize_aws_json_1_1(
            data["services"]
        )
    if data.get("eventTypeCategories") is not None:
        import capo_health.types.event_type_category_list

        out["event_type_categories"] = (
            capo_health.types.event_type_category_list.deserialize_aws_json_1_1(
                data["eventTypeCategories"]
            )
        )
    if data.get("actionabilities") is not None:
        import capo_health.types.event_type_actionability_list

        out["actionabilities"] = (
            capo_health.types.event_type_actionability_list.deserialize_aws_json_1_1(
                data["actionabilities"]
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
def serialize_cbor(value: EventTypeFilter) -> dict:
    out: dict = {}
    if "event_type_codes" in value:
        import capo_health.types.event_type_code_list

        out["eventTypeCodes"] = capo_health.types.event_type_code_list.serialize_cbor(
            value["event_type_codes"]
        )
    if "services" in value:
        import capo_health.types.service_list

        out["services"] = capo_health.types.service_list.serialize_cbor(
            value["services"]
        )
    if "event_type_categories" in value:
        import capo_health.types.event_type_category_list

        out["eventTypeCategories"] = (
            capo_health.types.event_type_category_list.serialize_cbor(
                value["event_type_categories"]
            )
        )
    if "actionabilities" in value:
        import capo_health.types.event_type_actionability_list

        out["actionabilities"] = (
            capo_health.types.event_type_actionability_list.serialize_cbor(
                value["actionabilities"]
            )
        )
    if "personas" in value:
        import capo_health.types.event_type_persona_list

        out["personas"] = capo_health.types.event_type_persona_list.serialize_cbor(
            value["personas"]
        )
    return out


def deserialize_cbor(data: dict) -> EventTypeFilter:
    out: EventTypeFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventTypeCodes") is not None:
        import capo_health.types.event_type_code_list

        out["event_type_codes"] = (
            capo_health.types.event_type_code_list.deserialize_cbor(
                data["eventTypeCodes"]
            )
        )
    if data.get("services") is not None:
        import capo_health.types.service_list

        out["services"] = capo_health.types.service_list.deserialize_cbor(
            data["services"]
        )
    if data.get("eventTypeCategories") is not None:
        import capo_health.types.event_type_category_list

        out["event_type_categories"] = (
            capo_health.types.event_type_category_list.deserialize_cbor(
                data["eventTypeCategories"]
            )
        )
    if data.get("actionabilities") is not None:
        import capo_health.types.event_type_actionability_list

        out["actionabilities"] = (
            capo_health.types.event_type_actionability_list.deserialize_cbor(
                data["actionabilities"]
            )
        )
    if data.get("personas") is not None:
        import capo_health.types.event_type_persona_list

        out["personas"] = capo_health.types.event_type_persona_list.deserialize_cbor(
            data["personas"]
        )
    return out
