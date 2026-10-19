"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateSourceServerReplicationTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.replication_type
    import capo_mgn.types.source_server_id


class UpdateSourceServerReplicationTypeRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>ID of source server on which to update replication type.</p>"""
    replication_type: "capo_mgn.types.replication_type.ReplicationType"
    """<p>Replication type to which to update source server.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID on which to update replication type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSourceServerReplicationTypeRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    out["replicationType"] = value["replication_type"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UpdateSourceServerReplicationTypeRequest:
    out: UpdateSourceServerReplicationTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("replicationType") is not None:
        out["replication_type"] = data["replicationType"]
    else:
        out["replication_type"] = ""
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
