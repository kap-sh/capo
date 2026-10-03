"""Generated from Smithy shape ``com.amazonaws.rds#CopyDBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CopyDBClusterSnapshotMessage(TypedDict, closed=True):
    source_db_cluster_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the DB cluster snapshot to copy. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid source snapshot in the "available" state.</p> </li> <li> <p>If the source snapshot is in the same Amazon Web Services Region as the copy, specify a valid DB snapshot identifier.</p> </li> <li> <p>If the source snapshot is in a different Amazon Web Services Region than the copy, specify a valid DB cluster snapshot ARN. You can also specify an ARN of a snapshot that is in a different account and a different Amazon Web Services Region. For more information, go to <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html#USER_CopySnapshot.AcrossRegions"> Copying Snapshots Across Amazon Web Services Regions</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>"""
    target_db_cluster_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot2</code> </p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted DB cluster snapshot. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the Amazon Web Services KMS key.</p> <p>If you copy an encrypted DB cluster snapshot from your Amazon Web Services account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new KMS key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.</p> <p>If you copy an encrypted DB cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for <code>KmsKeyId</code>.</p> <p>To copy an encrypted DB cluster snapshot to another Amazon Web Services Region, you must set <code>KmsKeyId</code> to the Amazon Web Services KMS key identifier you want to use to encrypt the copy of the DB cluster snapshot in the destination Amazon Web Services Region. KMS keys are specific to the Amazon Web Services Region that they are created in, and you can't use KMS keys from one Amazon Web Services Region in another Amazon Web Services Region.</p> <p>If you copy an unencrypted DB cluster snapshot and specify a value for the <code>KmsKeyId</code> parameter, an error is returned.</p>"""
    pre_signed_url: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>When you are copying a DB cluster snapshot from one Amazon Web Services GovCloud (US) Region to another, the URL that contains a Signature Version 4 signed request for the <code>CopyDBClusterSnapshot</code> API operation in the Amazon Web Services Region that contains the source DB cluster snapshot to copy. Use the <code>PreSignedUrl</code> parameter when copying an encrypted DB cluster snapshot from another Amazon Web Services Region. Don't specify <code>PreSignedUrl</code> when copying an encrypted DB cluster snapshot in the same Amazon Web Services Region.</p> <p>This setting applies only to Amazon Web Services GovCloud (US) Regions. It's ignored in other Amazon Web Services Regions.</p> <p>The presigned URL must be a valid request for the <code>CopyDBClusterSnapshot</code> API operation that can run in the source Amazon Web Services Region that contains the encrypted DB cluster snapshot to copy. The presigned URL request must contain the following parameter values:</p> <ul> <li> <p> <code>KmsKeyId</code> - The KMS key identifier for the KMS key to use to encrypt the copy of the DB cluster snapshot in the destination Amazon Web Services Region. This is the same identifier for both the <code>CopyDBClusterSnapshot</code> operation that is called in the destination Amazon Web Services Region, and the operation contained in the presigned URL.</p> </li> <li> <p> <code>DestinationRegion</code> - The name of the Amazon Web Services Region that the DB cluster snapshot is to be created in.</p> </li> <li> <p> <code>SourceDBClusterSnapshotIdentifier</code> - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 Amazon Web Services Region, then your <code>SourceDBClusterSnapshotIdentifier</code> looks like the following example: <code>arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115</code>.</p> </li> </ul> <p>To learn how to generate a Signature Version 4 signed request, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html"> Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"> Signature Version 4 Signing Process</a>.</p> <note> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.</p> </note>"""
    copy_tags: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot. By default, tags are not copied.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]


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
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
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
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
