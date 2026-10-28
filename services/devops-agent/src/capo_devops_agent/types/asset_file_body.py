"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileBody``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file_bytes
    import capo_devops_agent.types.asset_file_text


class AssetFileBodyBytesMember(TypedDict, closed=True):
    bytes: "capo_devops_agent.types.asset_file_bytes.AssetFileBytes"


class AssetFileBodyTextMember(TypedDict, closed=True):
    text: "capo_devops_agent.types.asset_file_text.AssetFileText"


AssetFileBody: TypeAlias = (
    AssetFileBodyBytesMember | AssetFileBodyTextMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileBody) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssetFileBody: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "bytes" in value:
        import capo_devops_agent.types.asset_file_bytes

        return {
            "bytes": capo_devops_agent.types.asset_file_bytes.serialize_json(
                value["bytes"]
            )
        }
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("AssetFileBody: no variant present")


def deserialize_json(data: dict) -> AssetFileBody:
    if data.get("bytes") is not None:
        import capo_devops_agent.types.asset_file_bytes

        return {
            "bytes": capo_devops_agent.types.asset_file_bytes.deserialize_json(
                data["bytes"]
            )
        }
    elif data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AssetFileBody: no recognized variant key")
