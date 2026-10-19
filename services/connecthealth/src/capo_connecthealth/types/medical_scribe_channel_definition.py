"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_scribe_channel_id
    import capo_connecthealth.types.medical_scribe_participant_role


class MedicalScribeChannelDefinition(TypedDict, closed=True):
    channel_id: (
        "capo_connecthealth.types.medical_scribe_channel_id.MedicalScribeChannelId"
    )
    """<p>The channel identifier</p>"""
    participant_role: "capo_connecthealth.types.medical_scribe_participant_role.MedicalScribeParticipantRole"
    """<p>The role of the participant on this channel</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeChannelDefinition) -> dict:
    out: dict = {}
    out["channelId"] = value["channel_id"]
    import capo_connecthealth.types.medical_scribe_participant_role

    out["participantRole"] = (
        capo_connecthealth.types.medical_scribe_participant_role.serialize_json(
            value["participant_role"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeChannelDefinition:
    out: MedicalScribeChannelDefinition = {}  # type: ignore[typeddict-item]
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    else:
        out["channel_id"] = 0
    if data.get("participantRole") is not None:
        import capo_connecthealth.types.medical_scribe_participant_role

        out["participant_role"] = (
            capo_connecthealth.types.medical_scribe_participant_role.deserialize_json(
                data["participantRole"]
            )
        )
    else:
        import typing

        out["participant_role"] = typing.cast(
            "capo_connecthealth.types.medical_scribe_participant_role.MedicalScribeParticipantRole",
            "",
        )
    return out
