"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayConnectionPool``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_grpc_connection_pool
    import capo_app_mesh.types.virtual_gateway_http2_connection_pool
    import capo_app_mesh.types.virtual_gateway_http_connection_pool


class _VirtualGatewayConnectionPool_http(TypedDict, closed=True):
    http: "capo_app_mesh.types.virtual_gateway_http_connection_pool.VirtualGatewayHttpConnectionPool"


class _VirtualGatewayConnectionPool_http2(TypedDict, closed=True):
    http2: "capo_app_mesh.types.virtual_gateway_http2_connection_pool.VirtualGatewayHttp2ConnectionPool"


class _VirtualGatewayConnectionPool_grpc(TypedDict, closed=True):
    grpc: "capo_app_mesh.types.virtual_gateway_grpc_connection_pool.VirtualGatewayGrpcConnectionPool"


VirtualGatewayConnectionPool: TypeAlias = (
    _VirtualGatewayConnectionPool_http
    | _VirtualGatewayConnectionPool_http2
    | _VirtualGatewayConnectionPool_grpc
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayConnectionPool) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VirtualGatewayConnectionPool: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "http" in value:
        import capo_app_mesh.types.virtual_gateway_http_connection_pool

        return {
            "http": capo_app_mesh.types.virtual_gateway_http_connection_pool.serialize_json(
                value["http"]
            )
        }
    elif "http2" in value:
        import capo_app_mesh.types.virtual_gateway_http2_connection_pool

        return {
            "http2": capo_app_mesh.types.virtual_gateway_http2_connection_pool.serialize_json(
                value["http2"]
            )
        }
    elif "grpc" in value:
        import capo_app_mesh.types.virtual_gateway_grpc_connection_pool

        return {
            "grpc": capo_app_mesh.types.virtual_gateway_grpc_connection_pool.serialize_json(
                value["grpc"]
            )
        }
    else:
        raise SerializationError("VirtualGatewayConnectionPool: no variant present")


def deserialize_json(data: dict) -> VirtualGatewayConnectionPool:
    if data.get("http") is not None:
        import capo_app_mesh.types.virtual_gateway_http_connection_pool

        return {
            "http": capo_app_mesh.types.virtual_gateway_http_connection_pool.deserialize_json(
                data["http"]
            )
        }
    elif data.get("http2") is not None:
        import capo_app_mesh.types.virtual_gateway_http2_connection_pool

        return {
            "http2": capo_app_mesh.types.virtual_gateway_http2_connection_pool.deserialize_json(
                data["http2"]
            )
        }
    elif data.get("grpc") is not None:
        import capo_app_mesh.types.virtual_gateway_grpc_connection_pool

        return {
            "grpc": capo_app_mesh.types.virtual_gateway_grpc_connection_pool.deserialize_json(
                data["grpc"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "VirtualGatewayConnectionPool: no recognized variant key"
        )
