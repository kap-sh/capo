"""Generated from Smithy shape ``com.amazonaws.appmesh#RouteData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.resource_metadata
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.route_spec
    import capo_app_mesh.types.route_status


class RouteData(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the route resides in.</p>"""
    virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The virtual router that the route is associated with.</p>"""
    route_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the route.</p>"""
    spec: "capo_app_mesh.types.route_spec.RouteSpec"
    """<p>The specifications of the route.</p>"""
    metadata: "capo_app_mesh.types.resource_metadata.ResourceMetadata"
    """<p>The associated metadata for the route.</p>"""
    status: "capo_app_mesh.types.route_status.RouteStatus"
    """<p>The status of the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualRouterName"] = value["virtual_router_name"]
    out["routeName"] = value["route_name"]
    import capo_app_mesh.types.route_spec

    out["spec"] = capo_app_mesh.types.route_spec.serialize_json(value["spec"])
    import capo_app_mesh.types.resource_metadata

    out["metadata"] = capo_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import capo_app_mesh.types.route_status

    out["status"] = capo_app_mesh.types.route_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> RouteData:
    out: RouteData = {}  # type: ignore[typeddict-item]
    if data.get("meshName") is not None:
        out["mesh_name"] = data["meshName"]
    else:
        out["mesh_name"] = ""
    if data.get("virtualRouterName") is not None:
        out["virtual_router_name"] = data["virtualRouterName"]
    else:
        out["virtual_router_name"] = ""
    if data.get("routeName") is not None:
        out["route_name"] = data["routeName"]
    else:
        out["route_name"] = ""
    if data.get("spec") is not None:
        import capo_app_mesh.types.route_spec

        out["spec"] = capo_app_mesh.types.route_spec.deserialize_json(data["spec"])
    else:
        raise DeserializationError("RouteData.spec required")
    if data.get("metadata") is not None:
        import capo_app_mesh.types.resource_metadata

        out["metadata"] = capo_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("RouteData.metadata required")
    if data.get("status") is not None:
        import capo_app_mesh.types.route_status

        out["status"] = capo_app_mesh.types.route_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("RouteData.status required")
    return out
