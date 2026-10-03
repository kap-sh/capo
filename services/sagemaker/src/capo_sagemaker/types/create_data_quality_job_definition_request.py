"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateDataQualityJobDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.data_quality_app_specification
    import capo_sagemaker.types.data_quality_baseline_config
    import capo_sagemaker.types.data_quality_job_input
    import capo_sagemaker.types.monitoring_job_definition_name
    import capo_sagemaker.types.monitoring_network_config
    import capo_sagemaker.types.monitoring_output_config
    import capo_sagemaker.types.monitoring_resources
    import capo_sagemaker.types.monitoring_stopping_condition
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateDataQualityJobDefinitionRequest(TypedDict, closed=True):
    job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name for the monitoring job definition.</p>"""
    data_quality_baseline_config: NotRequired[
        "capo_sagemaker.types.data_quality_baseline_config.DataQualityBaselineConfig"
    ]
    """<p>Configures the constraints and baselines for the monitoring job.</p>"""
    data_quality_app_specification: NotRequired[
        "capo_sagemaker.types.data_quality_app_specification.DataQualityAppSpecification"
    ]
    """<p>Specifies the container that runs the monitoring job.</p>"""
    data_quality_job_input: NotRequired[
        "capo_sagemaker.types.data_quality_job_input.DataQualityJobInput"
    ]
    """<p>A list of inputs for the monitoring job. Currently endpoints are supported as monitoring inputs.</p>"""
    data_quality_job_output_config: NotRequired[
        "capo_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    job_resources: NotRequired[
        "capo_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    network_config: NotRequired[
        "capo_sagemaker.types.monitoring_network_config.MonitoringNetworkConfig"
    ]
    """<p>Specifies networking configuration for the monitoring job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>(Optional) An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL"> Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataQualityJobDefinitionRequest) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    if "data_quality_baseline_config" in value:
        import capo_sagemaker.types.data_quality_baseline_config

        out["DataQualityBaselineConfig"] = (
            capo_sagemaker.types.data_quality_baseline_config.serialize_aws_json_1_1(
                value["data_quality_baseline_config"]
            )
        )
    if "data_quality_app_specification" in value:
        import capo_sagemaker.types.data_quality_app_specification

        out["DataQualityAppSpecification"] = (
            capo_sagemaker.types.data_quality_app_specification.serialize_aws_json_1_1(
                value["data_quality_app_specification"]
            )
        )
    if "data_quality_job_input" in value:
        import capo_sagemaker.types.data_quality_job_input

        out["DataQualityJobInput"] = (
            capo_sagemaker.types.data_quality_job_input.serialize_aws_json_1_1(
                value["data_quality_job_input"]
            )
        )
    if "data_quality_job_output_config" in value:
        import capo_sagemaker.types.monitoring_output_config

        out["DataQualityJobOutputConfig"] = (
            capo_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["data_quality_job_output_config"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateDataQualityJobDefinitionRequest:
    out: CreateDataQualityJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobDefinitionName") is not None:
        out["job_definition_name"] = data["JobDefinitionName"]
    if data.get("DataQualityBaselineConfig") is not None:
        import capo_sagemaker.types.data_quality_baseline_config

        out["data_quality_baseline_config"] = (
            capo_sagemaker.types.data_quality_baseline_config.deserialize_aws_json_1_1(
                data["DataQualityBaselineConfig"]
            )
        )
    if data.get("DataQualityAppSpecification") is not None:
        import capo_sagemaker.types.data_quality_app_specification

        out["data_quality_app_specification"] = (
            capo_sagemaker.types.data_quality_app_specification.deserialize_aws_json_1_1(
                data["DataQualityAppSpecification"]
            )
        )
    if data.get("DataQualityJobInput") is not None:
        import capo_sagemaker.types.data_quality_job_input

        out["data_quality_job_input"] = (
            capo_sagemaker.types.data_quality_job_input.deserialize_aws_json_1_1(
                data["DataQualityJobInput"]
            )
        )
    if data.get("DataQualityJobOutputConfig") is not None:
        import capo_sagemaker.types.monitoring_output_config

        out["data_quality_job_output_config"] = (
            capo_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["DataQualityJobOutputConfig"]
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
