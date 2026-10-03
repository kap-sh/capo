"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_instance_type
    import capo_sagemaker.types.image_arn
    import capo_sagemaker.types.image_version_alias
    import capo_sagemaker.types.image_version_arn
    import capo_sagemaker.types.studio_lifecycle_config_arn
    import capo_sagemaker.types.studio_resource_spec_training_plan_arn


class ResourceSpec(TypedDict, closed=True):
    sage_maker_image_arn: NotRequired["capo_sagemaker.types.image_arn.ImageArn"]
    """<p>The ARN of the SageMaker AI image that the image version belongs to.</p>"""
    sage_maker_image_version_arn: NotRequired[
        "capo_sagemaker.types.image_version_arn.ImageVersionArn"
    ]
    """<p>The ARN of the image version created on the instance. To clear the value set for <code>SageMakerImageVersionArn</code>, pass <code>None</code> as the value.</p>"""
    sage_maker_image_version_alias: NotRequired[
        "capo_sagemaker.types.image_version_alias.ImageVersionAlias"
    ]
    """<p>The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.</p>"""
    instance_type: NotRequired["capo_sagemaker.types.app_instance_type.AppInstanceType"]
    """<p>The instance type that the image version runs on.</p> <note> <p> <b>JupyterServer apps</b> only support the <code>system</code> value.</p> <p>For <b>KernelGateway apps</b>, the <code>system</code> value is translated to <code>ml.t3.medium</code>. KernelGateway apps also support all other values for available instance types.</p> </note>"""
    lifecycle_config_arn: NotRequired[
        "capo_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.</p>"""
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.studio_resource_spec_training_plan_arn.StudioResourceSpecTrainingPlanArn"
    ]
    """<p>The ARN of the SageMaker AI Training Plan to use for this app. When you specify a training plan, the app launches on reserved GPU capacity. This field is supported for JupyterLab and CodeEditor app types.</p> <p>For more information about how to reserve GPU capacity with SageMaker AI Training Plans, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-utilization-for-studio-apps.html">Using training plans in Studio applications</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSpec) -> dict:
    out: dict = {}
    if "sage_maker_image_arn" in value:
        out["SageMakerImageArn"] = value["sage_maker_image_arn"]
    if "sage_maker_image_version_arn" in value:
        out["SageMakerImageVersionArn"] = value["sage_maker_image_version_arn"]
    if "sage_maker_image_version_alias" in value:
        out["SageMakerImageVersionAlias"] = value["sage_maker_image_version_alias"]
    if "instance_type" in value:
        import capo_sagemaker.types.app_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.app_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "lifecycle_config_arn" in value:
        out["LifecycleConfigArn"] = value["lifecycle_config_arn"]
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceSpec:
    out: ResourceSpec = {}  # type: ignore[typeddict-item]
    if data.get("SageMakerImageArn") is not None:
        out["sage_maker_image_arn"] = data["SageMakerImageArn"]
    if data.get("SageMakerImageVersionArn") is not None:
        out["sage_maker_image_version_arn"] = data["SageMakerImageVersionArn"]
    if data.get("SageMakerImageVersionAlias") is not None:
        out["sage_maker_image_version_alias"] = data["SageMakerImageVersionAlias"]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.app_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.app_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("LifecycleConfigArn") is not None:
        out["lifecycle_config_arn"] = data["LifecycleConfigArn"]
    if data.get("TrainingPlanArn") is not None:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    return out
