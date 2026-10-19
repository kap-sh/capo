"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSnapshotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object


class ApplicationSnapshotConfiguration(TypedDict, closed=True):
    snapshots_enabled: "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    """<p>Describes whether snapshots are enabled for a Managed Service for Apache Flink application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSnapshotConfiguration) -> dict:
    out: dict = {}
    out["SnapshotsEnabled"] = value["snapshots_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSnapshotConfiguration:
    out: ApplicationSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotsEnabled") is not None:
        out["snapshots_enabled"] = data["SnapshotsEnabled"]
    else:
        out["snapshots_enabled"] = False
    return out
