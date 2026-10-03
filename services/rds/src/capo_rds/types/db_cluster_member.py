"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DBClusterMember(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the instance identifier for this member of the DB cluster.</p>"""
    is_cluster_writer: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the cluster member is the primary DB instance for the DB cluster.</p>"""
    db_cluster_parameter_group_status: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the status of the DB cluster parameter group for this member of the DB cluster.</p>"""
    promotion_tier: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance"> Fault Tolerance for an Aurora DB Cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "is_cluster_writer" in value:
        pairs.append(
            (
                f"{key_prefix}IsClusterWriter",
                "true" if value["is_cluster_writer"] else "false",
            )
        )
    if "db_cluster_parameter_group_status" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupStatus",
                str(value["db_cluster_parameter_group_status"]),
            )
        )
    if "promotion_tier" in value:
        pairs.append((f"{key_prefix}PromotionTier", str(value["promotion_tier"])))


def deserialize_query(el: Element) -> DBClusterMember:
    out: DBClusterMember = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_is_cluster_writer = el.find("IsClusterWriter")
    if child_is_cluster_writer is not None:
        out["is_cluster_writer"] = (
            child_is_cluster_writer.text or ""
        ).lower() == "true"
    child_db_cluster_parameter_group_status = el.find("DBClusterParameterGroupStatus")
    if child_db_cluster_parameter_group_status is not None:
        out["db_cluster_parameter_group_status"] = str(
            child_db_cluster_parameter_group_status.text or ""
        )
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    return out
