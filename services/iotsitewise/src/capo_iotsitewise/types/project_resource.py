"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ProjectResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class ProjectResource(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectResource) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ProjectResource:
    out: ProjectResource = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
