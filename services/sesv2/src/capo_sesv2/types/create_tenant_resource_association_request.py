"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateTenantResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.tenant_name


class CreateTenantResourceAssociationRequest(TypedDict, closed=True):
    tenant_name: "capo_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to associate the resource with.</p>"""
    resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to associate with the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTenantResourceAssociationRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> CreateTenantResourceAssociationRequest:
    out: CreateTenantResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    else:
        out["tenant_name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
