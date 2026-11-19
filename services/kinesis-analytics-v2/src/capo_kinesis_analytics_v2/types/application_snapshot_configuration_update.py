"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSnapshotConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object
    import capo_kinesis_analytics_v2.types.snapshot_mode


class ApplicationSnapshotConfigurationUpdate(TypedDict, closed=True):
    snapshots_enabled_update: (
        "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    )
    """<p>Describes updates to whether snapshots are enabled for an application.</p>"""
    snapshot_mode_update: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_mode.SnapshotMode"
    ]
    """<p>Describes updates to the snapshot mode of a Managed Service for Apache Flink application. You can update the snapshot mode from <code>APPLICATION_SNAPSHOTS_LEGACY</code> to <code>ENHANCED_SNAPSHOTS</code>. You can't use <code>UpdateApplication</code> to change the snapshot mode back to <code>APPLICATION_SNAPSHOTS_LEGACY</code>.</p> <p>To return to <code>APPLICATION_SNAPSHOTS_LEGACY</code>, use <code>RollbackApplication</code>. After you update an application that uses <code>ENHANCED_SNAPSHOTS</code>, you can't roll it back to <code>APPLICATION_SNAPSHOTS_LEGACY</code>.</p> <p>To use <code>ENHANCED_SNAPSHOTS</code>, the application must use Apache Flink version 1.20 or later.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSnapshotConfigurationUpdate) -> dict:
    out: dict = {}
    out["SnapshotsEnabledUpdate"] = value["snapshots_enabled_update"]
    if "snapshot_mode_update" in value:
        import capo_kinesis_analytics_v2.types.snapshot_mode

        out["SnapshotModeUpdate"] = (
            capo_kinesis_analytics_v2.types.snapshot_mode.serialize_aws_json_1_1(
                value["snapshot_mode_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSnapshotConfigurationUpdate:
    out: ApplicationSnapshotConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotsEnabledUpdate") is not None:
        out["snapshots_enabled_update"] = data["SnapshotsEnabledUpdate"]
    else:
        out["snapshots_enabled_update"] = False
    if data.get("SnapshotModeUpdate") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_mode

        out["snapshot_mode_update"] = (
            capo_kinesis_analytics_v2.types.snapshot_mode.deserialize_aws_json_1_1(
                data["SnapshotModeUpdate"]
            )
        )
    return out
