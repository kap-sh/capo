"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ExportSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.export_destination_configuration
    import capo_kinesis_analytics_v2.types.snapshot_v2_name


class ExportSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot to export.</p>"""
    export_destination_configuration: "capo_kinesis_analytics_v2.types.export_destination_configuration.ExportDestinationConfiguration"
    """<p>Describes the location, IAM role, and encryption configuration of the export destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    import capo_kinesis_analytics_v2.types.export_destination_configuration

    out["ExportDestinationConfiguration"] = (
        capo_kinesis_analytics_v2.types.export_destination_configuration.serialize_aws_json_1_1(
            value["export_destination_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSnapshotRequest:
    out: ExportSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("ExportDestinationConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.export_destination_configuration

        out["export_destination_configuration"] = (
            capo_kinesis_analytics_v2.types.export_destination_configuration.deserialize_aws_json_1_1(
                data["ExportDestinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ExportSnapshotRequest.export_destination_configuration required"
        )
    return out
