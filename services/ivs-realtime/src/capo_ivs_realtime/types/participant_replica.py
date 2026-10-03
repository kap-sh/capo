"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantReplica``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.replication_state
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_session_id


class ParticipantReplica(TypedDict, closed=True):
    source_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage from which this participant is replicated.</p>"""
    participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId"
    """<p>Participant ID of the publisher that will be replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed"> create a self signed token</a>.</p>"""
    source_session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of the session within the source stage.</p>"""
    destination_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage where the participant is replicated.</p>"""
    destination_session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of the session within the destination stage.</p>"""
    replication_state: "capo_ivs_realtime.types.replication_state.ReplicationState"
    """<p>Replica’s current replication state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantReplica) -> dict:
    out: dict = {}
    out["sourceStageArn"] = value["source_stage_arn"]
    out["participantId"] = value["participant_id"]
    out["sourceSessionId"] = value["source_session_id"]
    out["destinationStageArn"] = value["destination_stage_arn"]
    out["destinationSessionId"] = value["destination_session_id"]
    out["replicationState"] = value["replication_state"]
    return out


def deserialize_json(data: dict) -> ParticipantReplica:
    out: ParticipantReplica = {}  # type: ignore[typeddict-item]
    if data.get("sourceStageArn") is not None:
        out["source_stage_arn"] = data["sourceStageArn"]
    else:
        raise DeserializationError("ParticipantReplica.source_stage_arn required")
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError("ParticipantReplica.participant_id required")
    if data.get("sourceSessionId") is not None:
        out["source_session_id"] = data["sourceSessionId"]
    else:
        raise DeserializationError("ParticipantReplica.source_session_id required")
    if data.get("destinationStageArn") is not None:
        out["destination_stage_arn"] = data["destinationStageArn"]
    else:
        raise DeserializationError("ParticipantReplica.destination_stage_arn required")
    if data.get("destinationSessionId") is not None:
        out["destination_session_id"] = data["destinationSessionId"]
    else:
        raise DeserializationError("ParticipantReplica.destination_session_id required")
    if data.get("replicationState") is not None:
        out["replication_state"] = data["replicationState"]
    else:
        raise DeserializationError("ParticipantReplica.replication_state required")
    return out
