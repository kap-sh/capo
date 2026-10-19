"""Generated from Smithy shape ``com.amazonaws.appfabric#Tenant``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.string2048
    import capo_appfabric.types.tenant_identifier


class Tenant(TypedDict, closed=True):
    tenant_identifier: "capo_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    tenant_display_name: "capo_appfabric.types.string2048.String2048"
    """<p>The display name of the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tenant) -> dict:
    out: dict = {}
    out["tenantIdentifier"] = value["tenant_identifier"]
    out["tenantDisplayName"] = value["tenant_display_name"]
    return out


def deserialize_json(data: dict) -> Tenant:
    out: Tenant = {}  # type: ignore[typeddict-item]
    if data.get("tenantIdentifier") is not None:
        out["tenant_identifier"] = data["tenantIdentifier"]
    else:
        out["tenant_identifier"] = ""
    if data.get("tenantDisplayName") is not None:
        out["tenant_display_name"] = data["tenantDisplayName"]
    else:
        out["tenant_display_name"] = ""
    return out
