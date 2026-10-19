"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.project_name


class DeleteProjectResponse(TypedDict, closed=True):
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project that you deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteProjectResponse:
    out: DeleteProjectResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
