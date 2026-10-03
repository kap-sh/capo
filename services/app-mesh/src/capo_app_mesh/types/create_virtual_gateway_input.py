"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateVirtualGatewayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.account_id
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.tag_list
    import capo_app_mesh.types.virtual_gateway_spec


class CreateVirtualGatewayInput(TypedDict, closed=True):
    virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name to use for the virtual gateway.</p>"""
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh to create the virtual gateway in.</p>"""
    spec: "capo_app_mesh.types.virtual_gateway_spec.VirtualGatewaySpec"
    """<p>The virtual gateway specification to apply.</p>"""
    tags: NotRequired["capo_app_mesh.types.tag_list.TagList"]
    """<p>Optional metadata that you can apply to the virtual gateway to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""
    mesh_owner: NotRequired["capo_app_mesh.types.account_id.AccountId"]
    """<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualGatewayInput) -> dict:
    out: dict = {}
    out["virtualGatewayName"] = value["virtual_gateway_name"]
    import capo_app_mesh.types.virtual_gateway_spec

    out["spec"] = capo_app_mesh.types.virtual_gateway_spec.serialize_json(value["spec"])
    if "tags" in value:
        import capo_app_mesh.types.tag_list

        out["tags"] = capo_app_mesh.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateVirtualGatewayInput:
    out: CreateVirtualGatewayInput = {}  # type: ignore[typeddict-item]
    if data.get("virtualGatewayName") is not None:
        out["virtual_gateway_name"] = data["virtualGatewayName"]
    else:
        raise DeserializationError(
            "CreateVirtualGatewayInput.virtual_gateway_name required"
        )
    if data.get("spec") is not None:
        import capo_app_mesh.types.virtual_gateway_spec

        out["spec"] = capo_app_mesh.types.virtual_gateway_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("CreateVirtualGatewayInput.spec required")
    if data.get("tags") is not None:
        import capo_app_mesh.types.tag_list

        out["tags"] = capo_app_mesh.types.tag_list.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
