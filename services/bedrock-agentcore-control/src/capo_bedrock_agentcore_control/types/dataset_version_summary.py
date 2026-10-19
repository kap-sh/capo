"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_version


class DatasetVersionSummary(TypedDict, closed=True):
    dataset_version: (
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    """<p> The version number of this published snapshot. </p>"""
    example_count: "int"
    """<p> The number of examples in this version. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when this version was published. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetVersionSummary) -> dict:
    out: dict = {}
    out["datasetVersion"] = value["dataset_version"]
    out["exampleCount"] = value["example_count"]
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
