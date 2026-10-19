"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_id


class FieldItem(TypedDict, closed=True):
    id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> FieldItem:
    out: FieldItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
