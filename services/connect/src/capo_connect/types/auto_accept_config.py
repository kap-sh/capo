"""Generated from Smithy shape ``com.amazonaws.connect#AutoAcceptConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_first_callback_auto_accept
    import capo_connect.types.auto_accept
    import capo_connect.types.channel


class AutoAcceptConfig(TypedDict, closed=True):
    channel: "capo_connect.types.channel.Channel"
    """<p>The channel for this auto-accept configuration. Valid values: VOICE, CHAT, TASK, EMAIL.</p>"""
    auto_accept: "capo_connect.types.auto_accept.AutoAccept"
    """<p>Indicates whether auto-accept is enabled for this channel. When enabled, available agents are automatically connected to contacts from this channel.</p>"""
    agent_first_callback_auto_accept: NotRequired[
        "capo_connect.types.agent_first_callback_auto_accept.AgentFirstCallbackAutoAccept"
    ]
    """<p>Indicates whether auto-accept is enabled for agent-first callbacks. This setting only applies to the VOICE channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoAcceptConfig) -> dict:
    out: dict = {}
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    out["AutoAccept"] = value.get("auto_accept", False)
    if "agent_first_callback_auto_accept" in value:
        out["AgentFirstCallbackAutoAccept"] = value["agent_first_callback_auto_accept"]
    return out


def deserialize_json(data: dict) -> AutoAcceptConfig:
    out: AutoAcceptConfig = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    if data.get("AutoAccept") is not None:
        out["auto_accept"] = data["AutoAccept"]
    else:
        out["auto_accept"] = False
    if data.get("AgentFirstCallbackAutoAccept") is not None:
        out["agent_first_callback_auto_accept"] = data["AgentFirstCallbackAutoAccept"]
    return out
