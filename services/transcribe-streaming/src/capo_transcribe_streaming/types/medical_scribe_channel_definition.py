"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_channel_id
    import capo_transcribe_streaming.types.medical_scribe_participant_role


class MedicalScribeChannelDefinition(TypedDict, closed=True):
    channel_id: "capo_transcribe_streaming.types.medical_scribe_channel_id.MedicalScribeChannelId"
    """<p>Specify the audio channel you want to define.</p>"""
    participant_role: "capo_transcribe_streaming.types.medical_scribe_participant_role.MedicalScribeParticipantRole"
    """<p>Specify the participant that you want to flag. The allowed options are <code>CLINICIAN</code> and <code>PATIENT</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeChannelDefinition) -> dict:
    out: dict = {}
    out["ChannelId"] = value.get("channel_id", 0)
    import capo_transcribe_streaming.types.medical_scribe_participant_role

    out["ParticipantRole"] = (
        capo_transcribe_streaming.types.medical_scribe_participant_role.serialize_json(
            value["participant_role"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeChannelDefinition:
    out: MedicalScribeChannelDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = 0
    if data.get("ParticipantRole") is not None:
        import capo_transcribe_streaming.types.medical_scribe_participant_role

        out["participant_role"] = (
            capo_transcribe_streaming.types.medical_scribe_participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    else:
        import typing

        out["participant_role"] = typing.cast(
            "capo_transcribe_streaming.types.medical_scribe_participant_role.MedicalScribeParticipantRole",
            "",
        )
    return out
