"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.project_description
    import capo_codecatalyst.types.project_display_name


class CreateProjectRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    display_name: "capo_codecatalyst.types.project_display_name.ProjectDisplayName"
    """<p>The friendly name of the project that will be displayed to users.</p>"""
    description: NotRequired[
        "capo_codecatalyst.types.project_description.ProjectDescription"
    ]
    """<p>The description of the project. This description will be displayed to all users of the project. We recommend providing a brief description of the project and its intended purpose.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
