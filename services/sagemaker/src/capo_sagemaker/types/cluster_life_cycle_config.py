"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterLifeCycleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_life_cycle_config_file_name
    import capo_sagemaker.types.s3_uri


class ClusterLifeCycleConfig(TypedDict, closed=True):
    source_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>An Amazon S3 bucket path where your lifecycle scripts are stored.</p> <important> <p>Make sure that the S3 bucket path starts with <code>s3://sagemaker-</code>. The <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod">IAM role for SageMaker HyperPod</a> has the managed <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html"> <code>AmazonSageMakerClusterInstanceRolePolicy</code> </a> attached, which allows access to S3 buckets with the specific prefix <code>sagemaker-</code>.</p> </important>"""
    on_create: NotRequired[
        "capo_sagemaker.types.cluster_life_cycle_config_file_name.ClusterLifeCycleConfigFileName"
    ]
    """<p>The file name of the entrypoint script of lifecycle scripts under <code>SourceS3Uri</code>. This entrypoint script runs during cluster creation.</p>"""
    on_init_complete: NotRequired[
        "capo_sagemaker.types.cluster_life_cycle_config_file_name.ClusterLifeCycleConfigFileName"
    ]
    """<p>The file name of the entrypoint script of lifecycle scripts under <code>SourceS3Uri</code>. This script runs on the node after the AMI-based initialization is complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterLifeCycleConfig) -> dict:
    out: dict = {}
    if "source_s3_uri" in value:
        out["SourceS3Uri"] = value["source_s3_uri"]
    if "on_create" in value:
        out["OnCreate"] = value["on_create"]
    if "on_init_complete" in value:
        out["OnInitComplete"] = value["on_init_complete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterLifeCycleConfig:
    out: ClusterLifeCycleConfig = {}  # type: ignore[typeddict-item]
    if data.get("SourceS3Uri") is not None:
        out["source_s3_uri"] = data["SourceS3Uri"]
    if data.get("OnCreate") is not None:
        out["on_create"] = data["OnCreate"]
    if data.get("OnInitComplete") is not None:
        out["on_init_complete"] = data["OnInitComplete"]
    return out
