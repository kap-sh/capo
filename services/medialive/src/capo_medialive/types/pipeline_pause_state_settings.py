"""Generated from Smithy shape ``com.amazonaws.medialive#PipelinePauseStateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.pipeline_id


class PipelinePauseStateSettings(TypedDict, closed=True):
    pipeline_id: NotRequired["capo_medialive.types.pipeline_id.PipelineId"]
    """Pipeline ID to pause ("PIPELINE_0" or "PIPELINE_1")."""


# --- restJson1 ser/de ---
def serialize_json(value: PipelinePauseStateSettings) -> dict:
    out: dict = {}
    if "pipeline_id" in value:
        import capo_medialive.types.pipeline_id

        out["pipelineId"] = capo_medialive.types.pipeline_id.serialize_json(
            value["pipeline_id"]
        )
    return out


def deserialize_json(data: dict) -> PipelinePauseStateSettings:
    out: PipelinePauseStateSettings = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        import capo_medialive.types.pipeline_id

        out["pipeline_id"] = capo_medialive.types.pipeline_id.deserialize_json(
            data["pipelineId"]
        )
    return out
