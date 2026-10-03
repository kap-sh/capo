"""Generated from Smithy shape ``com.amazonaws.qbusiness#ConfigurationEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_qbusiness.types.attribute_filter
    import capo_qbusiness.types.chat_mode
    import capo_qbusiness.types.chat_mode_configuration


class ConfigurationEvent(TypedDict, closed=True):
    chat_mode: NotRequired["capo_qbusiness.types.chat_mode.ChatMode"]
    """<p>The chat modes available to an Amazon Q Business end user.</p> <ul> <li> <p> <code>RETRIEVAL_MODE</code> - The default chat mode for an Amazon Q Business application. When this mode is enabled, Amazon Q Business generates responses only from data sources connected to an Amazon Q Business application.</p> </li> <li> <p> <code>CREATOR_MODE</code> - By selecting this mode, users can choose to generate responses only from the LLM knowledge, without consulting connected data sources, for a chat request.</p> </li> <li> <p> <code>PLUGIN_MODE</code> - By selecting this mode, users can choose to use plugins in chat.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html">Admin controls and guardrails</a>, <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html">Plugins</a>, and <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope">Conversation settings</a>.</p>"""
    chat_mode_configuration: NotRequired[
        "capo_qbusiness.types.chat_mode_configuration.ChatModeConfiguration"
    ]
    attribute_filter: NotRequired[
        "capo_qbusiness.types.attribute_filter.AttributeFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "chat_mode" in value:
        import capo_qbusiness.types.chat_mode

        out["chatMode"] = capo_qbusiness.types.chat_mode.serialize_json(
            value["chat_mode"]
        )
    if "chat_mode_configuration" in value:
        import capo_qbusiness.types.chat_mode_configuration

        out["chatModeConfiguration"] = (
            capo_qbusiness.types.chat_mode_configuration.serialize_json(
                value["chat_mode_configuration"]
            )
        )
    if "attribute_filter" in value:
        import capo_qbusiness.types.attribute_filter

        out["attributeFilter"] = capo_qbusiness.types.attribute_filter.serialize_json(
            value["attribute_filter"]
        )
    return out


def deserialize_json(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if data.get("chatMode") is not None:
        import capo_qbusiness.types.chat_mode

        out["chat_mode"] = capo_qbusiness.types.chat_mode.deserialize_json(
            data["chatMode"]
        )
    if data.get("chatModeConfiguration") is not None:
        import capo_qbusiness.types.chat_mode_configuration

        out["chat_mode_configuration"] = (
            capo_qbusiness.types.chat_mode_configuration.deserialize_json(
                data["chatModeConfiguration"]
            )
        )
    if data.get("attributeFilter") is not None:
        import capo_qbusiness.types.attribute_filter

        out["attribute_filter"] = (
            capo_qbusiness.types.attribute_filter.deserialize_json(
                data["attributeFilter"]
            )
        )
    return out


def serialize_event_json(value: ConfigurationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "configurationEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConfigurationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
