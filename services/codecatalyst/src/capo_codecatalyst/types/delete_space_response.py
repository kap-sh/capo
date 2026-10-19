"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string


class DeleteSpaceResponse(TypedDict, closed=True):
    name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name of the space displayed to users of the space in Amazon CodeCatalyst.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSpaceResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> DeleteSpaceResponse:
    out: DeleteSpaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out
