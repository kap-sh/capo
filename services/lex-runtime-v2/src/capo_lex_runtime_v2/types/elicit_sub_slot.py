"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ElicitSubSlot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.elicit_sub_slot
    import capo_lex_runtime_v2.types.non_empty_string


class ElicitSubSlot(TypedDict, closed=True):
    name: "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The name of the slot that should be elicited from the user.</p>"""
    sub_slot_to_elicit: NotRequired[
        "capo_lex_runtime_v2.types.elicit_sub_slot.ElicitSubSlot"
    ]
    """<p>The field is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElicitSubSlot) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "sub_slot_to_elicit" in value:
        import capo_lex_runtime_v2.types.elicit_sub_slot

        out["subSlotToElicit"] = (
            capo_lex_runtime_v2.types.elicit_sub_slot.serialize_json(
                value["sub_slot_to_elicit"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElicitSubSlot:
    out: ElicitSubSlot = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("subSlotToElicit") is not None:
        import capo_lex_runtime_v2.types.elicit_sub_slot

        out["sub_slot_to_elicit"] = (
            capo_lex_runtime_v2.types.elicit_sub_slot.deserialize_json(
                data["subSlotToElicit"]
            )
        )
    return out
