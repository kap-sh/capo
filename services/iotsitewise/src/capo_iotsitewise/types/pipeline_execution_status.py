"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.pipeline_execution_state
    import capo_iotsitewise.types.pipeline_execution_state_details


class PipelineExecutionStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.pipeline_execution_state.PipelineExecutionState"
    """<p>Current state of the pipeline execution.</p>"""
    state_details: NotRequired[
        "capo_iotsitewise.types.pipeline_execution_state_details.PipelineExecutionStateDetails"
    ]
    """<p>Additional information about the execution outcome. Populated when the execution has terminated (failed or cancelled).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineExecutionStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.pipeline_execution_state

    out["state"] = capo_iotsitewise.types.pipeline_execution_state.serialize_json(
        value["state"]
    )
    if "state_details" in value:
        import capo_iotsitewise.types.pipeline_execution_state_details

        out["stateDetails"] = (
            capo_iotsitewise.types.pipeline_execution_state_details.serialize_json(
                value["state_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipelineExecutionStatus:
    out: PipelineExecutionStatus = {}  # type: ignore[typeddict-item]
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
    if data.get("stateDetails") is not None:
        import capo_iotsitewise.types.pipeline_execution_state_details

        out["state_details"] = (
            capo_iotsitewise.types.pipeline_execution_state_details.deserialize_json(
                data["stateDetails"]
            )
        )
    return out
