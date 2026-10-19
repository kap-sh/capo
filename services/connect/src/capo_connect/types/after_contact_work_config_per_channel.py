"""Generated from Smithy shape ``com.amazonaws.connect#AfterContactWorkConfigPerChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.after_contact_work_config
    import capo_connect.types.channel


class AfterContactWorkConfigPerChannel(TypedDict, closed=True):
    channel: "capo_connect.types.channel.Channel"
    """<p>The channel for this ACW timeout configuration. Valid values: VOICE, CHAT, TASK, EMAIL.</p>"""
    after_contact_work_config: (
        "capo_connect.types.after_contact_work_config.AfterContactWorkConfig"
    )
    """<p>The ACW timeout settings for this channel.</p>"""
    agent_first_callback_after_contact_work_config: NotRequired[
        "capo_connect.types.after_contact_work_config.AfterContactWorkConfig"
    ]
    """<p>The ACW timeout settings for agent-first callbacks. This setting only applies to the VOICE channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AfterContactWorkConfigPerChannel) -> dict:
    out: dict = {}
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    import capo_connect.types.after_contact_work_config

    out["AfterContactWorkConfig"] = (
        capo_connect.types.after_contact_work_config.serialize_json(
            value["after_contact_work_config"]
        )
    )
    if "agent_first_callback_after_contact_work_config" in value:
        import capo_connect.types.after_contact_work_config

        out["AgentFirstCallbackAfterContactWorkConfig"] = (
            capo_connect.types.after_contact_work_config.serialize_json(
                value["agent_first_callback_after_contact_work_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AfterContactWorkConfigPerChannel:
    out: AfterContactWorkConfigPerChannel = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    if data.get("AfterContactWorkConfig") is not None:
        import capo_connect.types.after_contact_work_config

        out["after_contact_work_config"] = (
            capo_connect.types.after_contact_work_config.deserialize_json(
                data["AfterContactWorkConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AfterContactWorkConfigPerChannel.after_contact_work_config required"
        )
    if data.get("AgentFirstCallbackAfterContactWorkConfig") is not None:
        import capo_connect.types.after_contact_work_config

        out["agent_first_callback_after_contact_work_config"] = (
            capo_connect.types.after_contact_work_config.deserialize_json(
                data["AgentFirstCallbackAfterContactWorkConfig"]
            )
        )
    return out
