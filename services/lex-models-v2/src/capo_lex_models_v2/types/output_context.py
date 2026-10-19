"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OutputContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.context_time_to_live_in_seconds
    import capo_lex_models_v2.types.context_turns_to_live
    import capo_lex_models_v2.types.name


class OutputContext(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the output context.</p>"""
    time_to_live_in_seconds: "capo_lex_models_v2.types.context_time_to_live_in_seconds.ContextTimeToLiveInSeconds"
    """<p>The amount of time, in seconds, that the output context should remain active. The time is figured from the first time the context is sent to the user.</p>"""
    turns_to_live: "capo_lex_models_v2.types.context_turns_to_live.ContextTurnsToLive"
    """<p>The number of conversation turns that the output context should remain active. The number of turns is counted from the first time that the context is sent to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["timeToLiveInSeconds"] = value["time_to_live_in_seconds"]
    out["turnsToLive"] = value["turns_to_live"]
    return out


def deserialize_json(data: dict) -> OutputContext:
    out: OutputContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("timeToLiveInSeconds") is not None:
        out["time_to_live_in_seconds"] = data["timeToLiveInSeconds"]
    else:
        out["time_to_live_in_seconds"] = 0
    if data.get("turnsToLive") is not None:
        out["turns_to_live"] = data["turnsToLive"]
    else:
        out["turns_to_live"] = 0
    return out
