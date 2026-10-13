"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.field_id
    import capo_connectcases.types.sla_completion_time
    import capo_connectcases.types.sla_field_value_union_list
    import capo_connectcases.types.sla_name
    import capo_connectcases.types.sla_status
    import capo_connectcases.types.sla_target_time
    import capo_connectcases.types.sla_type


class SlaConfiguration(TypedDict, closed=True):
    name: "capo_connectcases.types.sla_name.SlaName"
    """<p>Name of an SLA.</p>"""
    type: "capo_connectcases.types.sla_type.SlaType"
    """<p>Type of SLA.</p>"""
    status: "capo_connectcases.types.sla_status.SlaStatus"
    """<p>Status of an SLA.</p>"""
    field_id: NotRequired["capo_connectcases.types.field_id.FieldId"]
    """<p>Unique identifier of a field.</p>"""
    target_field_values: NotRequired[
        "capo_connectcases.types.sla_field_value_union_list.SlaFieldValueUnionList"
    ]
    """<p>Represents a list of target field values for the fieldId specified in SlaConfiguration.</p>"""
    target_time: "capo_connectcases.types.sla_target_time.SlaTargetTime"
    """<p>Target time by which an SLA should be completed.</p>"""
    completion_time: NotRequired[
        "capo_connectcases.types.sla_completion_time.SlaCompletionTime"
    ]
    """<p>Time at which an SLA was completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    if "field_id" in value:
        out["fieldId"] = value["field_id"]
    if "target_field_values" in value:
        import capo_connectcases.types.sla_field_value_union_list

        out["targetFieldValues"] = (
            capo_connectcases.types.sla_field_value_union_list.serialize_json(
                value["target_field_values"]
            )
        )
    import capo_connectcases.types.sla_target_time

    out["targetTime"] = capo_connectcases.types.sla_target_time.serialize_json(
        value["target_time"]
    )
    if "completion_time" in value:
        import capo_connectcases.types.sla_completion_time

        out["completionTime"] = (
            capo_connectcases.types.sla_completion_time.serialize_json(
                value["completion_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlaConfiguration:
    out: SlaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SlaConfiguration.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SlaConfiguration.type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("SlaConfiguration.status required")
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    if data.get("targetFieldValues") is not None:
        import capo_connectcases.types.sla_field_value_union_list

        out["target_field_values"] = (
            capo_connectcases.types.sla_field_value_union_list.deserialize_json(
                data["targetFieldValues"]
            )
        )
    if data.get("targetTime") is not None:
        import capo_connectcases.types.sla_target_time

        out["target_time"] = capo_connectcases.types.sla_target_time.deserialize_json(
            data["targetTime"]
        )
    else:
        raise DeserializationError("SlaConfiguration.target_time required")
    if data.get("completionTime") is not None:
        import capo_connectcases.types.sla_completion_time

        out["completion_time"] = (
            capo_connectcases.types.sla_completion_time.deserialize_json(
                data["completionTime"]
            )
        )
    return out


def redact_sensitive(value: SlaConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
