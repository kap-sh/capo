"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteRemoteSourceActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.remote_source_action_id


class DeleteRemoteSourceActionRequest(TypedDict, closed=True):
    remote_source_action_id: (
        "capo_mgn.types.remote_source_action_id.RemoteSourceActionID"
    )
    """<p>The unique identifier of the source action to delete.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRemoteSourceActionRequest) -> dict:
    out: dict = {}
    out["remoteSourceActionID"] = value["remote_source_action_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DeleteRemoteSourceActionRequest:
    out: DeleteRemoteSourceActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionID") is not None:
        out["remote_source_action_id"] = data["remoteSourceActionID"]
    else:
        out["remote_source_action_id"] = ""
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
