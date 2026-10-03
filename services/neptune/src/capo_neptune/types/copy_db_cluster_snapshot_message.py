"""Generated from Smithy shape ``com.amazonaws.neptune#CopyDBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.string
    import capo_neptune.types.tag_list


class CopyDBClusterSnapshotMessage(TypedDict, closed=True):
    source_db_cluster_snapshot_identifier: NotRequired[
        "capo_neptune.types.string.String"
    ]
    """<p>The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive. If the source DB cluster snapshot is in a different region or owned by another account, specify the snapshot ARN.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid system snapshot in the "available" state.</p> </li> <li> <p>Specify a valid DB snapshot identifier.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>"""
    target_db_cluster_snapshot_identifier: NotRequired[
        "capo_neptune.types.string.String"
    ]
    """<p>The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot2</code> </p>"""
    kms_key_id: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.</p> <p>If you copy an encrypted DB cluster snapshot from your Amazon account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new KMS encryption key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.</p> <p>If you copy an encrypted DB cluster snapshot that is shared from another Amazon account, then you must specify a value for <code>KmsKeyId</code>.</p> <p> KMS encryption keys are specific to the Amazon Region that they are created in, and you can't use encryption keys from one Amazon Region in another Amazon Region.</p> <p>You cannot encrypt an unencrypted DB cluster snapshot when you copy it. If you try to copy an unencrypted DB cluster snapshot and specify a value for the KmsKeyId parameter, an error is returned.</p>"""
    pre_signed_url: NotRequired["capo_neptune.types.string.String"]
    """<p>Not currently supported.</p>"""
    copy_tags: NotRequired["capo_neptune.types.boolean_optional.BooleanOptional"]
    """<p>True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.</p>"""
    tags: NotRequired["capo_neptune.types.tag_list.TagList"]
    """<p>The tags to assign to the new DB cluster snapshot copy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterSnapshotIdentifier",
                str(value["source_db_cluster_snapshot_identifier"]),
            )
        )
    if "target_db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBClusterSnapshotIdentifier",
                str(value["target_db_cluster_snapshot_identifier"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "pre_signed_url" in value:
        pairs.append((f"{key_prefix}PreSignedUrl", str(value["pre_signed_url"])))
    if "copy_tags" in value:
        pairs.append(
            (f"{key_prefix}CopyTags", "true" if value["copy_tags"] else "false")
        )
    if "tags" in value:
        import capo_neptune.types.tag_list

        capo_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CopyDBClusterSnapshotMessage:
    out: CopyDBClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_source_db_cluster_snapshot_identifier = el.find(
        "SourceDBClusterSnapshotIdentifier"
    )
    if child_source_db_cluster_snapshot_identifier is not None:
        out["source_db_cluster_snapshot_identifier"] = str(
            child_source_db_cluster_snapshot_identifier.text or ""
        )
    child_target_db_cluster_snapshot_identifier = el.find(
        "TargetDBClusterSnapshotIdentifier"
    )
    if child_target_db_cluster_snapshot_identifier is not None:
        out["target_db_cluster_snapshot_identifier"] = str(
            child_target_db_cluster_snapshot_identifier.text or ""
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_pre_signed_url = el.find("PreSignedUrl")
    if child_pre_signed_url is not None:
        out["pre_signed_url"] = str(child_pre_signed_url.text or "")
    child_copy_tags = el.find("CopyTags")
    if child_copy_tags is not None:
        out["copy_tags"] = (child_copy_tags.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_neptune.types.tag_list

        out["tags"] = capo_neptune.types.tag_list.deserialize_query(child_tags)
    return out
