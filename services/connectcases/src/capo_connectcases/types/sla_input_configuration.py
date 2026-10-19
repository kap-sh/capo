"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaInputConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_id
    import capo_connectcases.types.sla_field_value_union_list
    import capo_connectcases.types.sla_name
    import capo_connectcases.types.sla_type
    import capo_connectcases.types.target_sla_minutes


class SlaInputConfiguration(TypedDict, closed=True):
    name: "capo_connectcases.types.sla_name.SlaName"
    """<p>Name of an SLA.</p>"""
    type: "capo_connectcases.types.sla_type.SlaType"
    """<p>Type of SLA.</p>"""
    field_id: NotRequired["capo_connectcases.types.field_id.FieldId"]
    """<p>Unique identifier of a field.</p>"""
    target_field_values: NotRequired[
        "capo_connectcases.types.sla_field_value_union_list.SlaFieldValueUnionList"
    ]
    """<p>Represents a list of target field values for the fieldId specified in SlaInputConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.</p>"""
    target_sla_minutes: "capo_connectcases.types.target_sla_minutes.TargetSlaMinutes"
    """<p>Target duration in minutes within which an SLA should be completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaInputConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "field_id" in value:
        out["fieldId"] = value["field_id"]
    if "target_field_values" in value:
        import capo_connectcases.types.sla_field_value_union_list

        out["targetFieldValues"] = (
            capo_connectcases.types.sla_field_value_union_list.serialize_json(
                value["target_field_values"]
            )
        )
    out["targetSlaMinutes"] = value["target_sla_minutes"]
    return out


def deserialize_json(data: dict) -> SlaInputConfiguration:
    out: SlaInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    if data.get("targetFieldValues") is not None:
        import capo_connectcases.types.sla_field_value_union_list

        out["target_field_values"] = (
            capo_connectcases.types.sla_field_value_union_list.deserialize_json(
                data["targetFieldValues"]
            )
        )
    if data.get("targetSlaMinutes") is not None:
        out["target_sla_minutes"] = data["targetSlaMinutes"]
    else:
        out["target_sla_minutes"] = 0
    return out


def redact_sensitive(value: SlaInputConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
