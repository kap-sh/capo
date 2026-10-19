"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#OutputContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.context_time_to_live_in_seconds
    import capo_lex_model_building_service.types.context_turns_to_live
    import capo_lex_model_building_service.types.output_context_name


class OutputContext(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.output_context_name.OutputContextName"
    """<p>The name of the context.</p>"""
    time_to_live_in_seconds: "capo_lex_model_building_service.types.context_time_to_live_in_seconds.ContextTimeToLiveInSeconds"
    """<p>The number of seconds that the context should be active after it is first sent in a <code>PostContent</code> or <code>PostText</code> response. You can set the value between 5 and 86,400 seconds (24 hours).</p>"""
    turns_to_live: (
        "capo_lex_model_building_service.types.context_turns_to_live.ContextTurnsToLive"
    )
    """<p>The number of conversation turns that the context should be active. A conversation turn is one <code>PostContent</code> or <code>PostText</code> request and the corresponding response from Amazon Lex.</p>"""


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
