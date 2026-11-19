"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_id
    import capo_bedrock_agentcore.types.dataset_version


class DatasetSource(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    dataset_version: NotRequired[
        "capo_bedrock_agentcore.types.dataset_version.DatasetVersion"
    ]
    """<p>The number of a published version of the dataset. You can't run the <code>DRAFT</code> version. If you don't specify a version, the batch evaluation uses the latest published version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSource) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    if "dataset_version" in value:
        out["datasetVersion"] = value["dataset_version"]
    return out


def deserialize_json(data: dict) -> DatasetSource:
    out: DatasetSource = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    return out
