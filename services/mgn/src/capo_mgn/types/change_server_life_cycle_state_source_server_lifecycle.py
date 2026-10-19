"""Generated from Smithy shape ``com.amazonaws.mgn#ChangeServerLifeCycleStateSourceServerLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle_state


class ChangeServerLifeCycleStateSourceServerLifecycle(TypedDict, closed=True):
    state: "capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle_state.ChangeServerLifeCycleStateSourceServerLifecycleState"
    """<p>The request to change the source server migration lifecycle state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeServerLifeCycleStateSourceServerLifecycle) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> ChangeServerLifeCycleStateSourceServerLifecycle:
    out: ChangeServerLifeCycleStateSourceServerLifecycle = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out
