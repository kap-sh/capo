"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.asset_file_body
    import capo_devops_agent.types.asset_file_path


class AssetFile(TypedDict, closed=True):
    path: "capo_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of this file within the asset</p>"""
    content: "capo_devops_agent.types.asset_file_body.AssetFileBody"
    """<p>The content of this file</p>"""
    metadata: NotRequired["object"]
    """<p>The metadata for this file</p>"""
    version: "int"
    """<p>The asset version this file belongs to</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when this file was created</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when this file was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetFile) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import capo_devops_agent.types.asset_file_body

    out["content"] = capo_devops_agent.types.asset_file_body.serialize_json(
        value["content"]
    )
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    out["version"] = value["version"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types._prelude.timestamp

    out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AssetFile:
    out: AssetFile = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("content") is not None:
        import capo_devops_agent.types.asset_file_body

        out["content"] = capo_devops_agent.types.asset_file_body.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if data.get("createdAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
