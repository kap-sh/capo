"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_state


class ExecutionStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.execution_state.ExecutionState"
    """<p>The current state of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.execution_state

    out["state"] = capo_iotsitewise.types.execution_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> ExecutionStatus:
    out: ExecutionStatus = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.execution_state

        out["state"] = capo_iotsitewise.types.execution_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.execution_state.ExecutionState", ""
        )
    return out
