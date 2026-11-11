"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterExtensionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_details
    import capo_sagemaker.types.extension_node_summary


class DescribeClusterExtensionResponse(TypedDict, closed=True):
    extension_details: NotRequired[
        "capo_sagemaker.types.extension_details.ExtensionDetails"
    ]
    """<p>The details of the extension.</p>"""
    node_summary: NotRequired[
        "capo_sagemaker.types.extension_node_summary.ExtensionNodeSummary"
    ]
    """<p>A summary of how many nodes in your cluster the extension targets, and how many of them run the extension's current version and configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterExtensionResponse) -> dict:
    out: dict = {}
    if "extension_details" in value:
        import capo_sagemaker.types.extension_details

        out["ExtensionDetails"] = (
            capo_sagemaker.types.extension_details.serialize_aws_json_1_1(
                value["extension_details"]
            )
        )
    if "node_summary" in value:
        import capo_sagemaker.types.extension_node_summary

        out["NodeSummary"] = (
            capo_sagemaker.types.extension_node_summary.serialize_aws_json_1_1(
                value["node_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterExtensionResponse:
    out: DescribeClusterExtensionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionDetails") is not None:
        import capo_sagemaker.types.extension_details

        out["extension_details"] = (
            capo_sagemaker.types.extension_details.deserialize_aws_json_1_1(
                data["ExtensionDetails"]
            )
        )
    if data.get("NodeSummary") is not None:
        import capo_sagemaker.types.extension_node_summary

        out["node_summary"] = (
            capo_sagemaker.types.extension_node_summary.deserialize_aws_json_1_1(
                data["NodeSummary"]
            )
        )
    return out
