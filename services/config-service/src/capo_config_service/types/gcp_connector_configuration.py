"""Generated from Smithy shape ``com.amazonaws.configservice#GcpConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.gcp_organization_id
    import capo_config_service.types.gcp_service_account_email
    import capo_config_service.types.gcp_workload_identity_pool_provider


class GcpConnectorConfiguration(TypedDict, closed=True):
    gcp_organization_id: NotRequired[
        "capo_config_service.types.gcp_organization_id.GcpOrganizationId"
    ]
    """<p>The ID of the Google Cloud organization that contains the connector's management project, which is the project of the service account in <code>serviceAccountEmail</code>.</p> <p>Required if the management project belongs to an organization. A connector needs an organization ID to record an entire organization or more than one project. Omit it only if the management project doesn't belong to an organization. In that case, the connector can record only the management project.</p>"""
    service_account_email: (
        "capo_config_service.types.gcp_service_account_email.GcpServiceAccountEmail"
    )
    """<p>The email address of the Google Cloud service account that Config uses to access your Google Cloud resources. The format is <code>SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com</code>.</p> <p>The project that contains this service account is the connector's management project. If the connector has no <code>gcpOrganizationId</code>, it can record only the management project.</p>"""
    workload_identity_pool_provider: "capo_config_service.types.gcp_workload_identity_pool_provider.GcpWorkloadIdentityPoolProvider"
    """<p>The full resource name of the Google Cloud workload identity pool provider that trusts Config. The format is <code>projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GcpConnectorConfiguration) -> dict:
    out: dict = {}
    if "gcp_organization_id" in value:
        out["gcpOrganizationId"] = value["gcp_organization_id"]
    out["serviceAccountEmail"] = value["service_account_email"]
    out["workloadIdentityPoolProvider"] = value["workload_identity_pool_provider"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GcpConnectorConfiguration:
    out: GcpConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("gcpOrganizationId") is not None:
        out["gcp_organization_id"] = data["gcpOrganizationId"]
    if data.get("serviceAccountEmail") is not None:
        out["service_account_email"] = data["serviceAccountEmail"]
    else:
        out["service_account_email"] = ""
    if data.get("workloadIdentityPoolProvider") is not None:
        out["workload_identity_pool_provider"] = data["workloadIdentityPoolProvider"]
    else:
        out["workload_identity_pool_provider"] = ""
    return out
