"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppDatasetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_dataset_id


class CreateWhatsAppDatasetOutput(TypedDict, closed=True):
    dataset_id: "capo_socialmessaging.types.whats_app_dataset_id.WhatsAppDatasetId"
    """<p>The Meta-generated dataset ID, a numeric string of 10 to 20 digits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppDatasetOutput) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppDatasetOutput:
    out: CreateWhatsAppDatasetOutput = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    return out
