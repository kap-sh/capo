"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_spec
    import capo_app_mesh.types.gateway_route_status
    import capo_app_mesh.types.resource_metadata
    import capo_app_mesh.types.resource_name


class GatewayRouteData(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the resource resides in. </p>"""
    gateway_route_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the gateway route.</p>"""
    virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The virtual gateway that the gateway route is associated with.</p>"""
    spec: "capo_app_mesh.types.gateway_route_spec.GatewayRouteSpec"
    """<p>The specifications of the gateway route.</p>"""
    metadata: "capo_app_mesh.types.resource_metadata.ResourceMetadata"
    status: "capo_app_mesh.types.gateway_route_status.GatewayRouteStatus"
    """<p>The status of the gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["gatewayRouteName"] = value["gateway_route_name"]
    out["virtualGatewayName"] = value["virtual_gateway_name"]
    import capo_app_mesh.types.gateway_route_spec

    out["spec"] = capo_app_mesh.types.gateway_route_spec.serialize_json(value["spec"])
    import capo_app_mesh.types.resource_metadata

    out["metadata"] = capo_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import capo_app_mesh.types.gateway_route_status

    out["status"] = capo_app_mesh.types.gateway_route_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GatewayRouteData:
    out: GatewayRouteData = {}  # type: ignore[typeddict-item]
    if data.get("meshName") is not None:
        out["mesh_name"] = data["meshName"]
    else:
        out["mesh_name"] = ""
    if data.get("gatewayRouteName") is not None:
        out["gateway_route_name"] = data["gatewayRouteName"]
    else:
        out["gateway_route_name"] = ""
    if data.get("virtualGatewayName") is not None:
        out["virtual_gateway_name"] = data["virtualGatewayName"]
    else:
        out["virtual_gateway_name"] = ""
    if data.get("spec") is not None:
        import capo_app_mesh.types.gateway_route_spec

        out["spec"] = capo_app_mesh.types.gateway_route_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("GatewayRouteData.spec required")
    if data.get("metadata") is not None:
        import capo_app_mesh.types.resource_metadata

        out["metadata"] = capo_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("GatewayRouteData.metadata required")
    if data.get("status") is not None:
        import capo_app_mesh.types.gateway_route_status

        out["status"] = capo_app_mesh.types.gateway_route_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GatewayRouteData.status required")
    return out
