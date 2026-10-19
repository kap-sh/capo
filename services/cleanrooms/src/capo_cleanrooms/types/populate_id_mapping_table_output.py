"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulateIdMappingTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.uuid


class PopulateIdMappingTableOutput(TypedDict, closed=True):
    id_mapping_job_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the mapping job that will populate the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulateIdMappingTableOutput) -> dict:
    out: dict = {}
    out["idMappingJobId"] = value["id_mapping_job_id"]
    return out


def deserialize_json(data: dict) -> PopulateIdMappingTableOutput:
    out: PopulateIdMappingTableOutput = {}  # type: ignore[typeddict-item]
    if data.get("idMappingJobId") is not None:
        out["id_mapping_job_id"] = data["idMappingJobId"]
    else:
        out["id_mapping_job_id"] = ""
    return out
