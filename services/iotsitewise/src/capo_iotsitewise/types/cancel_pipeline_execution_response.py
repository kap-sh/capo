"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CancelPipelineExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.pipeline_execution_state


class CancelPipelineExecutionResponse(TypedDict, closed=True):
    state: "capo_iotsitewise.types.pipeline_execution_state.PipelineExecutionState"
    """<p>The current execution state of the pipeline. Can only be CANCELLING or CANCELLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelPipelineExecutionResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.pipeline_execution_state

    out["state"] = capo_iotsitewise.types.pipeline_execution_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> CancelPipelineExecutionResponse:
    out: CancelPipelineExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.pipeline_execution_state

        out["state"] = capo_iotsitewise.types.pipeline_execution_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.pipeline_execution_state.PipelineExecutionState", ""
        )
    return out
