"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSnapshotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object
    import capo_kinesis_analytics_v2.types.snapshot_mode


class ApplicationSnapshotConfiguration(TypedDict, closed=True):
    snapshots_enabled: "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    """<p>Describes whether snapshots are enabled for a Managed Service for Apache Flink application.</p>"""
    snapshot_mode: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_mode.SnapshotMode"
    ]
    """<p>Specifies the snapshot mode for a Managed Service for Apache Flink application. To use enhanced snapshots, specify <code>ENHANCED_SNAPSHOTS</code>. If you don't specify this parameter, the application uses <code>APPLICATION_SNAPSHOTS_LEGACY</code>. For more information, see <a href="https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html">Enhanced Snapshots</a>.</p> <p>To use <code>ENHANCED_SNAPSHOTS</code>, the application must use Apache Flink version 1.20 or later.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSnapshotConfiguration) -> dict:
    out: dict = {}
    out["SnapshotsEnabled"] = value["snapshots_enabled"]
    if "snapshot_mode" in value:
        import capo_kinesis_analytics_v2.types.snapshot_mode

        out["SnapshotMode"] = (
            capo_kinesis_analytics_v2.types.snapshot_mode.serialize_aws_json_1_1(
                value["snapshot_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSnapshotConfiguration:
    out: ApplicationSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotsEnabled") is not None:
        out["snapshots_enabled"] = data["SnapshotsEnabled"]
    else:
        out["snapshots_enabled"] = False
    if data.get("SnapshotMode") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_mode

        out["snapshot_mode"] = (
            capo_kinesis_analytics_v2.types.snapshot_mode.deserialize_aws_json_1_1(
                data["SnapshotMode"]
            )
        )
    return out
