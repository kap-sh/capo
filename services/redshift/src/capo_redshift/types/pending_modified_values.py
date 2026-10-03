"""Generated from Smithy shape ``com.amazonaws.redshift#PendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.integer_optional
    import capo_redshift.types.sensitive_string
    import capo_redshift.types.string


class PendingModifiedValues(TypedDict, closed=True):
    master_user_password: NotRequired[
        "capo_redshift.types.sensitive_string.SensitiveString"
    ]
    """<p>The pending or in-progress change of the admin user password for the cluster.</p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The pending or in-progress change of the cluster's node type.</p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The pending or in-progress change of the number of nodes in the cluster.</p>"""
    cluster_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The pending or in-progress change of the cluster type.</p>"""
    cluster_version: NotRequired["capo_redshift.types.string.String"]
    """<p>The pending or in-progress change of the service version.</p>"""
    automated_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The pending or in-progress change of the automated snapshot retention period.</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The pending or in-progress change of the new identifier for the cluster.</p>"""
    publicly_accessible: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>The pending or in-progress change of the ability to connect to the cluster from the public network.</p>"""
    enhanced_vpc_routing: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>"""
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the maintenance track that the cluster will change to during the next maintenance window.</p>"""
    encryption_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The encryption type for a cluster. Possible values are: KMS and None. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingModifiedValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "number_of_nodes" in value:
        pairs.append((f"{key_prefix}NumberOfNodes", str(value["number_of_nodes"])))
    if "cluster_type" in value:
        pairs.append((f"{key_prefix}ClusterType", str(value["cluster_type"])))
    if "cluster_version" in value:
        pairs.append((f"{key_prefix}ClusterVersion", str(value["cluster_version"])))
    if "automated_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}AutomatedSnapshotRetentionPeriod",
                str(value["automated_snapshot_retention_period"]),
            )
        )
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "enhanced_vpc_routing" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedVpcRouting",
                "true" if value["enhanced_vpc_routing"] else "false",
            )
        )
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{key_prefix}MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "encryption_type" in value:
        pairs.append((f"{key_prefix}EncryptionType", str(value["encryption_type"])))


def deserialize_query(el: Element) -> PendingModifiedValues:
    out: PendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
    child_cluster_type = el.find("ClusterType")
    if child_cluster_type is not None:
        out["cluster_type"] = str(child_cluster_type.text or "")
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_automated_snapshot_retention_period = el.find(
        "AutomatedSnapshotRetentionPeriod"
    )
    if child_automated_snapshot_retention_period is not None:
        out["automated_snapshot_retention_period"] = int(
            child_automated_snapshot_retention_period.text or ""
        )
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_enhanced_vpc_routing = el.find("EnhancedVpcRouting")
    if child_enhanced_vpc_routing is not None:
        out["enhanced_vpc_routing"] = (
            child_enhanced_vpc_routing.text or ""
        ).lower() == "true"
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_encryption_type = el.find("EncryptionType")
    if child_encryption_type is not None:
        out["encryption_type"] = str(child_encryption_type.text or "")
    return out
