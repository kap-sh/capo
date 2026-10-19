"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.dataset_name


class UpdateDatasetResponse(TypedDict, closed=True):
    name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateDatasetResponse:
    out: UpdateDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
