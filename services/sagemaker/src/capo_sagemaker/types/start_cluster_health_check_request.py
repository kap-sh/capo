"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartClusterHealthCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.deep_health_check_configurations


class StartClusterHealthCheckRequest(TypedDict, closed=True):
    cluster_name: "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    """<p>The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.</p>"""
    deep_health_check_configurations: "capo_sagemaker.types.deep_health_check_configurations.DeepHealthCheckConfigurations"
    """<p>A list of configurations containing instance group names, EC2 instance IDs, and deep health checks to perform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartClusterHealthCheckRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    import capo_sagemaker.types.deep_health_check_configurations

    out["DeepHealthCheckConfigurations"] = (
        capo_sagemaker.types.deep_health_check_configurations.serialize_aws_json_1_1(
            value["deep_health_check_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartClusterHealthCheckRequest:
    out: StartClusterHealthCheckRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("DeepHealthCheckConfigurations") is not None:
        import capo_sagemaker.types.deep_health_check_configurations

        out["deep_health_check_configurations"] = (
            capo_sagemaker.types.deep_health_check_configurations.deserialize_aws_json_1_1(
                data["DeepHealthCheckConfigurations"]
            )
        )
    else:
        out["deep_health_check_configurations"] = []
    return out
