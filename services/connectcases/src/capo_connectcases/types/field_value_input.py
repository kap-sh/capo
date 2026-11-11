"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_identifier_union
    import capo_connectcases.types.field_value_union


class FieldValueInput(TypedDict, closed=True):
    field_identifier: (
        "capo_connectcases.types.field_identifier_union.FieldIdentifierUnion"
    )
    """<p>The field to update, identified by field ID or field name.</p>"""
    value: "capo_connectcases.types.field_value_union.FieldValueUnion"
    """<p>The value to set for the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueInput) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_identifier_union

    out["fieldIdentifier"] = (
        capo_connectcases.types.field_identifier_union.serialize_json(
            value["field_identifier"]
        )
    )
    import capo_connectcases.types.field_value_union

    out["value"] = capo_connectcases.types.field_value_union.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> FieldValueInput:
    out: FieldValueInput = {}  # type: ignore[typeddict-item]
    if data.get("fieldIdentifier") is not None:
        import capo_connectcases.types.field_identifier_union

        out["field_identifier"] = (
            capo_connectcases.types.field_identifier_union.deserialize_json(
                data["fieldIdentifier"]
            )
        )
    else:
        out["field_identifier"] = {"$unknown": {"name": ""}}
    if data.get("value") is not None:
        import capo_connectcases.types.field_value_union

        out["value"] = capo_connectcases.types.field_value_union.deserialize_json(
            data["value"]
        )
    else:
        out["value"] = {"$unknown": {"name": ""}}
    return out
