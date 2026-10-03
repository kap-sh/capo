"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateVirtualGatewayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.account_id
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.virtual_gateway_spec


class UpdateVirtualGatewayInput(TypedDict, closed=True):
    virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual gateway to update.</p>"""
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual gateway resides in.</p>"""
    spec: "capo_app_mesh.types.virtual_gateway_spec.VirtualGatewaySpec"
    """<p>The new virtual gateway specification to apply. This overwrites the existing data.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""
    mesh_owner: NotRequired["capo_app_mesh.types.account_id.AccountId"]
    """<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualGatewayInput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_gateway_spec

    out["spec"] = capo_app_mesh.types.virtual_gateway_spec.serialize_json(value["spec"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateVirtualGatewayInput:
    out: UpdateVirtualGatewayInput = {}  # type: ignore[typeddict-item]
    if data.get("spec") is not None:
        import capo_app_mesh.types.virtual_gateway_spec

        out["spec"] = capo_app_mesh.types.virtual_gateway_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("UpdateVirtualGatewayInput.spec required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
