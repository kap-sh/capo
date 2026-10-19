"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CreateApplicationSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.snapshot_name


class CreateApplicationSnapshotRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of an existing application</p>"""
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    """<p>An identifier for the application snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationSnapshotRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationSnapshotRequest:
    out: CreateApplicationSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    return out
