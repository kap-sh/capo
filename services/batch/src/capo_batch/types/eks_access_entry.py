"""Generated from Smithy shape ``com.amazonaws.batch#EksAccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_access_entry_desired_state
    import capo_batch.types.eks_access_entry_status


class EksAccessEntry(TypedDict, closed=True):
    desired_state: NotRequired[
        "capo_batch.types.eks_access_entry_desired_state.EksAccessEntryDesiredState"
    ]
    """<p>The desired access entry state for the compute environment. Valid values:</p> <dl> <dt>ENABLED</dt> <dd> <p>Batch manages an access entry on the cluster for the compute environment.</p> </dd> <dt>DISABLED</dt> <dd> <p>Batch deletes the Batch-managed access entry for the cluster. This value is rejected if the cluster's <code>authenticationMode</code> is <code>API</code>, because such a cluster doesn't support the <code>aws-auth</code> ConfigMap.</p> </dd> <dt>INHERIT_FROM_CLUSTER</dt> <dd> <p>Batch defers to the cluster's current access entry <code>status</code>. On a cluster whose authentication mode is <code>API</code>, Batch creates and manages an access entry. On a cluster whose authentication mode is <code>API_AND_CONFIG_MAP</code> or <code>CONFIG_MAP</code>, Batch neither adds nor removes an access entry.</p> </dd> </dl>"""
    status: NotRequired["capo_batch.types.eks_access_entry_status.EksAccessEntryStatus"]
    """<p>The observed state of the access entry on the cluster. <code>ACTIVE</code> means that an access entry for the compute environment exists on the cluster and takes precedence over the <code>aws-auth</code> ConfigMap. <code>INACTIVE</code> means that no Batch-managed access entry is present. This is a read-only field returned by <code>DescribeComputeEnvironments</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksAccessEntry) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_batch.types.eks_access_entry_desired_state

        out["desiredState"] = (
            capo_batch.types.eks_access_entry_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "status" in value:
        import capo_batch.types.eks_access_entry_status

        out["status"] = capo_batch.types.eks_access_entry_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> EksAccessEntry:
    out: EksAccessEntry = {}  # type: ignore[typeddict-item]
    if data.get("desiredState") is not None:
        import capo_batch.types.eks_access_entry_desired_state

        out["desired_state"] = (
            capo_batch.types.eks_access_entry_desired_state.deserialize_json(
                data["desiredState"]
            )
        )
    if data.get("status") is not None:
        import capo_batch.types.eks_access_entry_status

        out["status"] = capo_batch.types.eks_access_entry_status.deserialize_json(
            data["status"]
        )
    return out
