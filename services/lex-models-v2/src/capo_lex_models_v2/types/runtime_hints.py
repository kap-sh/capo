"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RuntimeHints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_hints_intent_map


class RuntimeHints(TypedDict, closed=True):
    slot_hints: NotRequired[
        "capo_lex_models_v2.types.slot_hints_intent_map.SlotHintsIntentMap"
    ]
    """<p>A list of the slots in the intent that should have runtime hints added, and the phrases that should be added for each slot.</p> <p>The first level of the <code>slotHints</code> map is the name of the intent. The second level is the name of the slot within the intent. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html">Using hints to improve accuracy</a>.</p> <p>The intent name and slot name must exist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHints) -> dict:
    out: dict = {}
    if "slot_hints" in value:
        import capo_lex_models_v2.types.slot_hints_intent_map

        out["slotHints"] = (
            capo_lex_models_v2.types.slot_hints_intent_map.serialize_json(
                value["slot_hints"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeHints:
    out: RuntimeHints = {}  # type: ignore[typeddict-item]
    if data.get("slotHints") is not None:
        import capo_lex_models_v2.types.slot_hints_intent_map

        out["slot_hints"] = (
            capo_lex_models_v2.types.slot_hints_intent_map.deserialize_json(
                data["slotHints"]
            )
        )
    return out
