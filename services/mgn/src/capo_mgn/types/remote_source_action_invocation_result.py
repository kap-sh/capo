"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionInvocationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.account_id
    import capo_mgn.types.remote_source_action_id
    import capo_mgn.types.remote_source_action_invocation_status


class RemoteSourceActionInvocationResult(TypedDict, closed=True):
    remote_source_action_id: NotRequired[
        "capo_mgn.types.remote_source_action_id.RemoteSourceActionID"
    ]
    """<p>The unique identifier of the source action.</p>"""
    connector_owner_account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The ID of the account that owns the connector that ran the source action.</p>"""
    status: NotRequired[
        "capo_mgn.types.remote_source_action_invocation_status.RemoteSourceActionInvocationStatus"
    ]
    """<p>The status of the latest invocation.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the command started running.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the command finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionInvocationResult) -> dict:
    out: dict = {}
    if "remote_source_action_id" in value:
        out["remoteSourceActionID"] = value["remote_source_action_id"]
    if "connector_owner_account_id" in value:
        out["connectorOwnerAccountID"] = value["connector_owner_account_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "started_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["startedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["endedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    return out


def deserialize_json(data: dict) -> RemoteSourceActionInvocationResult:
    out: RemoteSourceActionInvocationResult = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionID") is not None:
        out["remote_source_action_id"] = data["remoteSourceActionID"]
    if data.get("connectorOwnerAccountID") is not None:
        out["connector_owner_account_id"] = data["connectorOwnerAccountID"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("startedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["started_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["ended_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    return out
