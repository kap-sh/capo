"""Generated from Smithy shape ``com.amazonaws.ssm#GcpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.gcp_configuration_targets
    import capo_ssm.types.gcp_organization_id
    import capo_ssm.types.gcp_service_account_email
    import capo_ssm.types.gcp_workload_identity_pool_provider


class GcpConfiguration(TypedDict, closed=True):
    organization_id: NotRequired["capo_ssm.types.gcp_organization_id.GcpOrganizationId"]
    """<p>The ID of the GCP organization.</p>"""
    workload_identity_pool_provider: "capo_ssm.types.gcp_workload_identity_pool_provider.GcpWorkloadIdentityPoolProvider"
    """<p>The full resource name of the GCP workload identity pool provider used for authentication.</p>"""
    service_account_email: (
        "capo_ssm.types.gcp_service_account_email.GcpServiceAccountEmail"
    )
    """<p>The email address of the GCP service account used for authentication.</p>"""
    targets: NotRequired[
        "capo_ssm.types.gcp_configuration_targets.GcpConfigurationTargets"
    ]
    """<p>The target GCP projects for the cloud connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GcpConfiguration) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    out["WorkloadIdentityPoolProvider"] = value["workload_identity_pool_provider"]
    out["ServiceAccountEmail"] = value["service_account_email"]
    if "targets" in value:
        import capo_ssm.types.gcp_configuration_targets

        out["Targets"] = (
            capo_ssm.types.gcp_configuration_targets.serialize_aws_json_1_1(
                value["targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GcpConfiguration:
    out: GcpConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    if data.get("WorkloadIdentityPoolProvider") is not None:
        out["workload_identity_pool_provider"] = data["WorkloadIdentityPoolProvider"]
    else:
        out["workload_identity_pool_provider"] = ""
    if data.get("ServiceAccountEmail") is not None:
        out["service_account_email"] = data["ServiceAccountEmail"]
    else:
        out["service_account_email"] = ""
    if data.get("Targets") is not None:
        import capo_ssm.types.gcp_configuration_targets

        out["targets"] = (
            capo_ssm.types.gcp_configuration_targets.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    return out
