"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterPendingUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.ac_ls_update_status
    import capo_memorydb.types.pending_modified_service_update_list
    import capo_memorydb.types.resharding_status


class ClusterPendingUpdates(TypedDict, closed=True):
    resharding: NotRequired["capo_memorydb.types.resharding_status.ReshardingStatus"]
    """<p>The status of an online resharding operation.</p>"""
    ac_ls: NotRequired["capo_memorydb.types.ac_ls_update_status.ACLsUpdateStatus"]
    """<p>A list of ACLs associated with the cluster that are being updated</p>"""
    service_updates: NotRequired[
        "capo_memorydb.types.pending_modified_service_update_list.PendingModifiedServiceUpdateList"
    ]
    """<p>A list of service updates being applied to the cluster</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterPendingUpdates) -> dict:
    out: dict = {}
    if "resharding" in value:
        import capo_memorydb.types.resharding_status

        out["Resharding"] = (
            capo_memorydb.types.resharding_status.serialize_aws_json_1_1(
                value["resharding"]
            )
        )
    if "ac_ls" in value:
        import capo_memorydb.types.ac_ls_update_status

        out["ACLs"] = capo_memorydb.types.ac_ls_update_status.serialize_aws_json_1_1(
            value["ac_ls"]
        )
    if "service_updates" in value:
        import capo_memorydb.types.pending_modified_service_update_list

        out["ServiceUpdates"] = (
            capo_memorydb.types.pending_modified_service_update_list.serialize_aws_json_1_1(
                value["service_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterPendingUpdates:
    out: ClusterPendingUpdates = {}  # type: ignore[typeddict-item]
    if data.get("Resharding") is not None:
        import capo_memorydb.types.resharding_status

        out["resharding"] = (
            capo_memorydb.types.resharding_status.deserialize_aws_json_1_1(
                data["Resharding"]
            )
        )
    if data.get("ACLs") is not None:
        import capo_memorydb.types.ac_ls_update_status

        out["ac_ls"] = capo_memorydb.types.ac_ls_update_status.deserialize_aws_json_1_1(
            data["ACLs"]
        )
    if data.get("ServiceUpdates") is not None:
        import capo_memorydb.types.pending_modified_service_update_list

        out["service_updates"] = (
            capo_memorydb.types.pending_modified_service_update_list.deserialize_aws_json_1_1(
                data["ServiceUpdates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusterPendingUpdates) -> dict:
    out: dict = {}
    if "resharding" in value:
        import capo_memorydb.types.resharding_status

        out["Resharding"] = capo_memorydb.types.resharding_status.serialize_cbor(
            value["resharding"]
        )
    if "ac_ls" in value:
        import capo_memorydb.types.ac_ls_update_status

        out["ACLs"] = capo_memorydb.types.ac_ls_update_status.serialize_cbor(
            value["ac_ls"]
        )
    if "service_updates" in value:
        import capo_memorydb.types.pending_modified_service_update_list

        out["ServiceUpdates"] = (
            capo_memorydb.types.pending_modified_service_update_list.serialize_cbor(
                value["service_updates"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ClusterPendingUpdates:
    out: ClusterPendingUpdates = {}  # type: ignore[typeddict-item]
    if data.get("Resharding") is not None:
        import capo_memorydb.types.resharding_status

        out["resharding"] = capo_memorydb.types.resharding_status.deserialize_cbor(
            data["Resharding"]
        )
    if data.get("ACLs") is not None:
        import capo_memorydb.types.ac_ls_update_status

        out["ac_ls"] = capo_memorydb.types.ac_ls_update_status.deserialize_cbor(
            data["ACLs"]
        )
    if data.get("ServiceUpdates") is not None:
        import capo_memorydb.types.pending_modified_service_update_list

        out["service_updates"] = (
            capo_memorydb.types.pending_modified_service_update_list.deserialize_cbor(
                data["ServiceUpdates"]
            )
        )
    return out
