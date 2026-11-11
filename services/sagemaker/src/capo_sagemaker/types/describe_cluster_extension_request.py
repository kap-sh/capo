"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.extension_arn


class DescribeClusterExtensionRequest(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.</p>"""
    extension_arn: NotRequired["capo_sagemaker.types.extension_arn.ExtensionArn"]
    """<p>The Amazon Resource Name (ARN) of the extension to describe. <code>CreateClusterExtension</code> returns this ARN, and <code>ListClusterExtensions</code> lists it. If you delete an extension and create it again, the new extension has a new ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterExtensionRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterExtensionRequest:
    out: DescribeClusterExtensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ExtensionArn") is not None:
        out["extension_arn"] = data["ExtensionArn"]
    return out
