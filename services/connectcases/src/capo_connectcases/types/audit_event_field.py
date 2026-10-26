"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.audit_event_field_id
    import capo_connectcases.types.audit_event_field_value_union


class AuditEventField(TypedDict, closed=True):
    event_field_id: "capo_connectcases.types.audit_event_field_id.AuditEventFieldId"
    """<p>Unique identifier of field in an Audit History entry.</p>"""
    old_value: NotRequired[
        "capo_connectcases.types.audit_event_field_value_union.AuditEventFieldValueUnion"
    ]
    """<p>Union of potential field value types.</p>"""
    new_value: "capo_connectcases.types.audit_event_field_value_union.AuditEventFieldValueUnion"
    """<p>Union of potential field value types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventField) -> dict:
    out: dict = {}
    out["eventFieldId"] = value["event_field_id"]
    if "old_value" in value:
        import capo_connectcases.types.audit_event_field_value_union

        out["oldValue"] = (
            capo_connectcases.types.audit_event_field_value_union.serialize_json(
                value["old_value"]
            )
        )
    import capo_connectcases.types.audit_event_field_value_union

    out["newValue"] = (
        capo_connectcases.types.audit_event_field_value_union.serialize_json(
            value["new_value"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuditEventField:
    out: AuditEventField = {}  # type: ignore[typeddict-item]
    if data.get("eventFieldId") is not None:
        out["event_field_id"] = data["eventFieldId"]
    else:
        out["event_field_id"] = ""
    if data.get("oldValue") is not None:
        import capo_connectcases.types.audit_event_field_value_union

        out["old_value"] = (
            capo_connectcases.types.audit_event_field_value_union.deserialize_json(
                data["oldValue"]
            )
        )
    if data.get("newValue") is not None:
        import capo_connectcases.types.audit_event_field_value_union

        out["new_value"] = (
            capo_connectcases.types.audit_event_field_value_union.deserialize_json(
                data["newValue"]
            )
        )
    else:
        out["new_value"] = {"$unknown": {"name": ""}}
    return out
