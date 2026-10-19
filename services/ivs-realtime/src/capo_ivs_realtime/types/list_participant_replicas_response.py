"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantReplicasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.participant_replica_list


class ListParticipantReplicasResponse(TypedDict, closed=True):
    replicas: "capo_ivs_realtime.types.participant_replica_list.ParticipantReplicaList"
    """<p>List of all participant replicas.</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more participants than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantReplicasResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.participant_replica_list

    out["replicas"] = capo_ivs_realtime.types.participant_replica_list.serialize_json(
        value["replicas"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListParticipantReplicasResponse:
    out: ListParticipantReplicasResponse = {}  # type: ignore[typeddict-item]
    if data.get("replicas") is not None:
        import capo_ivs_realtime.types.participant_replica_list

        out["replicas"] = (
            capo_ivs_realtime.types.participant_replica_list.deserialize_json(
                data["replicas"]
            )
        )
    else:
        out["replicas"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
