"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayAccessLog``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_file_access_log


class VirtualGatewayAccessLogFileMember(TypedDict, closed=True):
    file: "capo_app_mesh.types.virtual_gateway_file_access_log.VirtualGatewayFileAccessLog"


VirtualGatewayAccessLog: TypeAlias = (
    VirtualGatewayAccessLogFileMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayAccessLog) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VirtualGatewayAccessLog: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "file" in value:
        import capo_app_mesh.types.virtual_gateway_file_access_log

        return {
            "file": capo_app_mesh.types.virtual_gateway_file_access_log.serialize_json(
                value["file"]
            )
        }
    else:
        raise SerializationError("VirtualGatewayAccessLog: no variant present")


def deserialize_json(data: dict) -> VirtualGatewayAccessLog:
    if data.get("file") is not None:
        import capo_app_mesh.types.virtual_gateway_file_access_log

        return {
            "file": capo_app_mesh.types.virtual_gateway_file_access_log.deserialize_json(
                data["file"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("VirtualGatewayAccessLog: no recognized variant key")
