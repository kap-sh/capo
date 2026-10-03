"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAutoMLJobV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_compute_config
    import capo_sagemaker.types.auto_ml_data_split_config
    import capo_sagemaker.types.auto_ml_job_input_data_config
    import capo_sagemaker.types.auto_ml_job_name
    import capo_sagemaker.types.auto_ml_job_objective
    import capo_sagemaker.types.auto_ml_output_data_config
    import capo_sagemaker.types.auto_ml_problem_type_config
    import capo_sagemaker.types.auto_ml_security_config
    import capo_sagemaker.types.model_deploy_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateAutoMLJobV2Request(TypedDict, closed=True):
    auto_ml_job_name: NotRequired["capo_sagemaker.types.auto_ml_job_name.AutoMLJobName"]
    """<p>Identifies an Autopilot job. The name must be unique to your account and is case insensitive.</p>"""
    auto_ml_job_input_data_config: NotRequired[
        "capo_sagemaker.types.auto_ml_job_input_data_config.AutoMLJobInputDataConfig"
    ]
    """<p>An array of channel objects describing the input data and their location. Each channel is a named input source. Similar to the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-InputDataConfig">InputDataConfig</a> attribute in the <code>CreateAutoMLJob</code> input parameters. The supported formats depend on the problem type:</p> <ul> <li> <p>For tabular problem types: <code>S3Prefix</code>, <code>ManifestFile</code>.</p> </li> <li> <p>For image classification: <code>S3Prefix</code>, <code>ManifestFile</code>, <code>AugmentedManifestFile</code>.</p> </li> <li> <p>For text classification: <code>S3Prefix</code>.</p> </li> <li> <p>For time-series forecasting: <code>S3Prefix</code>.</p> </li> <li> <p>For text generation (LLMs fine-tuning): <code>S3Prefix</code>.</p> </li> </ul>"""
    output_data_config: NotRequired[
        "capo_sagemaker.types.auto_ml_output_data_config.AutoMLOutputDataConfig"
    ]
    """<p>Provides information about encryption and the Amazon S3 output path needed to store artifacts from an AutoML job.</p>"""
    auto_ml_problem_type_config: NotRequired[
        "capo_sagemaker.types.auto_ml_problem_type_config.AutoMLProblemTypeConfig"
    ]
    """<p>Defines the configuration settings of one of the supported problem types.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the role that is used to access the data.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, such as by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web ServicesResources</a>. Tag keys must be unique per resource.</p>"""
    security_config: NotRequired[
        "capo_sagemaker.types.auto_ml_security_config.AutoMLSecurityConfig"
    ]
    """<p>The security configuration for traffic encryption or Amazon VPC settings.</p>"""
    auto_ml_job_objective: NotRequired[
        "capo_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    """<p>Specifies a metric to minimize or maximize as the objective of a job. If not specified, the default objective metric depends on the problem type. For the list of default values per problem type, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html">AutoMLJobObjective</a>.</p> <note> <ul> <li> <p>For tabular problem types: You must either provide both the <code>AutoMLJobObjective</code> and indicate the type of supervised learning problem in <code>AutoMLProblemTypeConfig</code> (<code>TabularJobConfig.ProblemType</code>), or none at all.</p> </li> <li> <p>For text generation problem types (LLMs fine-tuning): Fine-tuning language models in Autopilot does not require setting the <code>AutoMLJobObjective</code> field. Autopilot fine-tunes LLMs without requiring multiple candidates to be trained and evaluated. Instead, using your dataset, Autopilot directly fine-tunes your target model to enhance a default objective metric, the cross-entropy loss. After fine-tuning a language model, you can evaluate the quality of its generated text using different metrics. For a list of the available metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-metrics.html">Metrics for fine-tuning LLMs in Autopilot</a>.</p> </li> </ul> </note>"""
    model_deploy_config: NotRequired[
        "capo_sagemaker.types.model_deploy_config.ModelDeployConfig"
    ]
    """<p>Specifies how to generate the endpoint name for an automatic one-click Autopilot model deployment.</p>"""
    data_split_config: NotRequired[
        "capo_sagemaker.types.auto_ml_data_split_config.AutoMLDataSplitConfig"
    ]
    """<p>This structure specifies how to split the data into train and validation datasets.</p> <p>The validation and training datasets must contain the same headers. For jobs created by calling <code>CreateAutoMLJob</code>, the validation dataset must be less than 2 GB in size.</p> <note> <p>This attribute must not be set for the time-series forecasting problem type, as Autopilot automatically splits the input dataset into training and validation sets.</p> </note>"""
    auto_ml_compute_config: NotRequired[
        "capo_sagemaker.types.auto_ml_compute_config.AutoMLComputeConfig"
    ]
    """<p>Specifies the compute configuration for the AutoML job V2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAutoMLJobV2Request) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    if "auto_ml_job_input_data_config" in value:
        import capo_sagemaker.types.auto_ml_job_input_data_config

        out["AutoMLJobInputDataConfig"] = (
            capo_sagemaker.types.auto_ml_job_input_data_config.serialize_aws_json_1_1(
                value["auto_ml_job_input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_sagemaker.types.auto_ml_output_data_config

        out["OutputDataConfig"] = (
            capo_sagemaker.types.auto_ml_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "auto_ml_problem_type_config" in value:
        import capo_sagemaker.types.auto_ml_problem_type_config

        out["AutoMLProblemTypeConfig"] = (
            capo_sagemaker.types.auto_ml_problem_type_config.serialize_aws_json_1_1(
                value["auto_ml_problem_type_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "security_config" in value:
        import capo_sagemaker.types.auto_ml_security_config

        out["SecurityConfig"] = (
            capo_sagemaker.types.auto_ml_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "auto_ml_job_objective" in value:
        import capo_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            capo_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "model_deploy_config" in value:
        import capo_sagemaker.types.model_deploy_config

        out["ModelDeployConfig"] = (
            capo_sagemaker.types.model_deploy_config.serialize_aws_json_1_1(
                value["model_deploy_config"]
            )
        )
    if "data_split_config" in value:
        import capo_sagemaker.types.auto_ml_data_split_config

        out["DataSplitConfig"] = (
            capo_sagemaker.types.auto_ml_data_split_config.serialize_aws_json_1_1(
                value["data_split_config"]
            )
        )
    if "auto_ml_compute_config" in value:
        import capo_sagemaker.types.auto_ml_compute_config

        out["AutoMLComputeConfig"] = (
            capo_sagemaker.types.auto_ml_compute_config.serialize_aws_json_1_1(
                value["auto_ml_compute_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAutoMLJobV2Request:
    out: CreateAutoMLJobV2Request = {}  # type: ignore[typeddict-item]
    if data.get("AutoMLJobName") is not None:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    if data.get("AutoMLJobInputDataConfig") is not None:
        import capo_sagemaker.types.auto_ml_job_input_data_config

        out["auto_ml_job_input_data_config"] = (
            capo_sagemaker.types.auto_ml_job_input_data_config.deserialize_aws_json_1_1(
                data["AutoMLJobInputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_sagemaker.types.auto_ml_output_data_config

        out["output_data_config"] = (
            capo_sagemaker.types.auto_ml_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("AutoMLProblemTypeConfig") is not None:
        import capo_sagemaker.types.auto_ml_problem_type_config

        out["auto_ml_problem_type_config"] = (
            capo_sagemaker.types.auto_ml_problem_type_config.deserialize_aws_json_1_1(
                data["AutoMLProblemTypeConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("SecurityConfig") is not None:
        import capo_sagemaker.types.auto_ml_security_config

        out["security_config"] = (
            capo_sagemaker.types.auto_ml_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if data.get("AutoMLJobObjective") is not None:
        import capo_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            capo_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if data.get("ModelDeployConfig") is not None:
        import capo_sagemaker.types.model_deploy_config

        out["model_deploy_config"] = (
            capo_sagemaker.types.model_deploy_config.deserialize_aws_json_1_1(
                data["ModelDeployConfig"]
            )
        )
    if data.get("DataSplitConfig") is not None:
        import capo_sagemaker.types.auto_ml_data_split_config

        out["data_split_config"] = (
            capo_sagemaker.types.auto_ml_data_split_config.deserialize_aws_json_1_1(
                data["DataSplitConfig"]
            )
        )
    if data.get("AutoMLComputeConfig") is not None:
        import capo_sagemaker.types.auto_ml_compute_config

        out["auto_ml_compute_config"] = (
            capo_sagemaker.types.auto_ml_compute_config.deserialize_aws_json_1_1(
                data["AutoMLComputeConfig"]
            )
        )
    return out
