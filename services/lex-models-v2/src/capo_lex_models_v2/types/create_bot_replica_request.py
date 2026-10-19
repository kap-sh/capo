"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.replica_region


class CreateBotReplicaRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The request for the unique bot ID of the source bot to be replicated in the secondary region.</p>"""
    replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the secondary region that will be used in the replication of the source bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotReplicaRequest) -> dict:
    out: dict = {}
    out["replicaRegion"] = value["replica_region"]
    return out


def deserialize_json(data: dict) -> CreateBotReplicaRequest:
    out: CreateBotReplicaRequest = {}  # type: ignore[typeddict-item]
    if data.get("replicaRegion") is not None:
        out["replica_region"] = data["replicaRegion"]
    else:
        out["replica_region"] = ""
    return out
