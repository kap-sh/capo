"""Generated from Smithy shape ``com.amazonaws.appmesh#MeshData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.mesh_spec
    import capo_app_mesh.types.mesh_status
    import capo_app_mesh.types.resource_metadata
    import capo_app_mesh.types.resource_name


class MeshData(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh.</p>"""
    spec: "capo_app_mesh.types.mesh_spec.MeshSpec"
    """<p>The associated specification for the service mesh.</p>"""
    metadata: "capo_app_mesh.types.resource_metadata.ResourceMetadata"
    """<p>The associated metadata for the service mesh.</p>"""
    status: "capo_app_mesh.types.mesh_status.MeshStatus"
    """<p>The status of the service mesh.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeshData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    import capo_app_mesh.types.mesh_spec

    out["spec"] = capo_app_mesh.types.mesh_spec.serialize_json(value["spec"])
    import capo_app_mesh.types.resource_metadata

    out["metadata"] = capo_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import capo_app_mesh.types.mesh_status

    out["status"] = capo_app_mesh.types.mesh_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> MeshData:
    out: MeshData = {}  # type: ignore[typeddict-item]
    if data.get("meshName") is not None:
        out["mesh_name"] = data["meshName"]
    else:
        out["mesh_name"] = ""
    if data.get("spec") is not None:
        import capo_app_mesh.types.mesh_spec

        out["spec"] = capo_app_mesh.types.mesh_spec.deserialize_json(data["spec"])
    else:
        raise DeserializationError("MeshData.spec required")
    if data.get("metadata") is not None:
        import capo_app_mesh.types.resource_metadata

        out["metadata"] = capo_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("MeshData.metadata required")
    if data.get("status") is not None:
        import capo_app_mesh.types.mesh_status

        out["status"] = capo_app_mesh.types.mesh_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("MeshData.status required")
    return out
