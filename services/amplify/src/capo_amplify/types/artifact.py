"""Generated from Smithy shape ``com.amazonaws.amplify#Artifact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.artifact_file_name
    import capo_amplify.types.artifact_id


class Artifact(TypedDict, closed=True):
    artifact_file_name: "capo_amplify.types.artifact_file_name.ArtifactFileName"
    """<p>The file name for the artifact. </p>"""
    artifact_id: "capo_amplify.types.artifact_id.ArtifactId"
    """<p>The unique ID for the artifact. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Artifact) -> dict:
    out: dict = {}
    out["artifactFileName"] = value["artifact_file_name"]
    out["artifactId"] = value["artifact_id"]
    return out


def deserialize_json(data: dict) -> Artifact:
    out: Artifact = {}  # type: ignore[typeddict-item]
    if data.get("artifactFileName") is not None:
        out["artifact_file_name"] = data["artifactFileName"]
    else:
        out["artifact_file_name"] = ""
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    else:
        out["artifact_id"] = ""
    return out
