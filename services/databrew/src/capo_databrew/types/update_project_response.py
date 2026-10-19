"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.date
    import capo_databrew.types.project_name


class UpdateProjectResponse(TypedDict, closed=True):
    last_modified_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time that the project was last modified.</p>"""
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectResponse) -> dict:
    out: dict = {}
    if "last_modified_date" in value:
        import capo_databrew.types.date

        out["LastModifiedDate"] = capo_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateProjectResponse:
    out: UpdateProjectResponse = {}  # type: ignore[typeddict-item]
    if data.get("LastModifiedDate") is not None:
        import capo_databrew.types.date

        out["last_modified_date"] = capo_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
