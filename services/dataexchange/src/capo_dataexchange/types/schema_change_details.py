"""Generated from Smithy shape ``com.amazonaws.dataexchange#SchemaChangeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.schema_change_type


class SchemaChangeDetails(TypedDict, closed=True):
    name: "capo_dataexchange.types.__string.__string"
    """<p>Name of the changing field. This value can be up to 255 characters long.</p>"""
    type: "capo_dataexchange.types.schema_change_type.SchemaChangeType"
    """<p>Is the field being added, removed, or modified?</p>"""
    description: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>Description of what's changing about this field. This value can be up to 512 characters long.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaChangeDetails) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SchemaChangeDetails:
    out: SchemaChangeDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
