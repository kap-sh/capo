"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeArtifactDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.maximum_action_type_artifact_count
    import capo_codepipeline.types.minimum_action_type_artifact_count


class ActionTypeArtifactDetails(TypedDict, closed=True):
    minimum_count: "capo_codepipeline.types.minimum_action_type_artifact_count.MinimumActionTypeArtifactCount"
    """<p>The minimum number of artifacts that can be used with the action type. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of <code>source</code>.</p>"""
    maximum_count: "capo_codepipeline.types.maximum_action_type_artifact_count.MaximumActionTypeArtifactCount"
    """<p>The maximum number of artifacts that can be used with the actiontype. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of <code>source</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeArtifactDetails) -> dict:
    out: dict = {}
    out["minimumCount"] = value.get("minimum_count", 0)
    out["maximumCount"] = value.get("maximum_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeArtifactDetails:
    out: ActionTypeArtifactDetails = {}  # type: ignore[typeddict-item]
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
def serialize_cbor(value: ActionTypeArtifactDetails) -> dict:
    out: dict = {}
    out["minimumCount"] = value.get("minimum_count", 0)
    out["maximumCount"] = value.get("maximum_count", 0)
    return out


def deserialize_cbor(data: dict) -> ActionTypeArtifactDetails:
    out: ActionTypeArtifactDetails = {}  # type: ignore[typeddict-item]
    if data.get("minimumCount") is not None:
        out["minimum_count"] = data["minimumCount"]
    else:
        out["minimum_count"] = 0
    if data.get("maximumCount") is not None:
        out["maximum_count"] = data["maximumCount"]
    else:
        out["maximum_count"] = 0
    return out
