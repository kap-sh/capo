"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourcePathComponent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.resource_name_type


class ResourcePathComponent(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the resource path.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the resource path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePathComponent) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ResourcePathComponent:
    out: ResourcePathComponent = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: ResourcePathComponent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
