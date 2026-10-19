"""Generated from Smithy shape ``com.amazonaws.configservice#AzureConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.azure_client_identifier
    import capo_config_service.types.azure_tenant_identifier


class AzureConnectorConfiguration(TypedDict, closed=True):
    tenant_identifier: (
        "capo_config_service.types.azure_tenant_identifier.AzureTenantIdentifier"
    )
    """<p>The Azure tenant identifier.</p>"""
    client_identifier: (
        "capo_config_service.types.azure_client_identifier.AzureClientIdentifier"
    )
    """<p>The Azure client identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureConnectorConfiguration) -> dict:
    out: dict = {}
    out["tenantIdentifier"] = value["tenant_identifier"]
    out["clientIdentifier"] = value["client_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AzureConnectorConfiguration:
    out: AzureConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tenantIdentifier") is not None:
        out["tenant_identifier"] = data["tenantIdentifier"]
    else:
        out["tenant_identifier"] = ""
    if data.get("clientIdentifier") is not None:
        out["client_identifier"] = data["clientIdentifier"]
    else:
        out["client_identifier"] = ""
    return out
