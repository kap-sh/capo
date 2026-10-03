"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTrainingJobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.checkpoint_config
    import capo_sagemaker.types.hyper_parameter_algorithm_specification
    import capo_sagemaker.types.hyper_parameter_training_job_definition_name
    import capo_sagemaker.types.hyper_parameter_training_job_environment_map
    import capo_sagemaker.types.hyper_parameter_tuning_job_objective
    import capo_sagemaker.types.hyper_parameter_tuning_resource_config
    import capo_sagemaker.types.hyper_parameters
    import capo_sagemaker.types.input_data_config
    import capo_sagemaker.types.output_data_config
    import capo_sagemaker.types.parameter_ranges
    import capo_sagemaker.types.resource_config
    import capo_sagemaker.types.retry_strategy
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.stopping_condition
    import capo_sagemaker.types.vpc_config


class HyperParameterTrainingJobDefinition(TypedDict, closed=True):
    definition_name: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_definition_name.HyperParameterTrainingJobDefinitionName"
    ]
    """<p>The job definition name.</p>"""
    tuning_objective: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_objective.HyperParameterTuningJobObjective"
    ]
    hyper_parameter_ranges: NotRequired[
        "capo_sagemaker.types.parameter_ranges.ParameterRanges"
    ]
    static_hyper_parameters: NotRequired[
        "capo_sagemaker.types.hyper_parameters.HyperParameters"
    ]
    """<p>Specifies the values of hyperparameters that do not change for the tuning job.</p>"""
    algorithm_specification: NotRequired[
        "capo_sagemaker.types.hyper_parameter_algorithm_specification.HyperParameterAlgorithmSpecification"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html">HyperParameterAlgorithmSpecification</a> object that specifies the resource algorithm to use for the training jobs that the tuning job launches.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.</p>"""
    input_data_config: NotRequired[
        "capo_sagemaker.types.input_data_config.InputDataConfig"
    ]
    """<p>An array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html">Channel</a> objects that specify the input for the training jobs that the tuning job launches.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>The <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html">VpcConfig</a> object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html">Protect Training Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    output_data_config: NotRequired[
        "capo_sagemaker.types.output_data_config.OutputDataConfig"
    ]
    """<p>Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.</p>"""
    resource_config: NotRequired["capo_sagemaker.types.resource_config.ResourceConfig"]
    """<p>The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.</p> <p>Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want SageMaker to use the storage volume to store the training data, choose <code>File</code> as the <code>TrainingInputMode</code> in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.</p> <note> <p>If you want to use hyperparameter optimization with instance type flexibility, use <code>HyperParameterTuningResourceConfig</code> instead.</p> </note>"""
    hyper_parameter_tuning_resource_config: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_resource_config.HyperParameterTuningResourceConfig"
    ]
    """<p>The configuration for the hyperparameter tuning resources, including the compute instances and storage volumes, used for training jobs launched by the tuning job. By default, storage volumes hold model artifacts and incremental states. Choose <code>File</code> for <code>TrainingInputMode</code> in the <code>AlgorithmSpecification</code> parameter to additionally store training data in the storage volume (optional).</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model hyperparameter training job can run. It also specifies how long a managed spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.</p>"""
    enable_network_isolation: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.</p>"""
    enable_inter_container_traffic_encryption: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>To encrypt all communications between ML compute instances in distributed training, choose <code>True</code>. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.</p>"""
    enable_managed_spot_training: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>A Boolean indicating whether managed spot training is enabled (<code>True</code>) or not (<code>False</code>).</p>"""
    checkpoint_config: NotRequired[
        "capo_sagemaker.types.checkpoint_config.CheckpointConfig"
    ]
    retry_strategy: NotRequired["capo_sagemaker.types.retry_strategy.RetryStrategy"]
    """<p>The number of times to retry the job when the job fails due to an <code>InternalServerError</code>.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_environment_map.HyperParameterTrainingJobEnvironmentMap"
    ]
    """<p>An environment variable that you can pass into the SageMaker <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html">CreateTrainingJob</a> API. You can use an existing <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-Environment">environment variable from the training container</a> or use your own. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html">Define metrics and variables</a> for more information.</p> <note> <p>The maximum number of items specified for <code>Map Entries</code> refers to the maximum number of environment variables for each <code>TrainingJobDefinition</code> and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of environment variables for all the training job definitions can't exceed the maximum number specified.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTrainingJobDefinition) -> dict:
    out: dict = {}
    if "definition_name" in value:
        out["DefinitionName"] = value["definition_name"]
    if "tuning_objective" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_objective

        out["TuningObjective"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_objective.serialize_aws_json_1_1(
                value["tuning_objective"]
            )
        )
    if "hyper_parameter_ranges" in value:
        import capo_sagemaker.types.parameter_ranges

        out["HyperParameterRanges"] = (
            capo_sagemaker.types.parameter_ranges.serialize_aws_json_1_1(
                value["hyper_parameter_ranges"]
            )
        )
    if "static_hyper_parameters" in value:
        import capo_sagemaker.types.hyper_parameters

        out["StaticHyperParameters"] = (
            capo_sagemaker.types.hyper_parameters.serialize_aws_json_1_1(
                value["static_hyper_parameters"]
            )
        )
    if "algorithm_specification" in value:
        import capo_sagemaker.types.hyper_parameter_algorithm_specification

        out["AlgorithmSpecification"] = (
            capo_sagemaker.types.hyper_parameter_algorithm_specification.serialize_aws_json_1_1(
                value["algorithm_specification"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "input_data_config" in value:
        import capo_sagemaker.types.input_data_config

        out["InputDataConfig"] = (
            capo_sagemaker.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "output_data_config" in value:
        import capo_sagemaker.types.output_data_config

        out["OutputDataConfig"] = (
            capo_sagemaker.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "resource_config" in value:
        import capo_sagemaker.types.resource_config

        out["ResourceConfig"] = (
            capo_sagemaker.types.resource_config.serialize_aws_json_1_1(
                value["resource_config"]
            )
        )
    if "hyper_parameter_tuning_resource_config" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_resource_config

        out["HyperParameterTuningResourceConfig"] = (
            capo_sagemaker.types.hyper_parameter_tuning_resource_config.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_resource_config"]
            )
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    if "enable_inter_container_traffic_encryption" in value:
        out["EnableInterContainerTrafficEncryption"] = value[
            "enable_inter_container_traffic_encryption"
        ]
    if "enable_managed_spot_training" in value:
        out["EnableManagedSpotTraining"] = value["enable_managed_spot_training"]
    if "checkpoint_config" in value:
        import capo_sagemaker.types.checkpoint_config

        out["CheckpointConfig"] = (
            capo_sagemaker.types.checkpoint_config.serialize_aws_json_1_1(
                value["checkpoint_config"]
            )
        )
    if "retry_strategy" in value:
        import capo_sagemaker.types.retry_strategy

        out["RetryStrategy"] = (
            capo_sagemaker.types.retry_strategy.serialize_aws_json_1_1(
                value["retry_strategy"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.hyper_parameter_training_job_environment_map

        out["Environment"] = (
            capo_sagemaker.types.hyper_parameter_training_job_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTrainingJobDefinition:
    out: HyperParameterTrainingJobDefinition = {}  # type: ignore[typeddict-item]
    if data.get("DefinitionName") is not None:
        out["definition_name"] = data["DefinitionName"]
    if data.get("TuningObjective") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_objective

        out["tuning_objective"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_objective.deserialize_aws_json_1_1(
                data["TuningObjective"]
            )
        )
    if data.get("HyperParameterRanges") is not None:
        import capo_sagemaker.types.parameter_ranges

        out["hyper_parameter_ranges"] = (
            capo_sagemaker.types.parameter_ranges.deserialize_aws_json_1_1(
                data["HyperParameterRanges"]
            )
        )
    if data.get("StaticHyperParameters") is not None:
        import capo_sagemaker.types.hyper_parameters

        out["static_hyper_parameters"] = (
            capo_sagemaker.types.hyper_parameters.deserialize_aws_json_1_1(
                data["StaticHyperParameters"]
            )
        )
    if data.get("AlgorithmSpecification") is not None:
        import capo_sagemaker.types.hyper_parameter_algorithm_specification

        out["algorithm_specification"] = (
            capo_sagemaker.types.hyper_parameter_algorithm_specification.deserialize_aws_json_1_1(
                data["AlgorithmSpecification"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("InputDataConfig") is not None:
        import capo_sagemaker.types.input_data_config

        out["input_data_config"] = (
            capo_sagemaker.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("OutputDataConfig") is not None:
        import capo_sagemaker.types.output_data_config

        out["output_data_config"] = (
            capo_sagemaker.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("ResourceConfig") is not None:
        import capo_sagemaker.types.resource_config

        out["resource_config"] = (
            capo_sagemaker.types.resource_config.deserialize_aws_json_1_1(
                data["ResourceConfig"]
            )
        )
    if data.get("HyperParameterTuningResourceConfig") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_resource_config

        out["hyper_parameter_tuning_resource_config"] = (
            capo_sagemaker.types.hyper_parameter_tuning_resource_config.deserialize_aws_json_1_1(
                data["HyperParameterTuningResourceConfig"]
            )
        )
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("EnableNetworkIsolation") is not None:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    if data.get("EnableInterContainerTrafficEncryption") is not None:
        out["enable_inter_container_traffic_encryption"] = data[
            "EnableInterContainerTrafficEncryption"
        ]
    if data.get("EnableManagedSpotTraining") is not None:
        out["enable_managed_spot_training"] = data["EnableManagedSpotTraining"]
    if data.get("CheckpointConfig") is not None:
        import capo_sagemaker.types.checkpoint_config

        out["checkpoint_config"] = (
            capo_sagemaker.types.checkpoint_config.deserialize_aws_json_1_1(
                data["CheckpointConfig"]
            )
        )
    if data.get("RetryStrategy") is not None:
        import capo_sagemaker.types.retry_strategy

        out["retry_strategy"] = (
            capo_sagemaker.types.retry_strategy.deserialize_aws_json_1_1(
                data["RetryStrategy"]
            )
        )
    if data.get("Environment") is not None:
        import capo_sagemaker.types.hyper_parameter_training_job_environment_map

        out["environment"] = (
            capo_sagemaker.types.hyper_parameter_training_job_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
