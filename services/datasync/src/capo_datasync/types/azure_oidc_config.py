"""Generated from Smithy shape ``com.amazonaws.datasync#AzureOidcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.azure_guid_string


class AzureOidcConfig(TypedDict, closed=True):
    tenant_id: "capo_datasync.types.azure_guid_string.AzureGuidString"
    """<p>Azure tenant ID string.</p>"""
    client_id: "capo_datasync.types.azure_guid_string.AzureGuidString"
    """<p>Azure client ID string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureOidcConfig) -> dict:
    out: dict = {}
    out["TenantId"] = value["tenant_id"]
    out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AzureOidcConfig:
    out: AzureOidcConfig = {}  # type: ignore[typeddict-item]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    else:
        out["tenant_id"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    return out
