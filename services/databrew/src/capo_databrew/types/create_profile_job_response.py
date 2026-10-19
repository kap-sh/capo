"""Generated from Smithy shape ``com.amazonaws.databrew#CreateProfileJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_name


class CreateProfileJobResponse(TypedDict, closed=True):
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileJobResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateProfileJobResponse:
    out: CreateProfileJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
