"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionNodeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_node_count


class ExtensionNodeSummary(TypedDict, closed=True):
    total_count: NotRequired[
        "capo_sagemaker.types.extension_node_count.ExtensionNodeCount"
    ]
    """<p>The number of nodes in your cluster that the extension targets. SageMaker HyperPod targets every running node in your cluster, including nodes that you add after you create the extension.</p>"""
    active_count: NotRequired[
        "capo_sagemaker.types.extension_node_count.ExtensionNodeCount"
    ]
    """<p>The number of nodes that are running the extension's current version and configuration. While SageMaker HyperPod creates or updates the extension, <code>ActiveCount</code> is lower than <code>TotalCount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionNodeSummary) -> dict:
    out: dict = {}
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    if "active_count" in value:
        out["ActiveCount"] = value["active_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtensionNodeSummary:
    out: ExtensionNodeSummary = {}  # type: ignore[typeddict-item]
    if data.get("TotalCount") is not None:
        out["total_count"] = data["TotalCount"]
    if data.get("ActiveCount") is not None:
        out["active_count"] = data["ActiveCount"]
    return out
