"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateProcessingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_specification
    import capo_sagemaker.types.experiment_config
    import capo_sagemaker.types.network_config
    import capo_sagemaker.types.processing_environment_map
    import capo_sagemaker.types.processing_inputs
    import capo_sagemaker.types.processing_job_name
    import capo_sagemaker.types.processing_output_config
    import capo_sagemaker.types.processing_resources
    import capo_sagemaker.types.processing_stopping_condition
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateProcessingJobRequest(TypedDict, closed=True):
    processing_inputs: NotRequired[
        "capo_sagemaker.types.processing_inputs.ProcessingInputs"
    ]
    """<p>An array of inputs configuring the data to download into the processing container.</p>"""
    processing_output_config: NotRequired[
        "capo_sagemaker.types.processing_output_config.ProcessingOutputConfig"
    ]
    """<p>Output configuration for the processing job.</p>"""
    processing_job_name: NotRequired[
        "capo_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p> The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    processing_resources: NotRequired[
        "capo_sagemaker.types.processing_resources.ProcessingResources"
    ]
    """<p>Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.processing_stopping_condition.ProcessingStoppingCondition"
    ]
    """<p>The time limit for how long the processing job is allowed to run.</p>"""
    app_specification: NotRequired[
        "capo_sagemaker.types.app_specification.AppSpecification"
    ]
    """<p>Configures the processing job to run a specified Docker container image.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.processing_environment_map.ProcessingEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. Up to 100 key and values entries in the map are supported.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.</p> </important>"""
    network_config: NotRequired["capo_sagemaker.types.network_config.NetworkConfig"]
    """<p>Networking options for a processing job, such as whether to allow inbound and outbound network calls to and from processing containers, and the VPC subnets and security groups to use for VPC-enabled processing jobs.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>(Optional) An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request tag variable or plain text fields.</p> </important>"""
    experiment_config: NotRequired[
        "capo_sagemaker.types.experiment_config.ExperimentConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProcessingJobRequest) -> dict:
    out: dict = {}
    if "processing_inputs" in value:
        import capo_sagemaker.types.processing_inputs

        out["ProcessingInputs"] = (
            capo_sagemaker.types.processing_inputs.serialize_aws_json_1_1(
                value["processing_inputs"]
            )
        )
    if "processing_output_config" in value:
        import capo_sagemaker.types.processing_output_config

        out["ProcessingOutputConfig"] = (
            capo_sagemaker.types.processing_output_config.serialize_aws_json_1_1(
                value["processing_output_config"]
            )
        )
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    if "processing_resources" in value:
        import capo_sagemaker.types.processing_resources

        out["ProcessingResources"] = (
            capo_sagemaker.types.processing_resources.serialize_aws_json_1_1(
                value["processing_resources"]
            )
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.processing_stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.processing_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "app_specification" in value:
        import capo_sagemaker.types.app_specification

        out["AppSpecification"] = (
            capo_sagemaker.types.app_specification.serialize_aws_json_1_1(
                value["app_specification"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.processing_environment_map

        out["Environment"] = (
            capo_sagemaker.types.processing_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "network_config" in value:
        import capo_sagemaker.types.network_config

        out["NetworkConfig"] = (
            capo_sagemaker.types.network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "experiment_config" in value:
        import capo_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            capo_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProcessingJobRequest:
    out: CreateProcessingJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProcessingInputs") is not None:
        import capo_sagemaker.types.processing_inputs

        out["processing_inputs"] = (
            capo_sagemaker.types.processing_inputs.deserialize_aws_json_1_1(
                data["ProcessingInputs"]
            )
        )
    if data.get("ProcessingOutputConfig") is not None:
        import capo_sagemaker.types.processing_output_config

        out["processing_output_config"] = (
            capo_sagemaker.types.processing_output_config.deserialize_aws_json_1_1(
                data["ProcessingOutputConfig"]
            )
        )
    if data.get("ProcessingJobName") is not None:
        out["processing_job_name"] = data["ProcessingJobName"]
    if data.get("ProcessingResources") is not None:
        import capo_sagemaker.types.processing_resources

        out["processing_resources"] = (
            capo_sagemaker.types.processing_resources.deserialize_aws_json_1_1(
                data["ProcessingResources"]
            )
        )
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.processing_stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.processing_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("AppSpecification") is not None:
        import capo_sagemaker.types.app_specification

        out["app_specification"] = (
            capo_sagemaker.types.app_specification.deserialize_aws_json_1_1(
                data["AppSpecification"]
            )
        )
    if data.get("Environment") is not None:
        import capo_sagemaker.types.processing_environment_map

        out["environment"] = (
            capo_sagemaker.types.processing_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if data.get("NetworkConfig") is not None:
        import capo_sagemaker.types.network_config

        out["network_config"] = (
            capo_sagemaker.types.network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ExperimentConfig") is not None:
        import capo_sagemaker.types.experiment_config

        out["experiment_config"] = (
            capo_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    return out
