"""Generated from Smithy shape ``com.amazonaws.securityagent#AddArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.artifact_type


class AddArtifactInput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to add the artifact to.</p>"""
    artifact_content: "bytes"
    """<p>The binary content of the artifact to upload.</p>"""
    artifact_type: "capo_securityagent.types.artifact_type.ArtifactType"
    """<p>The file type of the artifact. Valid values include TXT, PNG, JPEG, MD, PDF, DOCX, DOC, JSON, and YAML.</p>"""
    file_name: "str"
    """<p>The file name of the artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddArtifactInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_securityagent.types._prelude.blob

    out["artifactContent"] = capo_securityagent.types._prelude.blob.serialize_json(
        value["artifact_content"]
    )
    import capo_securityagent.types.artifact_type

    out["artifactType"] = capo_securityagent.types.artifact_type.serialize_json(
        value["artifact_type"]
    )
    out["fileName"] = value["file_name"]
    return out


def deserialize_json(data: dict) -> AddArtifactInput:
    out: AddArtifactInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("artifactContent") is not None:
        import capo_securityagent.types._prelude.blob

        out["artifact_content"] = (
            capo_securityagent.types._prelude.blob.deserialize_json(
                data["artifactContent"]
            )
        )
    else:
        out["artifact_content"] = b""
    if data.get("artifactType") is not None:
        import capo_securityagent.types.artifact_type

        out["artifact_type"] = capo_securityagent.types.artifact_type.deserialize_json(
            data["artifactType"]
        )
    else:
        import typing

        out["artifact_type"] = typing.cast(
            "capo_securityagent.types.artifact_type.ArtifactType", ""
        )
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    return out
