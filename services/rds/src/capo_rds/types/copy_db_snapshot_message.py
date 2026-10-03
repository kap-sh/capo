"""Generated from Smithy shape ``com.amazonaws.rds#CopyDBSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CopyDBSnapshotMessage(TypedDict, closed=True):
    source_db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the source DB snapshot.</p> <p>If the source snapshot is in the same Amazon Web Services Region as the copy, specify a valid DB snapshot identifier. For example, you might specify <code>rds:mysql-instance1-snapshot-20130805</code>.</p> <p>If you are copying from a shared manual DB snapshot, this parameter must be the Amazon Resource Name (ARN) of the shared DB snapshot.</p> <p>If the source snapshot is in a different Amazon Web Services Region than the copy, specify a valid DB snapshot ARN. You can also specify an ARN of a snapshot that is in a different account and a different Amazon Web Services Region. For example, you might specify <code>arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid source snapshot in the "available" state.</p> </li> </ul> <p>Example: <code>rds:mydb-2012-04-02-00-01</code> </p> <p>Example: <code>arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805</code> </p>"""
    target_db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the copy of the snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Can't be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-db-snapshot</code> </p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted DB snapshot. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you copy an encrypted DB snapshot from your Amazon Web Services account, you can specify a value for this parameter to encrypt the copy with a new KMS key. If you don't specify a value for this parameter, then the copy of the DB snapshot is encrypted with the same Amazon Web Services KMS key as the source DB snapshot.</p> <p>If you copy an encrypted DB snapshot that is shared from another Amazon Web Services account, then you must specify a value for this parameter.</p> <p>If you specify this parameter when you copy an unencrypted snapshot, the copy is encrypted.</p> <p>If you copy an encrypted snapshot to a different Amazon Web Services Region, then you must specify an Amazon Web Services KMS key identifier for the destination Amazon Web Services Region. KMS keys are specific to the Amazon Web Services Region that they are created in, and you can't use KMS keys from one Amazon Web Services Region in another Amazon Web Services Region.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    copy_tags: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to copy all tags from the source DB snapshot to the target DB snapshot. By default, tags aren't copied.</p>"""
    pre_signed_url: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>When you are copying a snapshot from one Amazon Web Services GovCloud (US) Region to another, the URL that contains a Signature Version 4 signed request for the <code>CopyDBSnapshot</code> API operation in the source Amazon Web Services Region that contains the source DB snapshot to copy.</p> <p>This setting applies only to Amazon Web Services GovCloud (US) Regions. It's ignored in other Amazon Web Services Regions.</p> <p>You must specify this parameter when you copy an encrypted DB snapshot from another Amazon Web Services Region by using the Amazon RDS API. Don't specify <code>PreSignedUrl</code> when you are copying an encrypted DB snapshot in the same Amazon Web Services Region.</p> <p>The presigned URL must be a valid request for the <code>CopyDBClusterSnapshot</code> API operation that can run in the source Amazon Web Services Region that contains the encrypted DB cluster snapshot to copy. The presigned URL request must contain the following parameter values:</p> <ul> <li> <p> <code>DestinationRegion</code> - The Amazon Web Services Region that the encrypted DB snapshot is copied to. This Amazon Web Services Region is the same one where the <code>CopyDBSnapshot</code> operation is called that contains this presigned URL.</p> <p>For example, if you copy an encrypted DB snapshot from the us-west-2 Amazon Web Services Region to the us-east-1 Amazon Web Services Region, then you call the <code>CopyDBSnapshot</code> operation in the us-east-1 Amazon Web Services Region and provide a presigned URL that contains a call to the <code>CopyDBSnapshot</code> operation in the us-west-2 Amazon Web Services Region. For this example, the <code>DestinationRegion</code> in the presigned URL must be set to the us-east-1 Amazon Web Services Region.</p> </li> <li> <p> <code>KmsKeyId</code> - The KMS key identifier for the KMS key to use to encrypt the copy of the DB snapshot in the destination Amazon Web Services Region. This is the same identifier for both the <code>CopyDBSnapshot</code> operation that is called in the destination Amazon Web Services Region, and the operation contained in the presigned URL.</p> </li> <li> <p> <code>SourceDBSnapshotIdentifier</code> - The DB snapshot identifier for the encrypted snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted DB snapshot from the us-west-2 Amazon Web Services Region, then your <code>SourceDBSnapshotIdentifier</code> looks like the following example: <code>arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20161115</code>.</p> </li> </ul> <p>To learn how to generate a Signature Version 4 signed request, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html">Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 Signing Process</a>.</p> <note> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.</p> </note>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of an option group to associate with the copy of the snapshot.</p> <p>Specify this option if you are copying a snapshot from one Amazon Web Services Region to another, and your DB instance uses a nondefault option group. If your source DB instance uses Transparent Data Encryption for Oracle or Microsoft SQL Server, you must specify this option when copying across Amazon Web Services Regions. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopySnapshot.Options">Option group considerations</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    target_custom_availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The external custom Availability Zone (CAZ) identifier for the target CAZ.</p> <p>Example: <code>rds-caz-aiqhTgQv</code>.</p>"""
    snapshot_target: NotRequired["capo_rds.types.string.String"]
    """<p>Configures the location where RDS will store copied snapshots.</p> <p>Valid Values:</p> <ul> <li> <p> <code>local</code> (Dedicated Local Zone)</p> </li> <li> <p> <code>outposts</code> (Amazon Web Services Outposts)</p> </li> <li> <p> <code>region</code> (Amazon Web Services Region)</p> </li> </ul>"""
    copy_option_group: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to copy the DB option group associated with the source DB snapshot to the target Amazon Web Services account and associate with the target DB snapshot. The associated option group can be copied only with cross-account snapshot copy calls.</p>"""
    snapshot_availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the Availability Zone where RDS stores the DB snapshot. This value is valid only for snapshots that RDS stores on a Dedicated Local Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBSnapshotIdentifier",
                str(value["source_db_snapshot_identifier"]),
            )
        )
    if "target_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBSnapshotIdentifier",
                str(value["target_db_snapshot_identifier"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "copy_tags" in value:
        pairs.append(
            (f"{key_prefix}CopyTags", "true" if value["copy_tags"] else "false")
        )
    if "pre_signed_url" in value:
        pairs.append((f"{key_prefix}PreSignedUrl", str(value["pre_signed_url"])))
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "target_custom_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}TargetCustomAvailabilityZone",
                str(value["target_custom_availability_zone"]),
            )
        )
    if "snapshot_target" in value:
        pairs.append((f"{key_prefix}SnapshotTarget", str(value["snapshot_target"])))
    if "copy_option_group" in value:
        pairs.append(
            (
                f"{key_prefix}CopyOptionGroup",
                "true" if value["copy_option_group"] else "false",
            )
        )
    if "snapshot_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotAvailabilityZone",
                str(value["snapshot_availability_zone"]),
            )
        )


def deserialize_query(el: Element) -> CopyDBSnapshotMessage:
    out: CopyDBSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_source_db_snapshot_identifier = el.find("SourceDBSnapshotIdentifier")
    if child_source_db_snapshot_identifier is not None:
        out["source_db_snapshot_identifier"] = str(
            child_source_db_snapshot_identifier.text or ""
        )
    child_target_db_snapshot_identifier = el.find("TargetDBSnapshotIdentifier")
    if child_target_db_snapshot_identifier is not None:
        out["target_db_snapshot_identifier"] = str(
            child_target_db_snapshot_identifier.text or ""
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_copy_tags = el.find("CopyTags")
    if child_copy_tags is not None:
        out["copy_tags"] = (child_copy_tags.text or "").lower() == "true"
    child_pre_signed_url = el.find("PreSignedUrl")
    if child_pre_signed_url is not None:
        out["pre_signed_url"] = str(child_pre_signed_url.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_target_custom_availability_zone = el.find("TargetCustomAvailabilityZone")
    if child_target_custom_availability_zone is not None:
        out["target_custom_availability_zone"] = str(
            child_target_custom_availability_zone.text or ""
        )
    child_snapshot_target = el.find("SnapshotTarget")
    if child_snapshot_target is not None:
        out["snapshot_target"] = str(child_snapshot_target.text or "")
    child_copy_option_group = el.find("CopyOptionGroup")
    if child_copy_option_group is not None:
        out["copy_option_group"] = (
            child_copy_option_group.text or ""
        ).lower() == "true"
    child_snapshot_availability_zone = el.find("SnapshotAvailabilityZone")
    if child_snapshot_availability_zone is not None:
        out["snapshot_availability_zone"] = str(
            child_snapshot_availability_zone.text or ""
        )
    return out
