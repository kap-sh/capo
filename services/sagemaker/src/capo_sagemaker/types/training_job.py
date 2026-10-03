"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_specification
    import capo_sagemaker.types.auto_ml_job_arn
    import capo_sagemaker.types.billable_time_in_seconds
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.checkpoint_config
    import capo_sagemaker.types.debug_hook_config
    import capo_sagemaker.types.debug_rule_configurations
    import capo_sagemaker.types.debug_rule_evaluation_statuses
    import capo_sagemaker.types.experiment_config
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.final_metric_data_list
    import capo_sagemaker.types.hyper_parameter_tuning_job_arn
    import capo_sagemaker.types.hyper_parameters
    import capo_sagemaker.types.input_data_config
    import capo_sagemaker.types.labeling_job_arn
    import capo_sagemaker.types.model_artifacts
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.model_package_config
    import capo_sagemaker.types.output_data_config
    import capo_sagemaker.types.profiler_config
    import capo_sagemaker.types.resource_config
    import capo_sagemaker.types.retry_strategy
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.secondary_status
    import capo_sagemaker.types.secondary_status_transitions
    import capo_sagemaker.types.stopping_condition
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.tensor_board_output_config
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_environment_map
    import capo_sagemaker.types.training_job_arn
    import capo_sagemaker.types.training_job_name
    import capo_sagemaker.types.training_job_status
    import capo_sagemaker.types.training_time_in_seconds
    import capo_sagemaker.types.vpc_config
    import capo_sagemaker.types.warm_pool_status


