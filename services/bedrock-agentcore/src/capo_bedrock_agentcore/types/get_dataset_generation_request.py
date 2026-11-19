"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetDatasetGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_generation_id
    import capo_bedrock_agentcore.types.dataset_id


class GetDatasetGenerationRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    generation_id: (
        "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId"
    )
    """<p>The unique identifier of the dataset generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetGenerationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDatasetGenerationRequest:
    out: GetDatasetGenerationRequest = {}  # type: ignore[typeddict-item]
    return out
