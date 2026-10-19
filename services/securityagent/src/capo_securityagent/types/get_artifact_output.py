"""Generated from Smithy shape ``com.amazonaws.securityagent#GetArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.artifact
    import capo_securityagent.types.artifact_id


class GetArtifactOutput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space that contains the artifact.</p>"""
    artifact_id: "capo_securityagent.types.artifact_id.ArtifactId"
    """<p>The unique identifier of the artifact.</p>"""
    artifact: "capo_securityagent.types.artifact.Artifact"
    """<p>The artifact content and type.</p>"""
    file_name: "str"
    """<p>The file name of the artifact.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time the artifact was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArtifactOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["artifactId"] = value["artifact_id"]
    import capo_securityagent.types.artifact

    out["artifact"] = capo_securityagent.types.artifact.serialize_json(
        value["artifact"]
    )
    out["fileName"] = value["file_name"]
    import capo_securityagent._protocol.serialize

    out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetArtifactOutput:
    out: GetArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    else:
        out["artifact_id"] = ""
    if data.get("artifact") is not None:
        import capo_securityagent.types.artifact

        out["artifact"] = capo_securityagent.types.artifact.deserialize_json(
            data["artifact"]
        )
    else:
        raise DeserializationError("GetArtifactOutput.artifact required")
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
