"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.channel_id
    import capo_transcribe_streaming.types.participant_role


class ChannelDefinition(TypedDict, closed=True):
    channel_id: "capo_transcribe_streaming.types.channel_id.ChannelId"
    """<p>Specify the audio channel you want to define.</p>"""
    participant_role: "capo_transcribe_streaming.types.participant_role.ParticipantRole"
    """<p>Specify the speaker you want to define. Omitting this parameter is equivalent to specifying both participants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelDefinition) -> dict:
    out: dict = {}
    out["ChannelId"] = value.get("channel_id", 0)
    import capo_transcribe_streaming.types.participant_role

    out["ParticipantRole"] = (
        capo_transcribe_streaming.types.participant_role.serialize_json(
            value["participant_role"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChannelDefinition:
    out: ChannelDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = 0
    if data.get("ParticipantRole") is not None:
        import capo_transcribe_streaming.types.participant_role

        out["participant_role"] = (
            capo_transcribe_streaming.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    else:
        import typing

        out["participant_role"] = typing.cast(
            "capo_transcribe_streaming.types.participant_role.ParticipantRole", ""
        )
    return out
