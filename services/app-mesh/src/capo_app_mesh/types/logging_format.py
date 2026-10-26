"""Generated from Smithy shape ``com.amazonaws.appmesh#LoggingFormat``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.json_format
    import capo_app_mesh.types.text_format


class _LoggingFormat_text(TypedDict, closed=True):
    text: "capo_app_mesh.types.text_format.TextFormat"


class _LoggingFormat_json(TypedDict, closed=True):
    json: "capo_app_mesh.types.json_format.JsonFormat"


LoggingFormat: TypeAlias = (
    _LoggingFormat_text | _LoggingFormat_json | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: LoggingFormat) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"LoggingFormat: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        import capo_app_mesh.types.json_format

        return {"json": capo_app_mesh.types.json_format.serialize_json(value["json"])}
    else:
        raise SerializationError("LoggingFormat: no variant present")


def deserialize_json(data: dict) -> LoggingFormat:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("json") is not None:
        import capo_app_mesh.types.json_format

        return {"json": capo_app_mesh.types.json_format.deserialize_json(data["json"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("LoggingFormat: no recognized variant key")
