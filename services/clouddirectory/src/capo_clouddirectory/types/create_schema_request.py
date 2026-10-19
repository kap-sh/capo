"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.schema_name


class CreateSchemaRequest(TypedDict, closed=True):
    name: "capo_clouddirectory.types.schema_name.SchemaName"
    """<p>The name that is associated with the schema. This is unique to each account and in each region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateSchemaRequest:
    out: CreateSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
