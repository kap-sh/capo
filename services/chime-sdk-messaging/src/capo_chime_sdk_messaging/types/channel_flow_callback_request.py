"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlowCallbackRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.callback_id_type
    import capo_chime_sdk_messaging.types.channel_message_callback
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.non_nullable_boolean


class ChannelFlowCallbackRequest(TypedDict, closed=True):
    callback_id: "capo_chime_sdk_messaging.types.callback_id_type.CallbackIdType"
    """<p>The identifier passed to the processor by the service when invoked. Use the identifier to call back the service.</p>"""
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    delete_resource: (
        "capo_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
    )
    """<p>When a processor determines that a message needs to be <code>DENIED</code>, pass this parameter with a value of true.</p>"""
    channel_message: (
        "capo_chime_sdk_messaging.types.channel_message_callback.ChannelMessageCallback"
    )
    """<p>Stores information about the processed message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlowCallbackRequest) -> dict:
    out: dict = {}
    out["CallbackId"] = value["callback_id"]
    out["DeleteResource"] = value.get("delete_resource", False)
    import capo_chime_sdk_messaging.types.channel_message_callback

    out["ChannelMessage"] = (
        capo_chime_sdk_messaging.types.channel_message_callback.serialize_json(
            value["channel_message"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChannelFlowCallbackRequest:
    out: ChannelFlowCallbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("CallbackId") is not None:
        out["callback_id"] = data["CallbackId"]
    else:
        raise DeserializationError("ChannelFlowCallbackRequest.callback_id required")
    if data.get("DeleteResource") is not None:
        out["delete_resource"] = data["DeleteResource"]
    else:
        out["delete_resource"] = False
    if data.get("ChannelMessage") is not None:
        import capo_chime_sdk_messaging.types.channel_message_callback

        out["channel_message"] = (
            capo_chime_sdk_messaging.types.channel_message_callback.deserialize_json(
                data["ChannelMessage"]
            )
        )
    else:
        raise DeserializationError(
            "ChannelFlowCallbackRequest.channel_message required"
        )
    return out


def redact_sensitive(value: ChannelFlowCallbackRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_message" in value:
        import capo_chime_sdk_messaging.types.channel_message_callback

        out["channel_message"] = (
            capo_chime_sdk_messaging.types.channel_message_callback.redact_sensitive(
                value["channel_message"]
            )
        )
    return out
