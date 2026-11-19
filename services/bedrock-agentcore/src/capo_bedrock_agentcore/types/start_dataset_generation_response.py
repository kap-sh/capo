"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartDatasetGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.dataset_generation_id
    import capo_bedrock_agentcore.types.dataset_generation_name
    import capo_bedrock_agentcore.types.dataset_generation_status
    import capo_bedrock_agentcore.types.dataset_id


class StartDatasetGenerationResponse(TypedDict, closed=True):
    generation_id: (
        "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId"
    )
    """<p>The unique identifier of the dataset generation.</p>"""
    name: "capo_bedrock_agentcore.types.dataset_generation_name.DatasetGenerationName"
    """<p>The name of the dataset generation.</p>"""
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    status: (
        "capo_bedrock_agentcore.types.dataset_generation_status.DatasetGenerationStatus"
    )
    """<p>The status of the dataset generation.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the dataset generation started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDatasetGenerationResponse) -> dict:
    out: dict = {}
    out["generationId"] = value["generation_id"]
    out["name"] = value["name"]
    out["datasetId"] = value["dataset_id"]
    import capo_bedrock_agentcore.types.dataset_generation_status

    out["status"] = (
        capo_bedrock_agentcore.types.dataset_generation_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["createdAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> StartDatasetGenerationResponse:
    out: StartDatasetGenerationResponse = {}  # type: ignore[typeddict-item]
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    else:
        out["generation_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
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
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
