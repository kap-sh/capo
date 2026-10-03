"""Generated from Smithy shape ``com.amazonaws.lightsail#CopySnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.region_name
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class CopySnapshotRequest(TypedDict, closed=True):
    source_snapshot_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the source manual snapshot to copy.</p> <p>Constraint:</p> <ul> <li> <p>Define this parameter only when copying a manual snapshot as another manual snapshot.</p> </li> </ul>"""
    source_resource_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the source instance or disk from which the source automatic snapshot was created.</p> <p>Constraint:</p> <ul> <li> <p>Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    restore_date: NotRequired["capo_lightsail.types.string.string"]
    """<p>The date of the source automatic snapshot to copy. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    use_latest_restorable_auto_snapshot: NotRequired[
        "capo_lightsail.types.boolean.boolean"
    ]
    """<p>A Boolean value to indicate whether to use the latest available automatic snapshot of the specified source instance or disk.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    target_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the new manual snapshot to be created as a copy.</p>"""
    source_region: "capo_lightsail.types.region_name.RegionName"
    """<p>The Amazon Web Services Region where the source manual or automatic snapshot is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopySnapshotRequest) -> dict:
    out: dict = {}
    if "source_snapshot_name" in value:
        out["sourceSnapshotName"] = value["source_snapshot_name"]
    if "source_resource_name" in value:
        out["sourceResourceName"] = value["source_resource_name"]
    if "restore_date" in value:
        out["restoreDate"] = value["restore_date"]
    if "use_latest_restorable_auto_snapshot" in value:
        out["useLatestRestorableAutoSnapshot"] = value[
            "use_latest_restorable_auto_snapshot"
        ]
    out["targetSnapshotName"] = value["target_snapshot_name"]
    import capo_lightsail.types.region_name

    out["sourceRegion"] = capo_lightsail.types.region_name.serialize_aws_json_1_1(
        value["source_region"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopySnapshotRequest:
    out: CopySnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceSnapshotName") is not None:
        out["source_snapshot_name"] = data["sourceSnapshotName"]
    if data.get("sourceResourceName") is not None:
        out["source_resource_name"] = data["sourceResourceName"]
    if data.get("restoreDate") is not None:
        out["restore_date"] = data["restoreDate"]
    if data.get("useLatestRestorableAutoSnapshot") is not None:
        out["use_latest_restorable_auto_snapshot"] = data[
            "useLatestRestorableAutoSnapshot"
        ]
    if data.get("targetSnapshotName") is not None:
        out["target_snapshot_name"] = data["targetSnapshotName"]
    else:
        raise DeserializationError("CopySnapshotRequest.target_snapshot_name required")
    if data.get("sourceRegion") is not None:
        import capo_lightsail.types.region_name

        out["source_region"] = (
            capo_lightsail.types.region_name.deserialize_aws_json_1_1(
                data["sourceRegion"]
            )
        )
    else:
        raise DeserializationError("CopySnapshotRequest.source_region required")
    return out
