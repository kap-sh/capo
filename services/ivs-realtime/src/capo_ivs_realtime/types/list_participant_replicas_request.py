"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantReplicasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.max_participant_replica_results
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.stage_arn


class ListParticipantReplicasRequest(TypedDict, closed=True):
    source_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage where the participant is publishing.</p>"""
    participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId"
    """<p>Participant ID of the publisher that has been replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed">create a self signed token</a>.</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>The first participant to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs_realtime.types.max_participant_replica_results.MaxParticipantReplicaResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantReplicasRequest) -> dict:
    out: dict = {}
    out["sourceStageArn"] = value["source_stage_arn"]
    out["participantId"] = value["participant_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListParticipantReplicasRequest:
    out: ListParticipantReplicasRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceStageArn") is not None:
        out["source_stage_arn"] = data["sourceStageArn"]
    else:
        raise DeserializationError(
            "ListParticipantReplicasRequest.source_stage_arn required"
        )
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError(
            "ListParticipantReplicasRequest.participant_id required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
