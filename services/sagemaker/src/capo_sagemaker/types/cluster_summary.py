"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_image_version_status
    import capo_sagemaker.types.cluster_name
    import capo_sagemaker.types.cluster_status
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_plan_arns


class ClusterSummary(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.</p>"""
    cluster_name: NotRequired["capo_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name of the SageMaker HyperPod cluster.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the SageMaker HyperPod cluster is created.</p>"""
    cluster_status: NotRequired["capo_sagemaker.types.cluster_status.ClusterStatus"]
    """<p>The status of the SageMaker HyperPod cluster.</p>"""
    training_plan_arns: NotRequired[
        "capo_sagemaker.types.training_plan_arns.TrainingPlanArns"
    ]
    """<p>A list of Amazon Resource Names (ARNs) of the training plans associated with this cluster.</p> <p>For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html">CreateTrainingPlan</a> </code>.</p>"""
    image_version_status: NotRequired[
        "capo_sagemaker.types.cluster_image_version_status.ClusterImageVersionStatus"
    ]
    """<p>The aggregate status of the image version across the cluster's instance groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSummary) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "cluster_status" in value:
        import capo_sagemaker.types.cluster_status

        out["ClusterStatus"] = (
            capo_sagemaker.types.cluster_status.serialize_aws_json_1_1(
                value["cluster_status"]
            )
        )
    if "training_plan_arns" in value:
        import capo_sagemaker.types.training_plan_arns

        out["TrainingPlanArns"] = (
            capo_sagemaker.types.training_plan_arns.serialize_aws_json_1_1(
                value["training_plan_arns"]
            )
        )
    if "image_version_status" in value:
        import capo_sagemaker.types.cluster_image_version_status

        out["ImageVersionStatus"] = (
            capo_sagemaker.types.cluster_image_version_status.serialize_aws_json_1_1(
                value["image_version_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSummary:
    out: ClusterSummary = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("ClusterStatus") is not None:
        import capo_sagemaker.types.cluster_status

        out["cluster_status"] = (
            capo_sagemaker.types.cluster_status.deserialize_aws_json_1_1(
                data["ClusterStatus"]
            )
        )
    if data.get("TrainingPlanArns") is not None:
        import capo_sagemaker.types.training_plan_arns

        out["training_plan_arns"] = (
            capo_sagemaker.types.training_plan_arns.deserialize_aws_json_1_1(
                data["TrainingPlanArns"]
            )
        )
    if data.get("ImageVersionStatus") is not None:
        import capo_sagemaker.types.cluster_image_version_status

        out["image_version_status"] = (
            capo_sagemaker.types.cluster_image_version_status.deserialize_aws_json_1_1(
                data["ImageVersionStatus"]
            )
        )
    return out
