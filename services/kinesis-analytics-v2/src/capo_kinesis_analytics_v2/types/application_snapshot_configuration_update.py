"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSnapshotConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object


class ApplicationSnapshotConfigurationUpdate(TypedDict, closed=True):
    snapshots_enabled_update: (
        "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    )
    """<p>Describes updates to whether snapshots are enabled for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSnapshotConfigurationUpdate) -> dict:
    out: dict = {}
    out["SnapshotsEnabledUpdate"] = value["snapshots_enabled_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSnapshotConfigurationUpdate:
    out: ApplicationSnapshotConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotsEnabledUpdate") is not None:
        out["snapshots_enabled_update"] = data["SnapshotsEnabledUpdate"]
    else:
        out["snapshots_enabled_update"] = False
    return out
