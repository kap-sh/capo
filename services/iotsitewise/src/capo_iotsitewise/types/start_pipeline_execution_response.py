"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StartPipelineExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class StartPipelineExecutionResponse(TypedDict, closed=True):
    pipeline_execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the created pipeline execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPipelineExecutionResponse) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_json(data: dict) -> StartPipelineExecutionResponse:
    out: StartPipelineExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        out["pipeline_execution_id"] = ""
    return out
