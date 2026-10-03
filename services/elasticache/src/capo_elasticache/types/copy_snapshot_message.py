"""Generated from Smithy shape ``com.amazonaws.elasticache#CopySnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CopySnapshotMessage(TypedDict, closed=True):
    source_snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of an existing snapshot from which to make a copy.</p>"""
    target_snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting. This value is stored as a lowercase string.</p>"""
    target_bucket: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.</p> <p>When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access">Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket</a> in the <i>Amazon ElastiCache User Guide</i>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html">Exporting a Snapshot</a> in the <i>Amazon ElastiCache User Guide</i>.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the target snapshot.</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CopySnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_snapshot_name" in value:
        pairs.append(
            (f"{key_prefix}SourceSnapshotName", str(value["source_snapshot_name"]))
        )
    if "target_snapshot_name" in value:
        pairs.append(
            (f"{key_prefix}TargetSnapshotName", str(value["target_snapshot_name"]))
        )
    if "target_bucket" in value:
        pairs.append((f"{key_prefix}TargetBucket", str(value["target_bucket"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CopySnapshotMessage:
    out: CopySnapshotMessage = {}  # type: ignore[typeddict-item]
    child_source_snapshot_name = el.find("SourceSnapshotName")
    if child_source_snapshot_name is not None:
        out["source_snapshot_name"] = str(child_source_snapshot_name.text or "")
    child_target_snapshot_name = el.find("TargetSnapshotName")
    if child_target_snapshot_name is not None:
        out["target_snapshot_name"] = str(child_target_snapshot_name.text or "")
    child_target_bucket = el.find("TargetBucket")
    if child_target_bucket is not None:
        out["target_bucket"] = str(child_target_bucket.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
