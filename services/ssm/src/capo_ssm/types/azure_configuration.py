"""Generated from Smithy shape ``com.amazonaws.ssm#AzureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.azure_application_display_name
    import capo_ssm.types.azure_application_id
    import capo_ssm.types.azure_tenant_display_name
    import capo_ssm.types.azure_tenant_id
    import capo_ssm.types.configuration_targets


class AzureConfiguration(TypedDict, closed=True):
    tenant_id: "capo_ssm.types.azure_tenant_id.AzureTenantId"
    """<p>The ID of the Azure tenant.</p>"""
    tenant_display_name: NotRequired[
        "capo_ssm.types.azure_tenant_display_name.AzureTenantDisplayName"
    ]
    """<p>The display name of the Azure tenant.</p>"""
    application_id: "capo_ssm.types.azure_application_id.AzureApplicationId"
    """<p>The ID of the Azure application registration used for authentication.</p>"""
    application_display_name: NotRequired[
        "capo_ssm.types.azure_application_display_name.AzureApplicationDisplayName"
    ]
    """<p>The display name of the Azure application registration.</p>"""
    targets: NotRequired["capo_ssm.types.configuration_targets.ConfigurationTargets"]
    """<p>The target Azure subscriptions for the cloud connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureConfiguration) -> dict:
    out: dict = {}
    out["TenantId"] = value["tenant_id"]
    if "tenant_display_name" in value:
        out["TenantDisplayName"] = value["tenant_display_name"]
    out["ApplicationId"] = value["application_id"]
    if "application_display_name" in value:
        out["ApplicationDisplayName"] = value["application_display_name"]
    if "targets" in value:
        import capo_ssm.types.configuration_targets

        out["Targets"] = capo_ssm.types.configuration_targets.serialize_aws_json_1_1(
            value["targets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AzureConfiguration:
    out: AzureConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    else:
        out["tenant_id"] = ""
    if data.get("TenantDisplayName") is not None:
        out["tenant_display_name"] = data["TenantDisplayName"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        out["application_id"] = ""
    if data.get("ApplicationDisplayName") is not None:
        out["application_display_name"] = data["ApplicationDisplayName"]
    if data.get("Targets") is not None:
        import capo_ssm.types.configuration_targets

        out["targets"] = capo_ssm.types.configuration_targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    return out
