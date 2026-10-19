"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnIntentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.user_turn_slot_output_map


class UserTurnIntentOutput(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the intent.</p>"""
    slots: NotRequired[
        "capo_lex_models_v2.types.user_turn_slot_output_map.UserTurnSlotOutputMap"
    ]
    """<p>The slots associated with the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnIntentOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "slots" in value:
        import capo_lex_models_v2.types.user_turn_slot_output_map

        out["slots"] = (
            capo_lex_models_v2.types.user_turn_slot_output_map.serialize_json(
                value["slots"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserTurnIntentOutput:
    out: UserTurnIntentOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("slots") is not None:
        import capo_lex_models_v2.types.user_turn_slot_output_map

        out["slots"] = (
            capo_lex_models_v2.types.user_turn_slot_output_map.deserialize_json(
                data["slots"]
            )
        )
    return out
