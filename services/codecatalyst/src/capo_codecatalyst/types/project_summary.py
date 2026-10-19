"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ProjectSummary``."""

from typing_extensions import NotRequired, TypedDict


class ProjectSummary(TypedDict, closed=True):
    name: "str"
    """<p>The name of the project in the space.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name displayed to users of the project in Amazon CodeCatalyst.</p>"""
    description: NotRequired["str"]
    """<p>The description of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ProjectSummary:
    out: ProjectSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
