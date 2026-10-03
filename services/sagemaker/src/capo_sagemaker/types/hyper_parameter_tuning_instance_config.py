"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningInstanceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_instance_count
    import capo_sagemaker.types.training_instance_type
    import capo_sagemaker.types.volume_size_in_gb


class HyperParameterTuningInstanceConfig(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.training_instance_type.TrainingInstanceType"
    ]
    """<p>The instance type used for processing of hyperparameter optimization jobs. Choose from general purpose (no GPUs) instance types: ml.m5.xlarge, ml.m5.2xlarge, and ml.m5.4xlarge or compute optimized (no GPUs) instance types: ml.c5.xlarge and ml.c5.2xlarge. For more information about instance types, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html">instance type descriptions</a>.</p>"""
    instance_count: NotRequired[
        "capo_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>The number of instances of the type specified by <code>InstanceType</code>. Choose an instance count larger than 1 for distributed training algorithms. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html">Step 2: Launch a SageMaker Distributed Training Job Using the SageMaker Python SDK</a> for more information.</p>"""
    volume_size_in_gb: NotRequired[
        "capo_sagemaker.types.volume_size_in_gb.VolumeSizeInGB"
    ]
    """<p>The volume size in GB of the data to be processed for hyperparameter optimization (optional).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningInstanceConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.training_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.training_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningInstanceConfig:
    out: HyperParameterTuningInstanceConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.training_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("VolumeSizeInGB") is not None:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    return out
