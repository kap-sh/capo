"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextStoreSyncState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.context_store_sync_status
    import capo_network_firewall.types.status_message


class ContextStoreSyncState(TypedDict, closed=True):
    sync_status: NotRequired[
        "capo_network_firewall.types.context_store_sync_status.ContextStoreSyncStatus"
    ]
    """<p>The synchronization status of the firewall's context sets. Valid values:</p> <ul> <li> <p> <code>SYNCING</code> - The firewall is applying the latest context store data.</p> </li> <li> <p> <code>FULLY_RESOLVED</code> - All resource identifiers in the firewall's context sets resolve to resources in the context store.</p> </li> <li> <p> <code>PARTIALLY_RESOLVED</code> - Some resource identifiers in the firewall's context sets don't resolve to resources in the context store.</p> </li> <li> <p> <code>SYNC_FAILED</code> - The firewall couldn't sync with the context store. For details, see <code>StatusMessage</code>.</p> </li> </ul>"""
    status_message: NotRequired[
        "capo_network_firewall.types.status_message.StatusMessage"
    ]
    """<p>A message that provides additional information about the synchronization status, particularly when the status is not <code>FULLY_RESOLVED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextStoreSyncState) -> dict:
    out: dict = {}
    if "sync_status" in value:
        import capo_network_firewall.types.context_store_sync_status

        out["SyncStatus"] = (
            capo_network_firewall.types.context_store_sync_status.serialize_aws_json_1_0(
                value["sync_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextStoreSyncState:
    out: ContextStoreSyncState = {}  # type: ignore[typeddict-item]
    if data.get("SyncStatus") is not None:
        import capo_network_firewall.types.context_store_sync_status

        out["sync_status"] = (
            capo_network_firewall.types.context_store_sync_status.deserialize_aws_json_1_0(
                data["SyncStatus"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContextStoreSyncState) -> dict:
    out: dict = {}
    if "sync_status" in value:
        import capo_network_firewall.types.context_store_sync_status

        out["SyncStatus"] = (
            capo_network_firewall.types.context_store_sync_status.serialize_cbor(
                value["sync_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_cbor(data: dict) -> ContextStoreSyncState:
    out: ContextStoreSyncState = {}  # type: ignore[typeddict-item]
    if data.get("SyncStatus") is not None:
        import capo_network_firewall.types.context_store_sync_status

        out["sync_status"] = (
            capo_network_firewall.types.context_store_sync_status.deserialize_cbor(
                data["SyncStatus"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
