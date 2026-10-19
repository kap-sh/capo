"""Generated from Smithy shape ``com.amazonaws.databrew#CreateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.dataset_name


class CreateDatasetResponse(TypedDict, closed=True):
    name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset that you created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
