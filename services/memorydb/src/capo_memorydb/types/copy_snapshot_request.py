"""Generated from Smithy shape ``com.amazonaws.memorydb#CopySnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_memorydb.types.kms_key_id
    import capo_memorydb.types.string
    import capo_memorydb.types.tag_list
    import capo_memorydb.types.target_bucket


class CopySnapshotRequest(TypedDict, closed=True):
    source_snapshot_name: "capo_memorydb.types.string.String"
    """<p>The name of an existing snapshot from which to make a copy.</p>"""
    target_snapshot_name: "capo_memorydb.types.string.String"
    """<p>A name for the snapshot copy. MemoryDB does not permit overwriting a snapshot, therefore this name must be unique within its context - MemoryDB or an Amazon S3 bucket if exporting.</p>"""
    target_bucket: NotRequired["capo_memorydb.types.target_bucket.TargetBucket"]
    """<p>The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access. When using this parameter to export a snapshot, be sure MemoryDB has the needed permissions to this S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/snapshots-exporting.html">Step 2: Grant MemoryDB Access to Your Amazon S3 Bucket</a>. </p>"""
    kms_key_id: NotRequired["capo_memorydb.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the KMS key used to encrypt the target snapshot.</p>"""
    tags: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopySnapshotRequest) -> dict:
    out: dict = {}
    out["SourceSnapshotName"] = value["source_snapshot_name"]
    out["TargetSnapshotName"] = value["target_snapshot_name"]
    if "target_bucket" in value:
        out["TargetBucket"] = value["target_bucket"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_memorydb.types.tag_list

        out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CopySnapshotRequest:
    out: CopySnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceSnapshotName") is not None:
        out["source_snapshot_name"] = data["SourceSnapshotName"]
    else:
        raise DeserializationError("CopySnapshotRequest.source_snapshot_name required")
    if data.get("TargetSnapshotName") is not None:
        out["target_snapshot_name"] = data["TargetSnapshotName"]
    else:
        raise DeserializationError("CopySnapshotRequest.target_snapshot_name required")
    if data.get("TargetBucket") is not None:
        out["target_bucket"] = data["TargetBucket"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
