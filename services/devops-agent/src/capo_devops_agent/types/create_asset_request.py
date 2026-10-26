"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.asset_content
    import capo_devops_agent.types.asset_type


class CreateAssetRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space where the asset will be created</p>"""
    asset_type: "capo_devops_agent.types.asset_type.AssetType"
    """<p>The type of asset to create</p>"""
    metadata: NotRequired["object"]
    """<p>The metadata describing this asset</p>"""
    content: "capo_devops_agent.types.asset_content.AssetContent"
    """<p>The content for the asset. Provide a single file, a zip bundle, or a sourceUrl to import from an external source.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent asset creation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetRequest) -> dict:
    out: dict = {}
    out["assetType"] = value["asset_type"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    import capo_devops_agent.types.asset_content

    out["content"] = capo_devops_agent.types.asset_content.serialize_json(
        value["content"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetRequest:
    out: CreateAssetRequest = {}  # type: ignore[typeddict-item]
    if data.get("assetType") is not None:
        out["asset_type"] = data["assetType"]
    else:
        out["asset_type"] = ""
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("content") is not None:
        import capo_devops_agent.types.asset_content

        out["content"] = capo_devops_agent.types.asset_content.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
