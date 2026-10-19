"""Generated from Smithy shape ``com.amazonaws.mgn#ChangeServerLifeCycleStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle
    import capo_mgn.types.source_server_id


class ChangeServerLifeCycleStateRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>The request to change the source server migration lifecycle state by source server ID.</p>"""
    life_cycle: "capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle"
    """<p>The request to change the source server migration lifecycle state.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The request to change the source server migration account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeServerLifeCycleStateRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    import capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle

    out["lifeCycle"] = (
        capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle.serialize_json(
            value["life_cycle"]
        )
    )
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ChangeServerLifeCycleStateRequest:
    out: ChangeServerLifeCycleStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("lifeCycle") is not None:
        import capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle

        out["life_cycle"] = (
            capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle.deserialize_json(
                data["lifeCycle"]
            )
        )
    else:
        raise DeserializationError(
            "ChangeServerLifeCycleStateRequest.life_cycle required"
        )
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
