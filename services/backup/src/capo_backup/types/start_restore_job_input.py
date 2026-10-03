"""Generated from Smithy shape ``com.amazonaws.backup#StartRestoreJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.boolean2
    import capo_backup.types.iam_role_arn
    import capo_backup.types.metadata
    import capo_backup.types.resource_type
    import capo_backup.types.string


class StartRestoreJobInput(TypedDict, closed=True):
    recovery_point_arn: "capo_backup.types.arn.ARN"
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    metadata: "capo_backup.types.metadata.Metadata"
    """<p>A set of metadata key-value pairs.</p> <p>You can get configuration metadata about a resource at the time it was backed up by calling <code>GetRecoveryPointRestoreMetadata</code>. However, values in addition to those provided by <code>GetRecoveryPointRestoreMetadata</code> might be required to restore a resource. For example, you might need to provide a new resource name if the original already exists.</p> <p>For more information about the metadata for each resource, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-aur.html#aur-restore-cli">Metadata for Amazon Aurora</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-docdb.html#docdb-restore-cli">Metadata for Amazon DocumentDB</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-application-stacks.html#restoring-cfn-cli">Metadata for CloudFormation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-dynamodb.html#ddb-restore-cli">Metadata for Amazon DynamoDB</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ebs.html#ebs-restore-cli"> Metadata for Amazon EBS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ec2.html#restoring-ec2-cli">Metadata for Amazon EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-efs.html#efs-restore-cli">Metadata for Amazon EFS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-eks.html#eks-restore-backup-section">Metadata for Amazon EKS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-fsx.html#fsx-restore-cli">Metadata for Amazon FSx</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-nep.html#nep-restore-cli">Metadata for Amazon Neptune</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-rds.html#rds-restore-cli">Metadata for Amazon RDS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-restores.html#redshift-restore-api">Metadata for Amazon Redshift</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html#restoring-sgw-cli">Metadata for Storage Gateway</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html#s3-restore-cli">Metadata for Amazon S3</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/timestream-restore.html#timestream-restore-api">Metadata for Amazon Timestream</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-vm.html#vm-restore-cli">Metadata for virtual machines</a> </p> </li> </ul>"""
    iam_role_arn: NotRequired["capo_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that Backup uses to create the target resource; for example: <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartRestoreJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>Starts a job to restore a recovery point for one of the following resources:</p> <ul> <li> <p> <code>Aurora</code> - Amazon Aurora</p> </li> <li> <p> <code>DocumentDB</code> - Amazon DocumentDB</p> </li> <li> <p> <code>CloudFormation</code> - CloudFormation</p> </li> <li> <p> <code>DynamoDB</code> - Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> - Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> - Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> - Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> - Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> - Amazon FSx</p> </li> <li> <p> <code>Neptune</code> - Amazon Neptune</p> </li> <li> <p> <code>RDS</code> - Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> - Amazon Redshift</p> </li> <li> <p> <code>Storage Gateway</code> - Storage Gateway</p> </li> <li> <p> <code>S3</code> - Amazon Simple Storage Service</p> </li> <li> <p> <code>Timestream</code> - Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> - Virtual machines</p> </li> </ul>"""
    copy_source_tags_to_restored_resource: "capo_backup.types.boolean2.Boolean2"
    """<p>This is an optional parameter. If this equals <code>True</code>, tags included in the backup will be copied to the restored resource.</p> <p>This can only be applied to backups created through Backup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRestoreJobInput) -> dict:
    out: dict = {}
    out["RecoveryPointArn"] = value["recovery_point_arn"]
    import capo_backup.types.metadata

    out["Metadata"] = capo_backup.types.metadata.serialize_json(value["metadata"])
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["CopySourceTagsToRestoredResource"] = value.get(
        "copy_source_tags_to_restored_resource", False
    )
    return out


def deserialize_json(data: dict) -> StartRestoreJobInput:
    out: StartRestoreJobInput = {}  # type: ignore[typeddict-item]
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    else:
        raise DeserializationError("StartRestoreJobInput.recovery_point_arn required")
    if data.get("Metadata") is not None:
        import capo_backup.types.metadata

        out["metadata"] = capo_backup.types.metadata.deserialize_json(data["Metadata"])
    else:
        raise DeserializationError("StartRestoreJobInput.metadata required")
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("CopySourceTagsToRestoredResource") is not None:
        out["copy_source_tags_to_restored_resource"] = data[
            "CopySourceTagsToRestoredResource"
        ]
    else:
        out["copy_source_tags_to_restored_resource"] = False
    return out
