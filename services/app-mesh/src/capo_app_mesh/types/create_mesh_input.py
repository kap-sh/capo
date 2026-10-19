"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateMeshInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.mesh_spec
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.tag_list


class CreateMeshInput(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name to use for the service mesh.</p>"""
    spec: NotRequired["capo_app_mesh.types.mesh_spec.MeshSpec"]
    """<p>The service mesh specification to apply.</p>"""
    tags: NotRequired["capo_app_mesh.types.tag_list.TagList"]
    """<p>Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeshInput) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    if "spec" in value:
        import capo_app_mesh.types.mesh_spec

        out["spec"] = capo_app_mesh.types.mesh_spec.serialize_json(value["spec"])
    if "tags" in value:
        import capo_app_mesh.types.tag_list

        out["tags"] = capo_app_mesh.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateMeshInput:
    out: CreateMeshInput = {}  # type: ignore[typeddict-item]
    if data.get("meshName") is not None:
        out["mesh_name"] = data["meshName"]
    else:
        out["mesh_name"] = ""
    if data.get("spec") is not None:
        import capo_app_mesh.types.mesh_spec

        out["spec"] = capo_app_mesh.types.mesh_spec.deserialize_json(data["spec"])
    if data.get("tags") is not None:
        import capo_app_mesh.types.tag_list

        out["tags"] = capo_app_mesh.types.tag_list.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
