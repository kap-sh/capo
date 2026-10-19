"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetArtifactMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.artifact_ids


class BatchGetArtifactMetadataInput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space that contains the artifacts.</p>"""
    artifact_ids: "capo_securityagent.types.artifact_ids.ArtifactIds"
    """<p>The list of artifact identifiers to retrieve metadata for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetArtifactMetadataInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_securityagent.types.artifact_ids

    out["artifactIds"] = capo_securityagent.types.artifact_ids.serialize_json(
        value["artifact_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetArtifactMetadataInput:
    out: BatchGetArtifactMetadataInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("artifactIds") is not None:
        import capo_securityagent.types.artifact_ids

        out["artifact_ids"] = capo_securityagent.types.artifact_ids.deserialize_json(
            data["artifactIds"]
        )
    else:
        out["artifact_ids"] = []
    return out
