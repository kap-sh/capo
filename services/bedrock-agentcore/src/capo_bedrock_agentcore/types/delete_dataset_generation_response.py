"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteDatasetGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_generation_id
    import capo_bedrock_agentcore.types.dataset_generation_status


class DeleteDatasetGenerationResponse(TypedDict, closed=True):
    generation_id: (
        "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId"
    )
    """<p>The unique identifier of the dataset generation.</p>"""
    status: (
        "capo_bedrock_agentcore.types.dataset_generation_status.DatasetGenerationStatus"
    )
    """<p>The status of the dataset generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetGenerationResponse) -> dict:
    out: dict = {}
    out["generationId"] = value["generation_id"]
    import capo_bedrock_agentcore.types.dataset_generation_status

    out["status"] = (
        capo_bedrock_agentcore.types.dataset_generation_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteDatasetGenerationResponse:
    out: DeleteDatasetGenerationResponse = {}  # type: ignore[typeddict-item]
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    else:
        out["generation_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.dataset_generation_status

        out["status"] = (
            capo_bedrock_agentcore.types.dataset_generation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.dataset_generation_status.DatasetGenerationStatus",
            "",
        )
    return out
