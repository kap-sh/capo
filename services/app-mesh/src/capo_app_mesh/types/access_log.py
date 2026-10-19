"""Generated from Smithy shape ``com.amazonaws.appmesh#AccessLog``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.file_access_log


class _AccessLog_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.file_access_log.FileAccessLog"


AccessLog: TypeAlias = _AccessLog_file | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: AccessLog) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AccessLog: cannot serialize unknown variant {value.name!r}"
        )
    elif "file" in value:
        import capo_app_mesh.types.file_access_log

        return {
            "file": capo_app_mesh.types.file_access_log.serialize_json(value["file"])
        }
    else:
        raise SerializationError("AccessLog: no variant present")


def deserialize_json(data: dict) -> AccessLog:
    if data.get("file") is not None:
        import capo_app_mesh.types.file_access_log

        return {
            "file": capo_app_mesh.types.file_access_log.deserialize_json(data["file"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AccessLog: no recognized variant key")
