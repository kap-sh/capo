"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteSnapshotCopyConfigurationRequest``."""

from typing_extensions import TypedDict


class DeleteSnapshotCopyConfigurationRequest(TypedDict, closed=True):
    snapshot_copy_configuration_id: "str"
    """<p>The ID of the snapshot copy configuration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotCopyConfigurationRequest) -> dict:
    out: dict = {}
    out["snapshotCopyConfigurationId"] = value["snapshot_copy_configuration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotCopyConfigurationRequest:
    out: DeleteSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("snapshotCopyConfigurationId") is not None:
        out["snapshot_copy_configuration_id"] = data["snapshotCopyConfigurationId"]
    else:
        out["snapshot_copy_configuration_id"] = ""
    return out
