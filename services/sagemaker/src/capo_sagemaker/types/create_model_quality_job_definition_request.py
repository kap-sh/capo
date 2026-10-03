"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelQualityJobDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_quality_app_specification
    import capo_sagemaker.types.model_quality_baseline_config
    import capo_sagemaker.types.model_quality_job_input
    import capo_sagemaker.types.monitoring_job_definition_name
    import capo_sagemaker.types.monitoring_network_config
    import capo_sagemaker.types.monitoring_output_config
    import capo_sagemaker.types.monitoring_resources
    import capo_sagemaker.types.monitoring_stopping_condition
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateModelQualityJobDefinitionRequest(TypedDict, closed=True):
    job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the monitoring job definition.</p>"""
    model_quality_baseline_config: NotRequired[
        "capo_sagemaker.types.model_quality_baseline_config.ModelQualityBaselineConfig"
    ]
    """<p>Specifies the constraints and baselines for the monitoring job.</p>"""
    model_quality_app_specification: NotRequired[
        "capo_sagemaker.types.model_quality_app_specification.ModelQualityAppSpecification"
    ]
    """<p>The container that runs the monitoring job.</p>"""
    model_quality_job_input: NotRequired[
        "capo_sagemaker.types.model_quality_job_input.ModelQualityJobInput"
    ]
    """<p>A list of the inputs that are monitored. Currently endpoints are supported.</p>"""
    model_quality_job_output_config: NotRequired[
        "capo_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    job_resources: NotRequired[
        "capo_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    network_config: NotRequired[
        "capo_sagemaker.types.monitoring_network_config.MonitoringNetworkConfig"
    ]
    """<p>Specifies the network configuration for the monitoring job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>(Optional) An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL"> Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelQualityJobDefinitionRequest) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    if "model_quality_baseline_config" in value:
        import capo_sagemaker.types.model_quality_baseline_config

        out["ModelQualityBaselineConfig"] = (
            capo_sagemaker.types.model_quality_baseline_config.serialize_aws_json_1_1(
                value["model_quality_baseline_config"]
            )
        )
    if "model_quality_app_specification" in value:
        import capo_sagemaker.types.model_quality_app_specification

        out["ModelQualityAppSpecification"] = (
            capo_sagemaker.types.model_quality_app_specification.serialize_aws_json_1_1(
                value["model_quality_app_specification"]
            )
        )
    if "model_quality_job_input" in value:
        import capo_sagemaker.types.model_quality_job_input

        out["ModelQualityJobInput"] = (
            capo_sagemaker.types.model_quality_job_input.serialize_aws_json_1_1(
                value["model_quality_job_input"]
            )
        )
    if "model_quality_job_output_config" in value:
        import capo_sagemaker.types.monitoring_output_config

        out["ModelQualityJobOutputConfig"] = (
            capo_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["model_quality_job_output_config"]
            )
        )
    if "job_resources" in value:
        import capo_sagemaker.types.monitoring_resources

        out["JobResources"] = (
            capo_sagemaker.types.monitoring_resources.serialize_aws_json_1_1(
                value["job_resources"]
            )
        )
    if "network_config" in value:
        import capo_sagemaker.types.monitoring_network_config

        out["NetworkConfig"] = (
            capo_sagemaker.types.monitoring_network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import capo_sagemaker.types.monitoring_stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.monitoring_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelQualityJobDefinitionRequest:
    out: CreateModelQualityJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobDefinitionName") is not None:
        out["job_definition_name"] = data["JobDefinitionName"]
    if data.get("ModelQualityBaselineConfig") is not None:
        import capo_sagemaker.types.model_quality_baseline_config

        out["model_quality_baseline_config"] = (
            capo_sagemaker.types.model_quality_baseline_config.deserialize_aws_json_1_1(
                data["ModelQualityBaselineConfig"]
            )
        )
    if data.get("ModelQualityAppSpecification") is not None:
        import capo_sagemaker.types.model_quality_app_specification

        out["model_quality_app_specification"] = (
            capo_sagemaker.types.model_quality_app_specification.deserialize_aws_json_1_1(
                data["ModelQualityAppSpecification"]
            )
        )
    if data.get("ModelQualityJobInput") is not None:
        import capo_sagemaker.types.model_quality_job_input

        out["model_quality_job_input"] = (
            capo_sagemaker.types.model_quality_job_input.deserialize_aws_json_1_1(
                data["ModelQualityJobInput"]
            )
        )
    if data.get("ModelQualityJobOutputConfig") is not None:
        import capo_sagemaker.types.monitoring_output_config

        out["model_quality_job_output_config"] = (
            capo_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["ModelQualityJobOutputConfig"]
            )
        )
    if data.get("JobResources") is not None:
        import capo_sagemaker.types.monitoring_resources

        out["job_resources"] = (
            capo_sagemaker.types.monitoring_resources.deserialize_aws_json_1_1(
                data["JobResources"]
            )
        )
    if data.get("NetworkConfig") is not None:
        import capo_sagemaker.types.monitoring_network_config

        out["network_config"] = (
            capo_sagemaker.types.monitoring_network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.monitoring_stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.monitoring_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
