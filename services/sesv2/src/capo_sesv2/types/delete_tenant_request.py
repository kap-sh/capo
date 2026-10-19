"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteTenantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.tenant_name


class DeleteTenantRequest(TypedDict, closed=True):
    tenant_name: "capo_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTenantRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    return out


def deserialize_json(data: dict) -> DeleteTenantRequest:
    out: DeleteTenantRequest = {}  # type: ignore[typeddict-item]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    else:
        out["tenant_name"] = ""
    return out
