"""Generated from Smithy shape ``com.amazonaws.amplify#GetArtifactUrlResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.artifact_id
    import capo_amplify.types.artifact_url


class GetArtifactUrlResult(TypedDict, closed=True):
    artifact_id: "capo_amplify.types.artifact_id.ArtifactId"
    """<p>The unique ID for an artifact. </p>"""
    artifact_url: "capo_amplify.types.artifact_url.ArtifactUrl"
    """<p>The presigned URL for the artifact. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArtifactUrlResult) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    out["artifactUrl"] = value["artifact_url"]
    return out


def deserialize_json(data: dict) -> GetArtifactUrlResult:
    out: GetArtifactUrlResult = {}  # type: ignore[typeddict-item]
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    else:
        out["artifact_id"] = ""
    if data.get("artifactUrl") is not None:
        out["artifact_url"] = data["artifactUrl"]
    else:
        out["artifact_url"] = ""
    return out
