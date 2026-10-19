"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace_name


class DeleteNamespaceRequest(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to delete.</p>"""
    final_snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot to be created before the namespace is deleted.</p>"""
    final_snapshot_retention_period: NotRequired["int"]
    """<p>How long to retain the final snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "final_snapshot_name" in value:
        out["finalSnapshotName"] = value["final_snapshot_name"]
    if "final_snapshot_retention_period" in value:
        out["finalSnapshotRetentionPeriod"] = value["final_snapshot_retention_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceRequest:
    out: DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("finalSnapshotName") is not None:
        out["final_snapshot_name"] = data["finalSnapshotName"]
    if data.get("finalSnapshotRetentionPeriod") is not None:
        out["final_snapshot_retention_period"] = data["finalSnapshotRetentionPeriod"]
    return out
