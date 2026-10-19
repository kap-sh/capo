"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_id
    import capo_securityagent.types.artifact_type


class ArtifactSummary(TypedDict, closed=True):
    artifact_id: "capo_securityagent.types.artifact_id.ArtifactId"
    """<p>The unique identifier of the artifact.</p>"""
    file_name: "str"
    """<p>The file name of the artifact.</p>"""
    artifact_type: "capo_securityagent.types.artifact_type.ArtifactType"
    """<p>The file type of the artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactSummary) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    out["fileName"] = value["file_name"]
    import capo_securityagent.types.artifact_type

    out["artifactType"] = capo_securityagent.types.artifact_type.serialize_json(
        value["artifact_type"]
    )
    return out


def deserialize_json(data: dict) -> ArtifactSummary:
    out: ArtifactSummary = {}  # type: ignore[typeddict-item]
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    else:
        out["artifact_id"] = ""
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
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
    return out
