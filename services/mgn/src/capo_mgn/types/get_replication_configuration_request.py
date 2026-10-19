"""Generated from Smithy shape ``com.amazonaws.mgn#GetReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.source_server_id


class GetReplicationConfigurationRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Request to get Replication Configuration by Source Server ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Request to get Replication Configuration by Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReplicationConfigurationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> GetReplicationConfigurationRequest:
    out: GetReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
