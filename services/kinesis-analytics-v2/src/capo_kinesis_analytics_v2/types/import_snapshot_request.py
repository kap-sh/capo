"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ImportSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.import_source_configuration
    import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration
    import capo_kinesis_analytics_v2.types.snapshot_format
    import capo_kinesis_analytics_v2.types.snapshot_v2_description
    import capo_kinesis_analytics_v2.types.snapshot_v2_name
    import capo_kinesis_analytics_v2.types.tags


class ImportSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot. The name must be unique among the snapshots in your account and Region. You can't reuse the name of an existing snapshot, including a snapshot in the <code>FAILED</code> status, until you delete that snapshot. Names that begin with <code>SYSTEMSNAPSHOT</code> are reserved.</p>"""
    import_source_configuration: "capo_kinesis_analytics_v2.types.import_source_configuration.ImportSourceConfiguration"
    """<p>Describes the location, IAM role, and encryption configuration of the savepoint data to import.</p>"""
    destination_encryption_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.SnapshotEncryptionConfiguration"
    ]
    """<p>The encryption configuration of the imported snapshot. If you don't specify this parameter, the snapshot is encrypted using a key of type <code>AWS_OWNED_KEY</code>. If you specify a KMS key, you must specify the key ARN.</p>"""
    snapshot_description: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_v2_description.SnapshotV2Description"
    ]
    """<p>A summary description of the snapshot.</p>"""
    snapshot_format: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_format.SnapshotFormat"
    ]
    """<p>The format of the snapshot being imported.</p>"""
    tags: NotRequired["capo_kinesis_analytics_v2.types.tags.Tags"]
    """<p>A list of one or more tags to assign to the snapshot. A tag is a key-value pair that identifies a snapshot. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    import capo_kinesis_analytics_v2.types.import_source_configuration

    out["ImportSourceConfiguration"] = (
        capo_kinesis_analytics_v2.types.import_source_configuration.serialize_aws_json_1_1(
            value["import_source_configuration"]
        )
    )
    if "destination_encryption_configuration" in value:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["DestinationEncryptionConfiguration"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.serialize_aws_json_1_1(
                value["destination_encryption_configuration"]
            )
        )
    if "snapshot_description" in value:
        out["SnapshotDescription"] = value["snapshot_description"]
    if "snapshot_format" in value:
        import capo_kinesis_analytics_v2.types.snapshot_format

        out["SnapshotFormat"] = (
            capo_kinesis_analytics_v2.types.snapshot_format.serialize_aws_json_1_1(
                value["snapshot_format"]
            )
        )
    if "tags" in value:
        import capo_kinesis_analytics_v2.types.tags

        out["Tags"] = capo_kinesis_analytics_v2.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSnapshotRequest:
    out: ImportSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("ImportSourceConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.import_source_configuration

        out["import_source_configuration"] = (
            capo_kinesis_analytics_v2.types.import_source_configuration.deserialize_aws_json_1_1(
                data["ImportSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ImportSnapshotRequest.import_source_configuration required"
        )
    if data.get("DestinationEncryptionConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["destination_encryption_configuration"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.deserialize_aws_json_1_1(
                data["DestinationEncryptionConfiguration"]
            )
        )
    if data.get("SnapshotDescription") is not None:
        out["snapshot_description"] = data["SnapshotDescription"]
    if data.get("SnapshotFormat") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_format

        out["snapshot_format"] = (
            capo_kinesis_analytics_v2.types.snapshot_format.deserialize_aws_json_1_1(
                data["SnapshotFormat"]
            )
        )
    if data.get("Tags") is not None:
        import capo_kinesis_analytics_v2.types.tags

        out["tags"] = capo_kinesis_analytics_v2.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
