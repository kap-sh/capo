"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.snapshot_v2_description
    import capo_kinesis_analytics_v2.types.snapshot_v2_name
    import capo_kinesis_analytics_v2.types.tags


class CreateSnapshotRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot. The name must be unique among the snapshots in your account and Region. You can't reuse the name of an existing snapshot, including a snapshot in the <code>FAILED</code> status, until you delete that snapshot. Names that begin with <code>SYSTEMSNAPSHOT</code> are reserved.</p>"""
    snapshot_description: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_v2_description.SnapshotV2Description"
    ]
    """<p>A summary description of the snapshot.</p>"""
    tags: NotRequired["capo_kinesis_analytics_v2.types.tags.Tags"]
    """<p>A list of one or more tags to assign to the snapshot. A tag is a key-value pair that identifies a snapshot. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["SnapshotName"] = value["snapshot_name"]
    if "snapshot_description" in value:
        out["SnapshotDescription"] = value["snapshot_description"]
    if "tags" in value:
        import capo_kinesis_analytics_v2.types.tags

        out["Tags"] = capo_kinesis_analytics_v2.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotRequest:
    out: CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("SnapshotDescription") is not None:
        out["snapshot_description"] = data["SnapshotDescription"]
    if data.get("Tags") is not None:
        import capo_kinesis_analytics_v2.types.tags

        out["tags"] = capo_kinesis_analytics_v2.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
