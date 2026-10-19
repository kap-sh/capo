"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetParticipantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_session_id


class GetParticipantRequest(TypedDict, closed=True):
    stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of a session within the stage.</p>"""
    participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId"
    """<p>Unique identifier for the participant. This is assigned by IVS and returned by <a>CreateParticipantToken</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetParticipantRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["sessionId"] = value["session_id"]
    out["participantId"] = value["participant_id"]
    return out


def deserialize_json(data: dict) -> GetParticipantRequest:
    out: GetParticipantRequest = {}  # type: ignore[typeddict-item]
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        out["stage_arn"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    else:
        out["participant_id"] = ""
    return out
