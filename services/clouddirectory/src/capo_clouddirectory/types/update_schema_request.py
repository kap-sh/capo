"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.schema_name


class UpdateSchemaRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.</p>"""
    name: "capo_clouddirectory.types.schema_name.SchemaName"
    """<p>The name of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateSchemaRequest:
    out: UpdateSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
