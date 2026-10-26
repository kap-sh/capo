"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file_body
    import capo_devops_agent.types.asset_file_path


class AssetFileContent(TypedDict, closed=True):
    path: "capo_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of the file within the asset</p>"""
    body: "capo_devops_agent.types.asset_file_body.AssetFileBody"
    """<p>The file content</p>"""
    metadata: NotRequired["object"]
    """<p>Optional metadata for this file</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileContent) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import capo_devops_agent.types.asset_file_body

    out["body"] = capo_devops_agent.types.asset_file_body.serialize_json(value["body"])
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AssetFileContent:
    out: AssetFileContent = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("body") is not None:
        import capo_devops_agent.types.asset_file_body

        out["body"] = capo_devops_agent.types.asset_file_body.deserialize_json(
            data["body"]
        )
    else:
        out["body"] = {"$unknown": {"name": ""}}
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    return out
