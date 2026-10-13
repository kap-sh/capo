"""Generated from Smithy shape ``com.amazonaws.connect#ViewVersionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.view_description
    import capo_connect.types.view_id
    import capo_connect.types.view_name
    import capo_connect.types.view_type
    import capo_connect.types.view_version


class ViewVersionSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.view_id.ViewId"]
    """<p>The identifier of the view version.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view version.</p>"""
    description: NotRequired["capo_connect.types.view_description.ViewDescription"]
    """<p>The description of the view version.</p>"""
    name: NotRequired["capo_connect.types.view_name.ViewName"]
    """<p>The name of the view version.</p>"""
    type: NotRequired["capo_connect.types.view_type.ViewType"]
    """<p>The type of the view version.</p>"""
    version: "capo_connect.types.view_version.ViewVersion"
    """<p>The sequentially incremented version of the view version.</p>"""
    version_description: NotRequired[
        "capo_connect.types.view_description.ViewDescription"
    ]
    """<p>The description of the view version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewVersionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_connect.types.view_type

        out["Type"] = capo_connect.types.view_type.serialize_json(value["type"])
    out["Version"] = value.get("version", 0)
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    return out


def deserialize_json(data: dict) -> ViewVersionSummary:
    out: ViewVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_connect.types.view_type

        out["type"] = capo_connect.types.view_type.deserialize_json(data["Type"])
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    return out


def redact_sensitive(value: ViewVersionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
