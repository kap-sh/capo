"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_node_service_provider
    import capo_app_mesh.types.virtual_router_service_provider


class _VirtualServiceProvider_virtualNode(TypedDict, closed=True):
    virtualNode: (
        "capo_app_mesh.types.virtual_node_service_provider.VirtualNodeServiceProvider"
    )


class _VirtualServiceProvider_virtualRouter(TypedDict, closed=True):
    virtualRouter: "capo_app_mesh.types.virtual_router_service_provider.VirtualRouterServiceProvider"


VirtualServiceProvider: TypeAlias = (
    _VirtualServiceProvider_virtualNode
    | _VirtualServiceProvider_virtualRouter
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceProvider) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"VirtualServiceProvider: cannot serialize unknown variant {value.name!r}"
        )
    elif "virtualNode" in value:
        import capo_app_mesh.types.virtual_node_service_provider

        return {
            "virtualNode": capo_app_mesh.types.virtual_node_service_provider.serialize_json(
                value["virtualNode"]
            )
        }
    elif "virtualRouter" in value:
        import capo_app_mesh.types.virtual_router_service_provider

        return {
            "virtualRouter": capo_app_mesh.types.virtual_router_service_provider.serialize_json(
                value["virtualRouter"]
            )
        }
    else:
        raise SerializationError("VirtualServiceProvider: no variant present")


def deserialize_json(data: dict) -> VirtualServiceProvider:
    if data.get("virtualNode") is not None:
        import capo_app_mesh.types.virtual_node_service_provider

        return {
            "virtualNode": capo_app_mesh.types.virtual_node_service_provider.deserialize_json(
                data["virtualNode"]
            )
        }
    elif data.get("virtualRouter") is not None:
        import capo_app_mesh.types.virtual_router_service_provider

        return {
            "virtualRouter": capo_app_mesh.types.virtual_router_service_provider.deserialize_json(
                data["virtualRouter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("VirtualServiceProvider: no recognized variant key")
