"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DialogAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.dialog_action_type
    import capo_lex_runtime_v2.types.elicit_sub_slot
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.style_type


class DialogAction(TypedDict, closed=True):
    type: "capo_lex_runtime_v2.types.dialog_action_type.DialogActionType"
    """<p>The next action that the bot should take in its interaction with the user. The following values are possible:</p> <ul> <li> <p> <code>Close</code> – Indicates that there will not be a response from the user. For example, the statement "Your order has been placed" does not require a response.</p> </li> <li> <p> <code>ConfirmIntent</code> – The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as "Place the order?"</p> </li> <li> <p> <code>Delegate</code> – The next action is determined by Amazon Lex V2.</p> </li> <li> <p> <code>ElicitIntent</code> – The next action is to elicit an intent from the user.</p> </li> <li> <p> <code>ElicitSlot</code> – The next action is to elicit a slot value from the user.</p> </li> </ul>"""
    slot_to_elicit: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the slot that should be elicited from the user.</p>"""
    slot_elicitation_style: NotRequired[
        "capo_lex_runtime_v2.types.style_type.StyleType"
    ]
    """<p>Configures the slot to use spell-by-letter or spell-by-word style. When you use a style on a slot, users can spell out their input to make it clear to your bot.</p> <ul> <li> <p>Spell by letter - "b" "o" "b"</p> </li> <li> <p>Spell by word - "b as in boy" "o as in oscar" "b as in boy"</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/spelling-styles.html"> Using spelling to enter slot values </a>.</p>"""
    sub_slot_to_elicit: NotRequired[
        "capo_lex_runtime_v2.types.elicit_sub_slot.ElicitSubSlot"
    ]
    """<p>The name of the constituent sub slot of the composite slot specified in slotToElicit that should be elicited from the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogAction) -> dict:
    out: dict = {}
    import capo_lex_runtime_v2.types.dialog_action_type

    out["type"] = capo_lex_runtime_v2.types.dialog_action_type.serialize_json(
        value["type"]
    )
    if "slot_to_elicit" in value:
        out["slotToElicit"] = value["slot_to_elicit"]
    if "slot_elicitation_style" in value:
        import capo_lex_runtime_v2.types.style_type

        out["slotElicitationStyle"] = (
            capo_lex_runtime_v2.types.style_type.serialize_json(
                value["slot_elicitation_style"]
            )
        )
    if "sub_slot_to_elicit" in value:
        import capo_lex_runtime_v2.types.elicit_sub_slot

        out["subSlotToElicit"] = (
            capo_lex_runtime_v2.types.elicit_sub_slot.serialize_json(
                value["sub_slot_to_elicit"]
            )
        )
    return out


def deserialize_json(data: dict) -> DialogAction:
    out: DialogAction = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_lex_runtime_v2.types.dialog_action_type

        out["type"] = capo_lex_runtime_v2.types.dialog_action_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DialogAction.type required")
    if data.get("slotToElicit") is not None:
        out["slot_to_elicit"] = data["slotToElicit"]
    if data.get("slotElicitationStyle") is not None:
        import capo_lex_runtime_v2.types.style_type

        out["slot_elicitation_style"] = (
            capo_lex_runtime_v2.types.style_type.deserialize_json(
                data["slotElicitationStyle"]
            )
        )
    if data.get("subSlotToElicit") is not None:
        import capo_lex_runtime_v2.types.elicit_sub_slot

        out["sub_slot_to_elicit"] = (
            capo_lex_runtime_v2.types.elicit_sub_slot.deserialize_json(
                data["subSlotToElicit"]
            )
        )
    return out
