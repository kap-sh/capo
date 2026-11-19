"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_id
    import capo_bedrock_agentcore.types.dataset_version


class DatasetDetails(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    dataset_version: "capo_bedrock_agentcore.types.dataset_version.DatasetVersion"
    """<p>The version of the dataset that the batch evaluation ran. If the request didn't specify a version, this is the latest published version when the batch evaluation started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetDetails) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetVersion"] = value["dataset_version"]
    return out


def deserialize_json(data: dict) -> DatasetDetails:
    out: DatasetDetails = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    else:
        out["dataset_version"] = ""
    return out