class TrainingJob(TypedDict, closed=True):
    training_job_name: NotRequired[
        "capo_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the training job.</p>"""
    training_job_arn: NotRequired[
        "capo_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training job.</p>"""
    tuning_job_arn: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.</p>"""
    labeling_job_arn: NotRequired[
        "capo_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the labeling job.</p>"""
    auto_ml_job_arn: NotRequired["capo_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    model_artifacts: NotRequired["capo_sagemaker.types.model_artifacts.ModelArtifacts"]
    """<p>Information about the Amazon S3 location that is configured for storing model artifacts.</p>"""
    training_job_status: NotRequired[
        "capo_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>The status of the training job.</p> <p>Training job statuses are:</p> <ul> <li> <p> <code>InProgress</code> - The training is in progress.</p> </li> <li> <p> <code>Completed</code> - The training job has completed.</p> </li> <li> <p> <code>Failed</code> - The training job has failed. To see the reason for the failure, see the <code>FailureReason</code> field in the response to a <code>DescribeTrainingJobResponse</code> call.</p> </li> <li> <p> <code>Stopping</code> - The training job is stopping.</p> </li> <li> <p> <code>Stopped</code> - The training job has stopped.</p> </li> </ul> <p>For more detailed information, see <code>SecondaryStatus</code>. </p>"""
    secondary_status: NotRequired[
        "capo_sagemaker.types.secondary_status.SecondaryStatus"
    ]
    """<p> Provides detailed information about the state of the training job. For detailed information about the secondary status of the training job, see <code>StatusMessage</code> under <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html">SecondaryStatusTransition</a>.</p> <p>SageMaker provides primary statuses and secondary statuses that apply to each of them:</p> <dl> <dt>InProgress</dt> <dd> <ul> <li> <p> <code>Starting</code> - Starting the training job.</p> </li> <li> <p> <code>Downloading</code> - An optional stage for algorithms that support <code>File</code> training input mode. It indicates that data is being downloaded to the ML storage volumes.</p> </li> <li> <p> <code>Training</code> - Training is in progress.</p> </li> <li> <p> <code>Uploading</code> - Training is complete and the model artifacts are being uploaded to the S3 location.</p> </li> </ul> </dd> <dt>Completed</dt> <dd> <ul> <li> <p> <code>Completed</code> - The training job has completed.</p> </li> </ul> </dd> <dt>Failed</dt> <dd> <ul> <li> <p> <code>Failed</code> - The training job has failed. The reason for the failure is returned in the <code>FailureReason</code> field of <code>DescribeTrainingJobResponse</code>.</p> </li> </ul> </dd> <dt>Stopped</dt> <dd> <ul> <li> <p> <code>MaxRuntimeExceeded</code> - The job stopped because it exceeded the maximum allowed runtime.</p> </li> <li> <p> <code>Stopped</code> - The training job has stopped.</p> </li> </ul> </dd> <dt>Stopping</dt> <dd> <ul> <li> <p> <code>Stopping</code> - Stopping the training job.</p> </li> </ul> </dd> </dl> <important> <p>Valid values for <code>SecondaryStatus</code> are subject to change. </p> </important> <p>We no longer support the following secondary statuses:</p> <ul> <li> <p> <code>LaunchingMLInstances</code> </p> </li> <li> <p> <code>PreparingTrainingStack</code> </p> </li> <li> <p> <code>DownloadingTrainingImage</code> </p> </li> </ul>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the training job failed, the reason it failed.</p>"""
    hyper_parameters: NotRequired[
        "capo_sagemaker.types.hyper_parameters.HyperParameters"
    ]
    """<p>Algorithm-specific parameters.</p>"""
    algorithm_specification: NotRequired[
        "capo_sagemaker.types.algorithm_specification.AlgorithmSpecification"
    ]
    """<p>Information about the algorithm used for training, and algorithm metadata.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) role configured for the training job.</p>"""
    input_data_config: NotRequired[
        "capo_sagemaker.types.input_data_config.InputDataConfig"
    ]
    """<p>An array of <code>Channel</code> objects that describes each data input channel.</p> <p>Your input must be in the same Amazon Web Services region as your training job.</p>"""
    output_data_config: NotRequired[
        "capo_sagemaker.types.output_data_config.OutputDataConfig"
    ]
    """<p>The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.</p>"""
    resource_config: NotRequired["capo_sagemaker.types.resource_config.ResourceConfig"]
    """<p>Resources, including ML compute instances and ML storage volumes, that are configured for model training.</p>"""
    warm_pool_status: NotRequired[
        "capo_sagemaker.types.warm_pool_status.WarmPoolStatus"
    ]
    """<p>The status of the warm pool associated with the training job.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>A <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html">VpcConfig</a> object that specifies the VPC that this training job has access to. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html">Protect Training Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.</p> <p>To stop a job, SageMaker sends the algorithm the <code>SIGTERM</code> signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost. </p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the training job was created.</p>"""
    training_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates the time when the training job starts on training instances. You are billed for the time interval between this time and the value of <code>TrainingEndTime</code>. The start time in CloudWatch Logs might be later than this time. The difference is due to the time it takes to download the training data and to the size of the training container.</p>"""
    training_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates the time when the training job ends on training instances. You are billed for the time interval between the value of <code>TrainingStartTime</code> and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the status of the training job was last modified.</p>"""
    secondary_status_transitions: NotRequired[
        "capo_sagemaker.types.secondary_status_transitions.SecondaryStatusTransitions"
    ]
    """<p>A history of all of the secondary statuses that the training job has transitioned through.</p>"""
    final_metric_data_list: NotRequired[
        "capo_sagemaker.types.final_metric_data_list.FinalMetricDataList"
    ]
    """<p>A list of final metric values that are set when the training job completes. Used only if the training job was configured to use metrics.</p>"""
    enable_network_isolation: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>If the <code>TrainingJob</code> was created with network isolation, the value is set to <code>true</code>. If network isolation is enabled, nodes can't communicate beyond the VPC they run in.</p>"""
    enable_inter_container_traffic_encryption: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>To encrypt all communications between ML compute instances in distributed training, choose <code>True</code>. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.</p>"""
    enable_managed_spot_training: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>When true, enables managed spot training using Amazon EC2 Spot instances to run training jobs instead of on-demand instances. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html">Managed Spot Training</a>.</p>"""
    checkpoint_config: NotRequired[
        "capo_sagemaker.types.checkpoint_config.CheckpointConfig"
    ]
    training_time_in_seconds: NotRequired[
        "capo_sagemaker.types.training_time_in_seconds.TrainingTimeInSeconds"
    ]
    """<p>The training time in seconds.</p>"""
    billable_time_in_seconds: NotRequired[
        "capo_sagemaker.types.billable_time_in_seconds.BillableTimeInSeconds"
    ]
    """<p>The billable time in seconds.</p>"""
    debug_hook_config: NotRequired[
        "capo_sagemaker.types.debug_hook_config.DebugHookConfig"
    ]
    experiment_config: NotRequired[
        "capo_sagemaker.types.experiment_config.ExperimentConfig"
    ]
    debug_rule_configurations: NotRequired[
        "capo_sagemaker.types.debug_rule_configurations.DebugRuleConfigurations"
    ]
    """<p>Information about the debug rule configuration.</p>"""
    tensor_board_output_config: NotRequired[
        "capo_sagemaker.types.tensor_board_output_config.TensorBoardOutputConfig"
    ]
    debug_rule_evaluation_statuses: NotRequired[
        "capo_sagemaker.types.debug_rule_evaluation_statuses.DebugRuleEvaluationStatuses"
    ]
    """<p>Information about the evaluation status of the rules for the training job.</p>"""
    output_model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p> The output model package Amazon Resource Name (ARN) that contains model weights or checkpoint. </p>"""
    model_package_config: NotRequired[
        "capo_sagemaker.types.model_package_config.ModelPackageConfig"
    ]
    """<p> The model package configuration. </p>"""
    profiler_config: NotRequired["capo_sagemaker.types.profiler_config.ProfilerConfig"]
    environment: NotRequired[
        "capo_sagemaker.types.training_environment_map.TrainingEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container.</p>"""
    retry_strategy: NotRequired["capo_sagemaker.types.retry_strategy.RetryStrategy"]
    """<p>The number of times to retry the job when the job fails due to an <code>InternalServerError</code>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJob) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    if "tuning_job_arn" in value:
        out["TuningJobArn"] = value["tuning_job_arn"]
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "model_artifacts" in value:
        import capo_sagemaker.types.model_artifacts

        out["ModelArtifacts"] = (
            capo_sagemaker.types.model_artifacts.serialize_aws_json_1_1(
                value["model_artifacts"]
            )
        )
    if "training_job_status" in value:
        import capo_sagemaker.types.training_job_status

        out["TrainingJobStatus"] = (
            capo_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["training_job_status"]
            )
        )
    if "secondary_status" in value:
        import capo_sagemaker.types.secondary_status

        out["SecondaryStatus"] = (
            capo_sagemaker.types.secondary_status.serialize_aws_json_1_1(
                value["secondary_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "hyper_parameters" in value:
        import capo_sagemaker.types.hyper_parameters

        out["HyperParameters"] = (
            capo_sagemaker.types.hyper_parameters.serialize_aws_json_1_1(
                value["hyper_parameters"]
            )
        )
    if "algorithm_specification" in value:
        import capo_sagemaker.types.algorithm_specification

        out["AlgorithmSpecification"] = (
            capo_sagemaker.types.algorithm_specification.serialize_aws_json_1_1(
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
    if "warm_pool_status" in value:
        import capo_sagemaker.types.warm_pool_status

        out["WarmPoolStatus"] = (
            capo_sagemaker.types.warm_pool_status.serialize_aws_json_1_1(
                value["warm_pool_status"]
            )
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "training_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["TrainingStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["training_start_time"]
            )
        )
    if "training_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["TrainingEndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["training_end_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "secondary_status_transitions" in value:
        import capo_sagemaker.types.secondary_status_transitions

        out["SecondaryStatusTransitions"] = (
            capo_sagemaker.types.secondary_status_transitions.serialize_aws_json_1_1(
                value["secondary_status_transitions"]
            )
        )
    if "final_metric_data_list" in value:
        import capo_sagemaker.types.final_metric_data_list

        out["FinalMetricDataList"] = (
            capo_sagemaker.types.final_metric_data_list.serialize_aws_json_1_1(
                value["final_metric_data_list"]
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
    if "training_time_in_seconds" in value:
        out["TrainingTimeInSeconds"] = value["training_time_in_seconds"]
    if "billable_time_in_seconds" in value:
        out["BillableTimeInSeconds"] = value["billable_time_in_seconds"]
    if "debug_hook_config" in value:
        import capo_sagemaker.types.debug_hook_config

        out["DebugHookConfig"] = (
            capo_sagemaker.types.debug_hook_config.serialize_aws_json_1_1(
                value["debug_hook_config"]
            )
        )
    if "experiment_config" in value:
        import capo_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            capo_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    if "debug_rule_configurations" in value:
        import capo_sagemaker.types.debug_rule_configurations

        out["DebugRuleConfigurations"] = (
            capo_sagemaker.types.debug_rule_configurations.serialize_aws_json_1_1(
                value["debug_rule_configurations"]
            )
        )
    if "tensor_board_output_config" in value:
        import capo_sagemaker.types.tensor_board_output_config

        out["TensorBoardOutputConfig"] = (
            capo_sagemaker.types.tensor_board_output_config.serialize_aws_json_1_1(
                value["tensor_board_output_config"]
            )
        )
    if "debug_rule_evaluation_statuses" in value:
        import capo_sagemaker.types.debug_rule_evaluation_statuses

        out["DebugRuleEvaluationStatuses"] = (
            capo_sagemaker.types.debug_rule_evaluation_statuses.serialize_aws_json_1_1(
                value["debug_rule_evaluation_statuses"]
            )
        )
    if "output_model_package_arn" in value:
        out["OutputModelPackageArn"] = value["output_model_package_arn"]
    if "model_package_config" in value:
        import capo_sagemaker.types.model_package_config

        out["ModelPackageConfig"] = (
            capo_sagemaker.types.model_package_config.serialize_aws_json_1_1(
                value["model_package_config"]
            )
        )
    if "profiler_config" in value:
        import capo_sagemaker.types.profiler_config

        out["ProfilerConfig"] = (
            capo_sagemaker.types.profiler_config.serialize_aws_json_1_1(
                value["profiler_config"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.training_environment_map

        out["Environment"] = (
            capo_sagemaker.types.training_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "retry_strategy" in value:
        import capo_sagemaker.types.retry_strategy

        out["RetryStrategy"] = (
            capo_sagemaker.types.retry_strategy.serialize_aws_json_1_1(
                value["retry_strategy"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingJob:
    out: TrainingJob = {}  # type: ignore[typeddict-item]
    if data.get("TrainingJobName") is not None:
        out["training_job_name"] = data["TrainingJobName"]
    if data.get("TrainingJobArn") is not None:
        out["training_job_arn"] = data["TrainingJobArn"]
    if data.get("TuningJobArn") is not None:
        out["tuning_job_arn"] = data["TuningJobArn"]
    if data.get("LabelingJobArn") is not None:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if data.get("AutoMLJobArn") is not None:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if data.get("ModelArtifacts") is not None:
        import capo_sagemaker.types.model_artifacts

        out["model_artifacts"] = (
            capo_sagemaker.types.model_artifacts.deserialize_aws_json_1_1(
                data["ModelArtifacts"]
            )
        )
    if data.get("TrainingJobStatus") is not None:
        import capo_sagemaker.types.training_job_status

        out["training_job_status"] = (
            capo_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["TrainingJobStatus"]
            )
        )
    if data.get("SecondaryStatus") is not None:
        import capo_sagemaker.types.secondary_status

        out["secondary_status"] = (
            capo_sagemaker.types.secondary_status.deserialize_aws_json_1_1(
                data["SecondaryStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("HyperParameters") is not None:
        import capo_sagemaker.types.hyper_parameters

        out["hyper_parameters"] = (
            capo_sagemaker.types.hyper_parameters.deserialize_aws_json_1_1(
                data["HyperParameters"]
            )
        )
    if data.get("AlgorithmSpecification") is not None:
        import capo_sagemaker.types.algorithm_specification

        out["algorithm_specification"] = (
            capo_sagemaker.types.algorithm_specification.deserialize_aws_json_1_1(
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
    if data.get("WarmPoolStatus") is not None:
        import capo_sagemaker.types.warm_pool_status

        out["warm_pool_status"] = (
            capo_sagemaker.types.warm_pool_status.deserialize_aws_json_1_1(
                data["WarmPoolStatus"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("TrainingStartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["training_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingStartTime"]
            )
        )
    if data.get("TrainingEndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["training_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingEndTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("SecondaryStatusTransitions") is not None:
        import capo_sagemaker.types.secondary_status_transitions

        out["secondary_status_transitions"] = (
            capo_sagemaker.types.secondary_status_transitions.deserialize_aws_json_1_1(
                data["SecondaryStatusTransitions"]
            )
        )
    if data.get("FinalMetricDataList") is not None:
        import capo_sagemaker.types.final_metric_data_list

        out["final_metric_data_list"] = (
            capo_sagemaker.types.final_metric_data_list.deserialize_aws_json_1_1(
                data["FinalMetricDataList"]
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
    if data.get("TrainingTimeInSeconds") is not None:
        out["training_time_in_seconds"] = data["TrainingTimeInSeconds"]
    if data.get("BillableTimeInSeconds") is not None:
        out["billable_time_in_seconds"] = data["BillableTimeInSeconds"]
    if data.get("DebugHookConfig") is not None:
        import capo_sagemaker.types.debug_hook_config

        out["debug_hook_config"] = (
            capo_sagemaker.types.debug_hook_config.deserialize_aws_json_1_1(
                data["DebugHookConfig"]
            )
        )
    if data.get("ExperimentConfig") is not None:
        import capo_sagemaker.types.experiment_config

        out["experiment_config"] = (
            capo_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    if data.get("DebugRuleConfigurations") is not None:
        import capo_sagemaker.types.debug_rule_configurations

        out["debug_rule_configurations"] = (
            capo_sagemaker.types.debug_rule_configurations.deserialize_aws_json_1_1(
                data["DebugRuleConfigurations"]
            )
        )
    if data.get("TensorBoardOutputConfig") is not None:
        import capo_sagemaker.types.tensor_board_output_config

        out["tensor_board_output_config"] = (
            capo_sagemaker.types.tensor_board_output_config.deserialize_aws_json_1_1(
                data["TensorBoardOutputConfig"]
            )
        )
    if data.get("DebugRuleEvaluationStatuses") is not None:
        import capo_sagemaker.types.debug_rule_evaluation_statuses

        out["debug_rule_evaluation_statuses"] = (
            capo_sagemaker.types.debug_rule_evaluation_statuses.deserialize_aws_json_1_1(
                data["DebugRuleEvaluationStatuses"]
            )
        )
    if data.get("OutputModelPackageArn") is not None:
        out["output_model_package_arn"] = data["OutputModelPackageArn"]
    if data.get("ModelPackageConfig") is not None:
        import capo_sagemaker.types.model_package_config

        out["model_package_config"] = (
            capo_sagemaker.types.model_package_config.deserialize_aws_json_1_1(
                data["ModelPackageConfig"]
            )
        )
    if data.get("ProfilerConfig") is not None:
        import capo_sagemaker.types.profiler_config

        out["profiler_config"] = (
            capo_sagemaker.types.profiler_config.deserialize_aws_json_1_1(
                data["ProfilerConfig"]
            )
        )
    if data.get("Environment") is not None:
        import capo_sagemaker.types.training_environment_map

        out["environment"] = (
            capo_sagemaker.types.training_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if data.get("RetryStrategy") is not None:
        import capo_sagemaker.types.retry_strategy

        out["retry_strategy"] = (
            capo_sagemaker.types.retry_strategy.deserialize_aws_json_1_1(
                data["RetryStrategy"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
