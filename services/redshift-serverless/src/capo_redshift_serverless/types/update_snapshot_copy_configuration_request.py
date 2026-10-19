"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateSnapshotCopyConfigurationRequest``."""

from typing_extensions import NotRequired, TypedDict


class UpdateSnapshotCopyConfigurationRequest(TypedDict, closed=True):
    snapshot_copy_configuration_id: "str"
    """<p>The ID of the snapshot copy configuration to update.</p>"""
    snapshot_retention_period: NotRequired["int"]
    """<p>The new retention period of how long to keep a snapshot in the destination Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotCopyConfigurationRequest) -> dict:
    out: dict = {}
    out["snapshotCopyConfigurationId"] = value["snapshot_copy_configuration_id"]
    if "snapshot_retention_period" in value:
        out["snapshotRetentionPeriod"] = value["snapshot_retention_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotCopyConfigurationRequest:
    out: UpdateSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("snapshotCopyConfigurationId") is not None:
        out["snapshot_copy_configuration_id"] = data["snapshotCopyConfigurationId"]
    else:
        out["snapshot_copy_configuration_id"] = ""
    if data.get("snapshotRetentionPeriod") is not None:
        out["snapshot_retention_period"] = data["snapshotRetentionPeriod"]
    return out
