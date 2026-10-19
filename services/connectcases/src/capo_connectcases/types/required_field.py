"""Generated from Smithy shape ``com.amazonaws.connectcases#RequiredField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_id


class RequiredField(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequiredField) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    return out


def deserialize_json(data: dict) -> RequiredField:
    out: RequiredField = {}  # type: ignore[typeddict-item]
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    else:
        out["field_id"] = ""
    return out
