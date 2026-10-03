"""Generated from Smithy shape ``com.amazonaws.rds#StartDBInstanceAutomatedBackupsReplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer_optional
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.tag_list


class StartDBInstanceAutomatedBackupsReplicationMessage(TypedDict, closed=True):
    source_db_instance_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the source DB instance for the replicated automated backups, for example, <code>arn:aws:rds:us-west-2:123456789012:db:mydatabase</code>.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The retention period for the replicated automated backups.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of the replicated automated backups. The KMS key ID is the Amazon Resource Name (ARN) for the KMS encryption key in the destination Amazon Web Services Region, for example, <code>arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE</code>.</p>"""
    pre_signed_url: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>In an Amazon Web Services GovCloud (US) Region, an URL that contains a Signature Version 4 signed request for the <code>StartDBInstanceAutomatedBackupsReplication</code> operation to call in the Amazon Web Services Region of the source DB instance. The presigned URL must be a valid request for the <code>StartDBInstanceAutomatedBackupsReplication</code> API operation that can run in the Amazon Web Services Region that contains the source DB instance.</p> <p>This setting applies only to Amazon Web Services GovCloud (US) Regions. It's ignored in other Amazon Web Services Regions.</p> <p>To learn how to generate a Signature Version 4 signed request, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html"> Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"> Signature Version 4 Signing Process</a>.</p> <note> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.</p> </note>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>A list of tags to associate with the replicated automated backups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartDBInstanceAutomatedBackupsReplicationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_db_instance_arn" in value:
        pairs.append(
            (f"{key_prefix}SourceDBInstanceArn", str(value["source_db_instance_arn"]))
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "pre_signed_url" in value:
        pairs.append((f"{key_prefix}PreSignedUrl", str(value["pre_signed_url"])))
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> StartDBInstanceAutomatedBackupsReplicationMessage:
    out: StartDBInstanceAutomatedBackupsReplicationMessage = {}  # type: ignore[typeddict-item]
    child_source_db_instance_arn = el.find("SourceDBInstanceArn")
    if child_source_db_instance_arn is not None:
        out["source_db_instance_arn"] = str(child_source_db_instance_arn.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_pre_signed_url = el.find("PreSignedUrl")
    if child_pre_signed_url is not None:
        out["pre_signed_url"] = str(child_pre_signed_url.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
