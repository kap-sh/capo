"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreFromSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.workgroup_name


class RestoreFromSnapshotRequest(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to restore the snapshot to.</p>"""
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup used to restore the snapshot.</p>"""
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot to restore from. Must not be specified at the same time as <code>snapshotArn</code>.</p>"""
    snapshot_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the snapshot to restore from. Required if restoring from a provisioned cluster to Amazon Redshift Serverless. Must not be specified at the same time as <code>snapshotName</code>.</p> <p>The format of the ARN is arn:aws:redshift:&lt;region&gt;:&lt;account_id&gt;:snapshot:&lt;cluster_identifier&gt;/&lt;snapshot_identifier&gt;.</p>"""
    owner_account: NotRequired["str"]
    """<p>The Amazon Web Services account that owns the snapshot.</p>"""
    manage_admin_password: NotRequired["bool"]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the restored snapshot's admin credentials. If <code>MmanageAdminPassword</code> is false or not set, Amazon Redshift uses the admin credentials that the namespace or cluster had at the time the snapshot was taken.</p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>"""
    maintain_integration: NotRequired["bool"]
    """<p>If <code>true</code>, maintain existing data sharing, zero-ETL and S3 event integrations when restoring. Otherwise, integrations will not be maintained after the restore operation. Integrations are only maintained when restored to the same serverless namespace.</p> <p>Default: true</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromSnapshotRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["workgroupName"] = value["workgroup_name"]
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "snapshot_arn" in value:
        out["snapshotArn"] = value["snapshot_arn"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "manage_admin_password" in value:
        out["manageAdminPassword"] = value["manage_admin_password"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    if "maintain_integration" in value:
        out["maintainIntegration"] = value["maintain_integration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromSnapshotRequest:
    out: RestoreFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    if data.get("snapshotArn") is not None:
        out["snapshot_arn"] = data["snapshotArn"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("manageAdminPassword") is not None:
        out["manage_admin_password"] = data["manageAdminPassword"]
    if data.get("adminPasswordSecretKmsKeyId") is not None:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    if data.get("maintainIntegration") is not None:
        out["maintain_integration"] = data["maintainIntegration"]
    return out
