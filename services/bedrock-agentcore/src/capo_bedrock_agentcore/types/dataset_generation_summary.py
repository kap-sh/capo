"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetGenerationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.dataset_generation_description
    import capo_bedrock_agentcore.types.dataset_generation_id
    import capo_bedrock_agentcore.types.dataset_generation_name
    import capo_bedrock_agentcore.types.dataset_generation_status
    import capo_bedrock_agentcore.types.dataset_id
    import capo_bedrock_agentcore.types.scenario_type


class DatasetGenerationSummary(TypedDict, closed=True):
    generation_id: (
        "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId"
    )
    """<p>The unique identifier of the dataset generation.</p>"""
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    name: "capo_bedrock_agentcore.types.dataset_generation_name.DatasetGenerationName"
    """<p>The name of the dataset generation.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.dataset_generation_description.DatasetGenerationDescription"
    ]
    """<p>The description of the dataset generation.</p>"""
    scenario_type: "capo_bedrock_agentcore.types.scenario_type.ScenarioType"
    """<p>The type of scenario the generation produces.</p>"""
    status: (
        "capo_bedrock_agentcore.types.dataset_generation_status.DatasetGenerationStatus"
    )
    """<p>The status of the dataset generation.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the dataset generation started.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The time at which the dataset generation finished. Present only when the generation has finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetGenerationSummary) -> dict:
    out: dict = {}
    out["generationId"] = value["generation_id"]
    out["datasetId"] = value["dataset_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore.types.scenario_type

    out["scenarioType"] = capo_bedrock_agentcore.types.scenario_type.serialize_json(
        value["scenario_type"]
    )
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
    if "completed_at" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["completedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> DatasetGenerationSummary:
    out: DatasetGenerationSummary = {}  # type: ignore[typeddict-item]
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    else:
        out["generation_id"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("scenarioType") is not None:
        import capo_bedrock_agentcore.types.scenario_type

        out["scenario_type"] = (
            capo_bedrock_agentcore.types.scenario_type.deserialize_json(
                data["scenarioType"]
            )
        )
    else:
        import typing

        out["scenario_type"] = typing.cast(
            "capo_bedrock_agentcore.types.scenario_type.ScenarioType", ""
        )
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
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    return out
