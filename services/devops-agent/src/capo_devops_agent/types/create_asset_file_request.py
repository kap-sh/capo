"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAssetFileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.asset_file_body
    import capo_devops_agent.types.asset_file_path
    import capo_devops_agent.types.resource_id


class CreateAssetFileRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset to create the file in</p>"""
    path: "capo_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of the file within the asset</p>"""
    content: "capo_devops_agent.types.asset_file_body.AssetFileBody"
    """<p>The content of the file to create</p>"""
    metadata: NotRequired["object"]
    """<p>Optional metadata describing this file</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent asset file creation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetFileRequest) -> dict:
    out: dict = {}
    import capo_devops_agent.types.asset_file_body

    out["content"] = capo_devops_agent.types.asset_file_body.serialize_json(
        value["content"]
    )
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetFileRequest:
    out: CreateAssetFileRequest = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_devops_agent.types.asset_file_body

        out["content"] = capo_devops_agent.types.asset_file_body.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
