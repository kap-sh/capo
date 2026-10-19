"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_execution_state
    import capo_iotsitewise.types.compute_node_execution_state_details


class ComputeNodeExecutionStatus(TypedDict, closed=True):
    state: (
        "capo_iotsitewise.types.compute_node_execution_state.ComputeNodeExecutionState"
    )
    """<p>Current state of the compute node execution.</p>"""
    state_details: NotRequired[
        "capo_iotsitewise.types.compute_node_execution_state_details.ComputeNodeExecutionStateDetails"
    ]
    """<p>Additional information about the compute node's failure. Populated when the compute node has failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeExecutionStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.compute_node_execution_state

    out["state"] = capo_iotsitewise.types.compute_node_execution_state.serialize_json(
        value["state"]
    )
    if "state_details" in value:
        import capo_iotsitewise.types.compute_node_execution_state_details

        out["stateDetails"] = (
            capo_iotsitewise.types.compute_node_execution_state_details.serialize_json(
                value["state_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComputeNodeExecutionStatus:
    out: ComputeNodeExecutionStatus = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.compute_node_execution_state

        out["state"] = (
            capo_iotsitewise.types.compute_node_execution_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.compute_node_execution_state.ComputeNodeExecutionState",
            "",
        )
    if data.get("stateDetails") is not None:
        import capo_iotsitewise.types.compute_node_execution_state_details

        out["state_details"] = (
            capo_iotsitewise.types.compute_node_execution_state_details.deserialize_json(
                data["stateDetails"]
            )
        )
    return out
