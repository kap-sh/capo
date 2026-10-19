"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreFromRecoveryPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.workgroup_name


class RestoreFromRecoveryPointRequest(TypedDict, closed=True):
    recovery_point_id: "str"
    """<p>The unique identifier of the recovery point to restore from.</p>"""
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to restore data into.</p>"""
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup used to restore data.</p>"""
    maintain_integration: NotRequired["bool"]
    """<p>If <code>true</code>, maintain existing data sharing, zero-ETL and S3 event integrations when restoring. Otherwise, integrations will not be maintained after the restore operation. Integrations are only maintained when restored to the same serverless namespace.</p> <p>Default: true</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromRecoveryPointRequest) -> dict:
    out: dict = {}
    out["recoveryPointId"] = value["recovery_point_id"]
    out["namespaceName"] = value["namespace_name"]
    out["workgroupName"] = value["workgroup_name"]
    if "maintain_integration" in value:
        out["maintainIntegration"] = value["maintain_integration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromRecoveryPointRequest:
    out: RestoreFromRecoveryPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPointId") is not None:
        out["recovery_point_id"] = data["recoveryPointId"]
    else:
        out["recovery_point_id"] = ""
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    if data.get("maintainIntegration") is not None:
        out["maintain_integration"] = data["maintainIntegration"]
    return out
