"""Generated from Smithy shape ``com.amazonaws.securityagent#AddArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_id


class AddArtifactOutput(TypedDict, closed=True):
    artifact_id: "capo_securityagent.types.artifact_id.ArtifactId"
    """<p>The unique identifier assigned to the uploaded artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddArtifactOutput) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    return out


def deserialize_json(data: dict) -> AddArtifactOutput:
    out: AddArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    else:
        out["artifact_id"] = ""
    return out
