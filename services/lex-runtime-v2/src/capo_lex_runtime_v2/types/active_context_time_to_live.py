"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ActiveContextTimeToLive``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.active_context_time_to_live_in_seconds
    import capo_lex_runtime_v2.types.active_context_turns_to_live


class ActiveContextTimeToLive(TypedDict, closed=True):
    time_to_live_in_seconds: "capo_lex_runtime_v2.types.active_context_time_to_live_in_seconds.ActiveContextTimeToLiveInSeconds"
    """<p>The number of seconds that the context is active. You can specify between 5 and 86400 seconds (24 hours).</p>"""
    turns_to_live: "capo_lex_runtime_v2.types.active_context_turns_to_live.ActiveContextTurnsToLive"
    """<p>The number of turns that the context is active. You can specify up to 20 turns. Each request and response from the bot is a turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContextTimeToLive) -> dict:
    out: dict = {}
    out["timeToLiveInSeconds"] = value["time_to_live_in_seconds"]
    out["turnsToLive"] = value["turns_to_live"]
    return out


def deserialize_json(data: dict) -> ActiveContextTimeToLive:
    out: ActiveContextTimeToLive = {}  # type: ignore[typeddict-item]
    if data.get("timeToLiveInSeconds") is not None:
        out["time_to_live_in_seconds"] = data["timeToLiveInSeconds"]
    else:
        out["time_to_live_in_seconds"] = 0
    if data.get("turnsToLive") is not None:
        out["turns_to_live"] = data["turnsToLive"]
    else:
        out["turns_to_live"] = 0
    return out
