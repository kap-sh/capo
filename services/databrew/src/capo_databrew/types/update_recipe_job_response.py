"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRecipeJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_name


class UpdateRecipeJobResponse(TypedDict, closed=True):
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecipeJobResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRecipeJobResponse:
    out: UpdateRecipeJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
