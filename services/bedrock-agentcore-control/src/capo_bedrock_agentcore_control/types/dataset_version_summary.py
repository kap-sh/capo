"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_version
    import capo_bedrock_agentcore_control.types.example_count_by_field


class DatasetVersionSummary(TypedDict, closed=True):
    dataset_version: (
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    """<p> The version number of this published snapshot. </p>"""
    example_count: "int"
    """<p> The number of examples in this version. </p>"""
    example_count_by_field: NotRequired[
        "capo_bedrock_agentcore_control.types.example_count_by_field.ExampleCountByField"
    ]
    """<p> The number of examples that have each field, for this version. Absent when the counts are unknown. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when this version was published. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetVersionSummary) -> dict:
    out: dict = {}
    out["datasetVersion"] = value["dataset_version"]
    out["exampleCount"] = value["example_count"]
    if "example_count_by_field" in value:
        import capo_bedrock_agentcore_control.types.example_count_by_field

        out["exampleCountByField"] = (
            capo_bedrock_agentcore_control.types.example_count_by_field.serialize_json(
                value["example_count_by_field"]
            )
        )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatasetVersionSummary:
    out: DatasetVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    else:
        out["dataset_version"] = ""
    if data.get("exampleCount") is not None:
        out["example_count"] = data["exampleCount"]
    else:
        out["example_count"] = 0
    if data.get("exampleCountByField") is not None:
        import capo_bedrock_agentcore_control.types.example_count_by_field

        out["example_count_by_field"] = (
            capo_bedrock_agentcore_control.types.example_count_by_field.deserialize_json(
                data["exampleCountByField"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
