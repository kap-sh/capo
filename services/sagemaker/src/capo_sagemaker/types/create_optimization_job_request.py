"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateOptimizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.optimization_configs
    import capo_sagemaker.types.optimization_job_deployment_instance_type
    import capo_sagemaker.types.optimization_job_environment_variables
    import capo_sagemaker.types.optimization_job_max_instance_count
    import capo_sagemaker.types.optimization_job_model_source
    import capo_sagemaker.types.optimization_job_output_config
    import capo_sagemaker.types.optimization_job_training_plan_arns
    import capo_sagemaker.types.optimization_vpc_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.stopping_condition
    import capo_sagemaker.types.tag_list


class CreateOptimizationJobRequest(TypedDict, closed=True):
    optimization_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>A custom name for the new optimization job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf. </p> <p>During model optimization, Amazon SageMaker AI needs your permission to:</p> <ul> <li> <p>Read input data from an S3 bucket</p> </li> <li> <p>Write model artifacts to an S3 bucket</p> </li> <li> <p>Write logs to Amazon CloudWatch Logs</p> </li> <li> <p>Publish metrics to Amazon CloudWatch</p> </li> </ul> <p>You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the <code>iam:PassRole</code> permission. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html">Amazon SageMaker AI Roles.</a> </p>"""
    model_source: NotRequired[
        "capo_sagemaker.types.optimization_job_model_source.OptimizationJobModelSource"
    ]
    """<p>The location of the source model to optimize with an optimization job.</p>"""
    deployment_instance_type: NotRequired[
        "capo_sagemaker.types.optimization_job_deployment_instance_type.OptimizationJobDeploymentInstanceType"
    ]
    """<p>The type of instance that hosts the optimized model that you create with the optimization job.</p>"""
    max_instance_count: NotRequired[
        "capo_sagemaker.types.optimization_job_max_instance_count.OptimizationJobMaxInstanceCount"
    ]
    """<p>The maximum number of instances to use for the optimization job.</p>"""
    optimization_environment: NotRequired[
        "capo_sagemaker.types.optimization_job_environment_variables.OptimizationJobEnvironmentVariables"
    ]
    """<p>The environment variables to set in the model container.</p>"""
    optimization_configs: NotRequired[
        "capo_sagemaker.types.optimization_configs.OptimizationConfigs"
    ]
    """<p>Settings for each of the optimization techniques that the job applies.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.optimization_job_output_config.OptimizationJobOutputConfig"
    ]
    """<p>Details for where to store the optimized model that you create with the optimization job.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of key-value pairs associated with the optimization job. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    vpc_config: NotRequired[
        "capo_sagemaker.types.optimization_vpc_config.OptimizationVpcConfig"
    ]
    """<p>A VPC in Amazon VPC that your optimized model has access to.</p>"""
    training_plan_arns: NotRequired[
        "capo_sagemaker.types.optimization_job_training_plan_arns.OptimizationJobTrainingPlanArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the training plan to use for this optimization job.</p> <p>When you use reserved capacity from a training plan, the optimization job runs on that reserved capacity instead of on-demand capacity. If you omit this field, the job uses on-demand capacity. You can specify at most one training plan.</p> <p>For more information about how to reserve GPU capacity for your optimization jobs using Amazon SageMaker Training Plans, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html">Reserve capacity with training plans</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOptimizationJobRequest) -> dict:
    out: dict = {}
    if "optimization_job_name" in value:
        out["OptimizationJobName"] = value["optimization_job_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "model_source" in value:
        import capo_sagemaker.types.optimization_job_model_source

        out["ModelSource"] = (
            capo_sagemaker.types.optimization_job_model_source.serialize_aws_json_1_1(
                value["model_source"]
            )
        )
    if "deployment_instance_type" in value:
        import capo_sagemaker.types.optimization_job_deployment_instance_type

        out["DeploymentInstanceType"] = (
            capo_sagemaker.types.optimization_job_deployment_instance_type.serialize_aws_json_1_1(
                value["deployment_instance_type"]
            )
        )
    if "max_instance_count" in value:
        out["MaxInstanceCount"] = value["max_instance_count"]
    if "optimization_environment" in value:
        import capo_sagemaker.types.optimization_job_environment_variables

        out["OptimizationEnvironment"] = (
            capo_sagemaker.types.optimization_job_environment_variables.serialize_aws_json_1_1(
                value["optimization_environment"]
            )
        )
    if "optimization_configs" in value:
        import capo_sagemaker.types.optimization_configs

        out["OptimizationConfigs"] = (
            capo_sagemaker.types.optimization_configs.serialize_aws_json_1_1(
                value["optimization_configs"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.optimization_job_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.optimization_job_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.optimization_vpc_config

        out["VpcConfig"] = (
            capo_sagemaker.types.optimization_vpc_config.serialize_aws_json_1_1(
                value["vpc_config"]
            )
        )
    if "training_plan_arns" in value:
        import capo_sagemaker.types.optimization_job_training_plan_arns

        out["TrainingPlanArns"] = (
            capo_sagemaker.types.optimization_job_training_plan_arns.serialize_aws_json_1_1(
                value["training_plan_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOptimizationJobRequest:
    out: CreateOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("OptimizationJobName") is not None:
        out["optimization_job_name"] = data["OptimizationJobName"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ModelSource") is not None:
        import capo_sagemaker.types.optimization_job_model_source

        out["model_source"] = (
            capo_sagemaker.types.optimization_job_model_source.deserialize_aws_json_1_1(
                data["ModelSource"]
            )
        )
    if data.get("DeploymentInstanceType") is not None:
        import capo_sagemaker.types.optimization_job_deployment_instance_type

        out["deployment_instance_type"] = (
            capo_sagemaker.types.optimization_job_deployment_instance_type.deserialize_aws_json_1_1(
                data["DeploymentInstanceType"]
            )
        )
    if data.get("MaxInstanceCount") is not None:
        out["max_instance_count"] = data["MaxInstanceCount"]
    if data.get("OptimizationEnvironment") is not None:
        import capo_sagemaker.types.optimization_job_environment_variables

        out["optimization_environment"] = (
            capo_sagemaker.types.optimization_job_environment_variables.deserialize_aws_json_1_1(
                data["OptimizationEnvironment"]
            )
        )
    if data.get("OptimizationConfigs") is not None:
        import capo_sagemaker.types.optimization_configs

        out["optimization_configs"] = (
            capo_sagemaker.types.optimization_configs.deserialize_aws_json_1_1(
                data["OptimizationConfigs"]
            )
        )
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.optimization_job_output_config

        out["output_config"] = (
            capo_sagemaker.types.optimization_job_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.optimization_vpc_config

        out["vpc_config"] = (
            capo_sagemaker.types.optimization_vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    if data.get("TrainingPlanArns") is not None:
        import capo_sagemaker.types.optimization_job_training_plan_arns

        out["training_plan_arns"] = (
            capo_sagemaker.types.optimization_job_training_plan_arns.deserialize_aws_json_1_1(
                data["TrainingPlanArns"]
            )
        )
    return out
