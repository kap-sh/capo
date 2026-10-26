"""Generated from Smithy shape ``com.amazonaws.appmesh#Backend``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_service_backend


class _Backend_virtualService(TypedDict, closed=True):
    virtualService: "capo_app_mesh.types.virtual_service_backend.VirtualServiceBackend"


Backend: TypeAlias = _Backend_virtualService | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Backend) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Backend: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "virtualService" in value:
        import capo_app_mesh.types.virtual_service_backend

        return {
            "virtualService": capo_app_mesh.types.virtual_service_backend.serialize_json(
                value["virtualService"]
            )
        }
    else:
        raise SerializationError("Backend: no variant present")


def deserialize_json(data: dict) -> Backend:
    if data.get("virtualService") is not None:
        import capo_app_mesh.types.virtual_service_backend

        return {
            "virtualService": capo_app_mesh.types.virtual_service_backend.deserialize_json(
                data["virtualService"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Backend: no recognized variant key")
