"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PublishSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.schema_name
    import capo_clouddirectory.types.version


class PublishSchemaRequest(TypedDict, closed=True):
    development_schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see <a>arns</a>.</p>"""
    version: "capo_clouddirectory.types.version.Version"
    """<p>The major version under which the schema will be published. Schemas have both a major and minor version associated with them.</p>"""
    minor_version: NotRequired["capo_clouddirectory.types.version.Version"]
    """<p>The minor version under which the schema will be published. This parameter is recommended. Schemas have both a major and minor version associated with them.</p>"""
    name: NotRequired["capo_clouddirectory.types.schema_name.SchemaName"]
    """<p>The new name under which the schema will be published. If this is not provided, the development schema is considered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishSchemaRequest) -> dict:
    out: dict = {}
    out["Version"] = value["version"]
    if "minor_version" in value:
        out["MinorVersion"] = value["minor_version"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> PublishSchemaRequest:
    out: PublishSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    if data.get("MinorVersion") is not None:
        out["minor_version"] = data["MinorVersion"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
