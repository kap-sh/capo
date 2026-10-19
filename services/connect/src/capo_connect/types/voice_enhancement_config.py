"""Generated from Smithy shape ``com.amazonaws.connect#VoiceEnhancementConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.voice_enhancement_mode


class VoiceEnhancementConfig(TypedDict, closed=True):
    channel: "capo_connect.types.channel.Channel"
    """<p>The channel for this voice enhancement configuration. <b>Only <code>VOICE</code> is supported for this data type.</b> </p>"""
    voice_enhancement_mode: (
        "capo_connect.types.voice_enhancement_mode.VoiceEnhancementMode"
    )
    """<p>The voice enhancement mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEnhancementConfig) -> dict:
    out: dict = {}
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    import capo_connect.types.voice_enhancement_mode

    out["VoiceEnhancementMode"] = (
        capo_connect.types.voice_enhancement_mode.serialize_json(
            value["voice_enhancement_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> VoiceEnhancementConfig:
    out: VoiceEnhancementConfig = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    if data.get("VoiceEnhancementMode") is not None:
        import capo_connect.types.voice_enhancement_mode

        out["voice_enhancement_mode"] = (
            capo_connect.types.voice_enhancement_mode.deserialize_json(
                data["VoiceEnhancementMode"]
            )
        )
    else:
        import typing

        out["voice_enhancement_mode"] = typing.cast(
            "capo_connect.types.voice_enhancement_mode.VoiceEnhancementMode", ""
        )
    return out
