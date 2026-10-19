"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.dialog_action_type
    import capo_lex_models_v2.types.name


class DialogAction(TypedDict, closed=True):
    type: "capo_lex_models_v2.types.dialog_action_type.DialogActionType"
    """<p>The action that the bot should execute. </p>"""
    slot_to_elicit: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>If the dialog action is <code>ElicitSlot</code>, defines the slot to elicit from the user.</p>"""
    suppress_next_message: NotRequired[
        "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>When true the next message for the intent is not used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogAction) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.dialog_action_type

    out["type"] = capo_lex_models_v2.types.dialog_action_type.serialize_json(
        value["type"]
    )
    if "slot_to_elicit" in value:
        out["slotToElicit"] = value["slot_to_elicit"]
    if "suppress_next_message" in value:
        out["suppressNextMessage"] = value["suppress_next_message"]
    return out


def deserialize_json(data: dict) -> DialogAction:
    out: DialogAction = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_lex_models_v2.types.dialog_action_type

        out["type"] = capo_lex_models_v2.types.dialog_action_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_lex_models_v2.types.dialog_action_type.DialogActionType", ""
        )
    if data.get("slotToElicit") is not None:
        out["slot_to_elicit"] = data["slotToElicit"]
    if data.get("suppressNextMessage") is not None:
        out["suppress_next_message"] = data["suppressNextMessage"]
    return out
