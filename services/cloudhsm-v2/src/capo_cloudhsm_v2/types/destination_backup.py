"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DestinationBackup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_id
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.region
    import capo_cloudhsm_v2.types.timestamp


class DestinationBackup(TypedDict, closed=True):
    create_timestamp: NotRequired["capo_cloudhsm_v2.types.timestamp.Timestamp"]
    """<p>The date and time when both the source backup was created.</p>"""
    source_region: NotRequired["capo_cloudhsm_v2.types.region.Region"]
    """<p>The AWS region that contains the source backup from which the new backup was copied.</p>"""
    source_backup: NotRequired["capo_cloudhsm_v2.types.backup_id.BackupId"]
    """<p>The identifier (ID) of the source backup from which the new backup was copied.</p>"""
    source_cluster: NotRequired["capo_cloudhsm_v2.types.cluster_id.ClusterId"]
    """<p>The identifier (ID) of the cluster containing the source backup from which the new backup was copied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationBackup) -> dict:
    out: dict = {}
    if "create_timestamp" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["CreateTimestamp"] = (
            capo_cloudhsm_v2.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "source_region" in value:
        out["SourceRegion"] = value["source_region"]
    if "source_backup" in value:
        out["SourceBackup"] = value["source_backup"]
    if "source_cluster" in value:
        out["SourceCluster"] = value["source_cluster"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationBackup:
    out: DestinationBackup = {}  # type: ignore[typeddict-item]
    if data.get("CreateTimestamp") is not None:
        import capo_cloudhsm_v2.types.timestamp

        out["create_timestamp"] = (
            capo_cloudhsm_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if data.get("SourceRegion") is not None:
        out["source_region"] = data["SourceRegion"]
    if data.get("SourceBackup") is not None:
        out["source_backup"] = data["SourceBackup"]
    if data.get("SourceCluster") is not None:
        out["source_cluster"] = data["SourceCluster"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DestinationBackup) -> dict:
    out: dict = {}
    if "create_timestamp" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["CreateTimestamp"] = capo_cloudhsm_v2.types.timestamp.serialize_cbor(
            value["create_timestamp"]
        )
    if "source_region" in value:
        out["SourceRegion"] = value["source_region"]
    if "source_backup" in value:
        out["SourceBackup"] = value["source_backup"]
    if "source_cluster" in value:
        out["SourceCluster"] = value["source_cluster"]
    return out


def deserialize_cbor(data: dict) -> DestinationBackup:
    out: DestinationBackup = {}  # type: ignore[typeddict-item]
    if data.get("CreateTimestamp") is not None:
        import capo_cloudhsm_v2.types.timestamp

        out["create_timestamp"] = capo_cloudhsm_v2.types.timestamp.deserialize_cbor(
            data["CreateTimestamp"]
        )
    if data.get("SourceRegion") is not None:
        out["source_region"] = data["SourceRegion"]
    if data.get("SourceBackup") is not None:
        out["source_backup"] = data["SourceBackup"]
    if data.get("SourceCluster") is not None:
        out["source_cluster"] = data["SourceCluster"]
    return out
