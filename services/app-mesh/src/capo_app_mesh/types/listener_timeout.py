"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTimeout``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_timeout
    import capo_app_mesh.types.http_timeout
    import capo_app_mesh.types.tcp_timeout


class _ListenerTimeout_tcp(TypedDict, closed=True):
    tcp: "capo_app_mesh.types.tcp_timeout.TcpTimeout"


class _ListenerTimeout_http(TypedDict, closed=True):
    http: "capo_app_mesh.types.http_timeout.HttpTimeout"


class _ListenerTimeout_http2(TypedDict, closed=True):
    http2: "capo_app_mesh.types.http_timeout.HttpTimeout"


class _ListenerTimeout_grpc(TypedDict, closed=True):
    grpc: "capo_app_mesh.types.grpc_timeout.GrpcTimeout"


ListenerTimeout: TypeAlias = (
    _ListenerTimeout_tcp
    | _ListenerTimeout_http
    | _ListenerTimeout_http2
    | _ListenerTimeout_grpc
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTimeout) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ListenerTimeout: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tcp" in value:
        import capo_app_mesh.types.tcp_timeout

        return {"tcp": capo_app_mesh.types.tcp_timeout.serialize_json(value["tcp"])}
    elif "http" in value:
        import capo_app_mesh.types.http_timeout

        return {"http": capo_app_mesh.types.http_timeout.serialize_json(value["http"])}
    elif "http2" in value:
        import capo_app_mesh.types.http_timeout

        return {
            "http2": capo_app_mesh.types.http_timeout.serialize_json(value["http2"])
        }
    elif "grpc" in value:
        import capo_app_mesh.types.grpc_timeout

        return {"grpc": capo_app_mesh.types.grpc_timeout.serialize_json(value["grpc"])}
    else:
        raise SerializationError("ListenerTimeout: no variant present")


def deserialize_json(data: dict) -> ListenerTimeout:
    if data.get("tcp") is not None:
        import capo_app_mesh.types.tcp_timeout

        return {"tcp": capo_app_mesh.types.tcp_timeout.deserialize_json(data["tcp"])}
    elif data.get("http") is not None:
        import capo_app_mesh.types.http_timeout

        return {"http": capo_app_mesh.types.http_timeout.deserialize_json(data["http"])}
    elif data.get("http2") is not None:
        import capo_app_mesh.types.http_timeout

        return {
            "http2": capo_app_mesh.types.http_timeout.deserialize_json(data["http2"])
        }
    elif data.get("grpc") is not None:
        import capo_app_mesh.types.grpc_timeout

        return {"grpc": capo_app_mesh.types.grpc_timeout.deserialize_json(data["grpc"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ListenerTimeout: no recognized variant key")
