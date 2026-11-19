"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_client_identifier
    import capo_observabilityadmin.types.azure_tenant_identifier


class AzureConnectorConfiguration(TypedDict, closed=True):
    tenant_identifier: (
        "capo_observabilityadmin.types.azure_tenant_identifier.AzureTenantIdentifier"
    )
    """<p>The ID of the Microsoft Entra ID tenant.</p>"""
    client_identifier: (
        "capo_observabilityadmin.types.azure_client_identifier.AzureClientIdentifier"
    )
    """<p>The application (client) ID of the Azure app registration. The app registration must have a federated identity credential that trusts the Amazon Web Services OpenID Connect (OIDC) issuer for your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureConnectorConfiguration) -> dict:
    out: dict = {}
    out["TenantIdentifier"] = value["tenant_identifier"]
    out["ClientIdentifier"] = value["client_identifier"]
    return out


def deserialize_json(data: dict) -> AzureConnectorConfiguration:
    out: AzureConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TenantIdentifier") is not None:
        out["tenant_identifier"] = data["TenantIdentifier"]
    else:
        out["tenant_identifier"] = ""
    if data.get("ClientIdentifier") is not None:
        out["client_identifier"] = data["ClientIdentifier"]
    else:
        out["client_identifier"] = ""
    return out
