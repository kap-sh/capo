"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PerObjectStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.per_object_sync_status
    import capo_network_firewall.types.update_token


class PerObjectStatus(TypedDict, closed=True):
    sync_status: NotRequired[
        "capo_network_firewall.types.per_object_sync_status.PerObjectSyncStatus"
    ]
    """<p>Indicates whether this object is in sync with the version indicated in the update token.</p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>The current version of the object that is either in sync or pending synchronization. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PerObjectStatus) -> dict:
    out: dict = {}
    if "sync_status" in value:
        import capo_network_firewall.types.per_object_sync_status

        out["SyncStatus"] = (
            capo_network_firewall.types.per_object_sync_status.serialize_aws_json_1_0(
                value["sync_status"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PerObjectStatus:
    out: PerObjectStatus = {}  # type: ignore[typeddict-item]
    if data.get("SyncStatus") is not None:
        import capo_network_firewall.types.per_object_sync_status

        out["sync_status"] = (
            capo_network_firewall.types.per_object_sync_status.deserialize_aws_json_1_0(
                data["SyncStatus"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PerObjectStatus) -> dict:
    out: dict = {}
    if "sync_status" in value:
        import capo_network_firewall.types.per_object_sync_status

        out["SyncStatus"] = (
            capo_network_firewall.types.per_object_sync_status.serialize_cbor(
                value["sync_status"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_cbor(data: dict) -> PerObjectStatus:
    out: PerObjectStatus = {}  # type: ignore[typeddict-item]
    if data.get("SyncStatus") is not None:
        import capo_network_firewall.types.per_object_sync_status

        out["sync_status"] = (
            capo_network_firewall.types.per_object_sync_status.deserialize_cbor(
                data["SyncStatus"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    return out
