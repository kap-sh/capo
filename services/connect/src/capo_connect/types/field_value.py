"""Generated from Smithy shape ``com.amazonaws.connect#FieldValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.field_value_id
    import capo_connect.types.field_value_union


class FieldValue(TypedDict, closed=True):
    id: "capo_connect.types.field_value_id.FieldValueId"
    """<p>Unique identifier of a field.</p>"""
    value: "capo_connect.types.field_value_union.FieldValueUnion"
    """<p>Union of potential field value types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValue) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_connect.types.field_value_union

    out["Value"] = capo_connect.types.field_value_union.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> FieldValue:
    out: FieldValue = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Value") is not None:
        import capo_connect.types.field_value_union

        out["value"] = capo_connect.types.field_value_union.deserialize_json(
            data["Value"]
        )
    else:
        raise DeserializationError("FieldValue.value required")
    return out
