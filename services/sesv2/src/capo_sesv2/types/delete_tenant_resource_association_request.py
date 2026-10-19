"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteTenantResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.tenant_name


class DeleteTenantResourceAssociationRequest(TypedDict, closed=True):
    tenant_name: "capo_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to remove the resource association from.</p>"""
    resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to remove from the tenant association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTenantResourceAssociationRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DeleteTenantResourceAssociationRequest:
    out: DeleteTenantResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    else:
        out["tenant_name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
