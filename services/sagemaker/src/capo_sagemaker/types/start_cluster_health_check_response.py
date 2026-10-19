"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartClusterHealthCheckResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn


class StartClusterHealthCheckResponse(TypedDict, closed=True):
    cluster_arn: "capo_sagemaker.types.cluster_arn.ClusterArn"
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the deep health checks were initiated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartClusterHealthCheckResponse) -> dict:
    out: dict = {}
    out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartClusterHealthCheckResponse:
    out: StartClusterHealthCheckResponse = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    else:
        out["cluster_arn"] = ""
    return out
