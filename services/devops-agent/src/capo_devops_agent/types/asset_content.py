"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file_content
    import capo_devops_agent.types.asset_source_url_content
    import capo_devops_agent.types.asset_zip_content


class _AssetContent_file(TypedDict, closed=True):
    file: "capo_devops_agent.types.asset_file_content.AssetFileContent"


class _AssetContent_zip(TypedDict, closed=True):
    zip: "capo_devops_agent.types.asset_zip_content.AssetZipContent"


class _AssetContent_sourceUrl(TypedDict, closed=True):
    sourceUrl: "capo_devops_agent.types.asset_source_url_content.AssetSourceUrlContent"


AssetContent: TypeAlias = (
    _AssetContent_file
    | _AssetContent_zip
    | _AssetContent_sourceUrl
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssetContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "file" in value:
        import capo_devops_agent.types.asset_file_content

        return {
            "file": capo_devops_agent.types.asset_file_content.serialize_json(
                value["file"]
            )
        }
    elif "zip" in value:
        import capo_devops_agent.types.asset_zip_content

        return {
            "zip": capo_devops_agent.types.asset_zip_content.serialize_json(
                value["zip"]
            )
        }
    elif "sourceUrl" in value:
        import capo_devops_agent.types.asset_source_url_content

        return {
            "sourceUrl": capo_devops_agent.types.asset_source_url_content.serialize_json(
                value["sourceUrl"]
            )
        }
    else:
        raise SerializationError("AssetContent: no variant present")


def deserialize_json(data: dict) -> AssetContent:
    if data.get("file") is not None:
        import capo_devops_agent.types.asset_file_content

        return {
            "file": capo_devops_agent.types.asset_file_content.deserialize_json(
                data["file"]
            )
        }
    elif data.get("zip") is not None:
        import capo_devops_agent.types.asset_zip_content

        return {
            "zip": capo_devops_agent.types.asset_zip_content.deserialize_json(
                data["zip"]
            )
        }
    elif data.get("sourceUrl") is not None:
        import capo_devops_agent.types.asset_source_url_content

        return {
            "sourceUrl": capo_devops_agent.types.asset_source_url_content.deserialize_json(
                data["sourceUrl"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AssetContent: no recognized variant key")
