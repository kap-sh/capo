"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.maximum_artifact_count
    import capo_codepipeline.types.minimum_artifact_count


class ArtifactDetails(TypedDict, closed=True):
    minimum_count: "capo_codepipeline.types.minimum_artifact_count.MinimumArtifactCount"
    """<p>The minimum number of artifacts allowed for the action type.</p>"""
    maximum_count: "capo_codepipeline.types.maximum_artifact_count.MaximumArtifactCount"
    """<p>The maximum number of artifacts allowed for the action type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactDetails) -> dict:
    out: dict = {}
    out["minimumCount"] = value.get("minimum_count", 0)
    out["maximumCount"] = value.get("maximum_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactDetails:
    out: ArtifactDetails = {}  # type: ignore[typeddict-item]
    if data.get("minimumCount") is not None:
        out["minimum_count"] = data["minimumCount"]
    else:
        out["minimum_count"] = 0
    if data.get("maximumCount") is not None:
        out["maximum_count"] = data["maximumCount"]
    else:
        out["maximum_count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactDetails) -> dict:
    out: dict = {}
    out["minimumCount"] = value.get("minimum_count", 0)
    out["maximumCount"] = value.get("maximum_count", 0)
    return out


def deserialize_cbor(data: dict) -> ArtifactDetails:
    out: ArtifactDetails = {}  # type: ignore[typeddict-item]
    if data.get("minimumCount") is not None:
        out["minimum_count"] = data["minimumCount"]
    else:
        out["minimum_count"] = 0
    if data.get("maximumCount") is not None:
        out["maximum_count"] = data["maximumCount"]
    else:
        out["maximum_count"] = 0
    return out
