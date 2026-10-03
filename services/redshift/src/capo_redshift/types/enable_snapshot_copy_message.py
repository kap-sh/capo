"""Generated from Smithy shape ``com.amazonaws.redshift#EnableSnapshotCopyMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class EnableSnapshotCopyMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the source cluster to copy snapshots from.</p> <p>Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.</p>"""
    destination_region: NotRequired["capo_redshift.types.string.String"]
    """<p>The destination Amazon Web Services Region that you want to copy snapshots to.</p> <p>Constraints: Must be the name of a valid Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region">Regions and Endpoints</a> in the Amazon Web Services General Reference. </p>"""
    retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain automated snapshots in the destination region after they are copied from the source region.</p> <p>Default: 7.</p> <p>Constraints: Must be at least 1 and no more than 35.</p>"""
    snapshot_copy_grant_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the snapshot copy grant to use when snapshots of an Amazon Web Services KMS-encrypted cluster are copied to the destination region.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain newly copied snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableSnapshotCopyMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "destination_region" in value:
        pairs.append(
            (f"{key_prefix}DestinationRegion", str(value["destination_region"]))
        )
    if "retention_period" in value:
        pairs.append((f"{key_prefix}RetentionPeriod", str(value["retention_period"])))
    if "snapshot_copy_grant_name" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotCopyGrantName",
                str(value["snapshot_copy_grant_name"]),
            )
        )
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )


def deserialize_query(el: Element) -> EnableSnapshotCopyMessage:
    out: EnableSnapshotCopyMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_destination_region = el.find("DestinationRegion")
    if child_destination_region is not None:
        out["destination_region"] = str(child_destination_region.text or "")
    child_retention_period = el.find("RetentionPeriod")
    if child_retention_period is not None:
        out["retention_period"] = int(child_retention_period.text or "")
    child_snapshot_copy_grant_name = el.find("SnapshotCopyGrantName")
    if child_snapshot_copy_grant_name is not None:
        out["snapshot_copy_grant_name"] = str(child_snapshot_copy_grant_name.text or "")
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    return out
