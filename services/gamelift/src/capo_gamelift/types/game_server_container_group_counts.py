"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerContainerGroupCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.whole_number


class GameServerContainerGroupCounts(TypedDict, closed=True):
    pending: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p> The number of container groups that are starting up but haven't yet registered. </p>"""
    active: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p> The number of container groups that have active game sessions. </p>"""
    idle: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p> The number of container groups that have no active game sessions. </p>"""
    terminating: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p> The number of container groups that are in the process of shutting down. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerContainerGroupCounts) -> dict:
    out: dict = {}
    if "pending" in value:
        out["PENDING"] = value["pending"]
    if "active" in value:
        out["ACTIVE"] = value["active"]
    if "idle" in value:
        out["IDLE"] = value["idle"]
    if "terminating" in value:
        out["TERMINATING"] = value["terminating"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServerContainerGroupCounts:
    out: GameServerContainerGroupCounts = {}  # type: ignore[typeddict-item]
    if data.get("PENDING") is not None:
        out["pending"] = data["PENDING"]
    if data.get("ACTIVE") is not None:
        out["active"] = data["ACTIVE"]
    if data.get("IDLE") is not None:
        out["idle"] = data["IDLE"]
    if data.get("TERMINATING") is not None:
        out["terminating"] = data["TERMINATING"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerContainerGroupCounts) -> dict:
    out: dict = {}
    if "pending" in value:
        out["PENDING"] = value["pending"]
    if "active" in value:
        out["ACTIVE"] = value["active"]
    if "idle" in value:
        out["IDLE"] = value["idle"]
    if "terminating" in value:
        out["TERMINATING"] = value["terminating"]
    return out


def deserialize_cbor(data: dict) -> GameServerContainerGroupCounts:
    out: GameServerContainerGroupCounts = {}  # type: ignore[typeddict-item]
    if data.get("PENDING") is not None:
        out["pending"] = data["PENDING"]
    if data.get("ACTIVE") is not None:
        out["active"] = data["ACTIVE"]
    if data.get("IDLE") is not None:
        out["idle"] = data["IDLE"]
    if data.get("TERMINATING") is not None:
        out["terminating"] = data["TERMINATING"]
    return out
