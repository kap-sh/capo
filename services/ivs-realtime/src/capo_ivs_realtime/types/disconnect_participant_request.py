"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DisconnectParticipantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.disconnect_participant_reason
    import capo_ivs_realtime.types.participant_token_id
    import capo_ivs_realtime.types.stage_arn


class DisconnectParticipantRequest(TypedDict, closed=True):
    stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to which the participant is attached.</p>"""
    participant_id: "capo_ivs_realtime.types.participant_token_id.ParticipantTokenId"
    """<p>Identifier of the participant to be disconnected. IVS assigns this; it is returned by <a>CreateParticipantToken</a> (for streams using WebRTC ingest) or <a>CreateIngestConfiguration</a> (for streams using RTMP ingest).</p>"""
    reason: NotRequired[
        "capo_ivs_realtime.types.disconnect_participant_reason.DisconnectParticipantReason"
    ]
    """<p>Description of why this participant is being disconnected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectParticipantRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["participantId"] = value["participant_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> DisconnectParticipantRequest:
    out: DisconnectParticipantRequest = {}  # type: ignore[typeddict-item]
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        out["stage_arn"] = ""
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    else:
        out["participant_id"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
