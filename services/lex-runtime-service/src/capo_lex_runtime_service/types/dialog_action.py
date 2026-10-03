"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DialogAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.dialog_action_type
    import capo_lex_runtime_service.types.fulfillment_state
    import capo_lex_runtime_service.types.intent_name
    import capo_lex_runtime_service.types.message_format_type
    import capo_lex_runtime_service.types.string
    import capo_lex_runtime_service.types.string_map
    import capo_lex_runtime_service.types.text


class DialogAction(TypedDict, closed=True):
    type: "capo_lex_runtime_service.types.dialog_action_type.DialogActionType"
    """<p>The next action that the bot should take in its interaction with the user. The possible values are:</p> <ul> <li> <p> <code>ConfirmIntent</code> - The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as "Place the order?"</p> </li> <li> <p> <code>Close</code> - Indicates that the there will not be a response from the user. For example, the statement "Your order has been placed" does not require a response.</p> </li> <li> <p> <code>Delegate</code> - The next action is determined by Amazon Lex.</p> </li> <li> <p> <code>ElicitIntent</code> - The next action is to determine the intent that the user wants to fulfill.</p> </li> <li> <p> <code>ElicitSlot</code> - The next action is to elicit a slot value from the user.</p> </li> </ul>"""
    intent_name: NotRequired["capo_lex_runtime_service.types.intent_name.IntentName"]
    """<p>The name of the intent.</p>"""
    slots: NotRequired["capo_lex_runtime_service.types.string_map.StringMap"]
    """<p>Map of the slots that have been gathered and their values. </p>"""
    slot_to_elicit: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>The name of the slot that should be elicited from the user.</p>"""
    fulfillment_state: NotRequired[
        "capo_lex_runtime_service.types.fulfillment_state.FulfillmentState"
    ]
    """<p>The fulfillment state of the intent. The possible values are:</p> <ul> <li> <p> <code>Failed</code> - The Lambda function associated with the intent failed to fulfill the intent.</p> </li> <li> <p> <code>Fulfilled</code> - The intent has fulfilled by the Lambda function associated with the intent. </p> </li> <li> <p> <code>ReadyForFulfillment</code> - All of the information necessary for the intent is present and the intent ready to be fulfilled by the client application.</p> </li> </ul>"""
    message: NotRequired["capo_lex_runtime_service.types.text.Text"]
    """<p>The message that should be shown to the user. If you don't specify a message, Amazon Lex will use the message configured for the intent.</p>"""
    message_format: NotRequired[
        "capo_lex_runtime_service.types.message_format_type.MessageFormatType"
    ]
    """<ul> <li> <p> <code>PlainText</code> - The message contains plain UTF-8 text.</p> </li> <li> <p> <code>CustomPayload</code> - The message is a custom format for the client.</p> </li> <li> <p> <code>SSML</code> - The message contains text formatted for voice output.</p> </li> <li> <p> <code>Composite</code> - The message contains an escaped JSON object containing one or more messages. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/howitworks-manage-prompts.html">Message Groups</a>. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogAction) -> dict:
    out: dict = {}
    import capo_lex_runtime_service.types.dialog_action_type

    out["type"] = capo_lex_runtime_service.types.dialog_action_type.serialize_json(
        value["type"]
    )
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "slots" in value:
        import capo_lex_runtime_service.types.string_map

        out["slots"] = capo_lex_runtime_service.types.string_map.serialize_json(
            value["slots"]
        )
    if "slot_to_elicit" in value:
        out["slotToElicit"] = value["slot_to_elicit"]
    if "fulfillment_state" in value:
        import capo_lex_runtime_service.types.fulfillment_state

        out["fulfillmentState"] = (
            capo_lex_runtime_service.types.fulfillment_state.serialize_json(
                value["fulfillment_state"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "message_format" in value:
        import capo_lex_runtime_service.types.message_format_type

        out["messageFormat"] = (
            capo_lex_runtime_service.types.message_format_type.serialize_json(
                value["message_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> DialogAction:
    out: DialogAction = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_lex_runtime_service.types.dialog_action_type

        out["type"] = (
            capo_lex_runtime_service.types.dialog_action_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DialogAction.type required")
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    if data.get("slots") is not None:
        import capo_lex_runtime_service.types.string_map

        out["slots"] = capo_lex_runtime_service.types.string_map.deserialize_json(
            data["slots"]
        )
    if data.get("slotToElicit") is not None:
        out["slot_to_elicit"] = data["slotToElicit"]
    if data.get("fulfillmentState") is not None:
        import capo_lex_runtime_service.types.fulfillment_state

        out["fulfillment_state"] = (
            capo_lex_runtime_service.types.fulfillment_state.deserialize_json(
                data["fulfillmentState"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("messageFormat") is not None:
        import capo_lex_runtime_service.types.message_format_type

        out["message_format"] = (
            capo_lex_runtime_service.types.message_format_type.deserialize_json(
                data["messageFormat"]
            )
        )
    return out
