"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#IntuneConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.azure_application_id
    import capo_pca_connector_scep.types.azure_domain


class IntuneConfiguration(TypedDict, closed=True):
    azure_application_id: (
        "capo_pca_connector_scep.types.azure_application_id.AzureApplicationId"
    )
    """<p>The directory (tenant) ID from your Microsoft Entra ID app registration.</p>"""
    domain: "capo_pca_connector_scep.types.azure_domain.AzureDomain"
    """<p>The primary domain from your Microsoft Entra ID app registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntuneConfiguration) -> dict:
    out: dict = {}
    out["AzureApplicationId"] = value["azure_application_id"]
    out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> IntuneConfiguration:
    out: IntuneConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AzureApplicationId") is not None:
        out["azure_application_id"] = data["AzureApplicationId"]
    else:
        out["azure_application_id"] = ""
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    return out
