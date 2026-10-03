"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAutoMLJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_input_data_config
    import capo_sagemaker.types.auto_ml_job_config
    import capo_sagemaker.types.auto_ml_job_name
    import capo_sagemaker.types.auto_ml_job_objective
    import capo_sagemaker.types.auto_ml_output_data_config
    import capo_sagemaker.types.generate_candidate_definitions_only
    import capo_sagemaker.types.model_deploy_config
    import capo_sagemaker.types.problem_type
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateAutoMLJobRequest(TypedDict, closed=True):
    auto_ml_job_name: NotRequired["capo_sagemaker.types.auto_ml_job_name.AutoMLJobName"]
    """<p>Identifies an Autopilot job. The name must be unique to your account and is case insensitive.</p>"""
    input_data_config: NotRequired[
        "capo_sagemaker.types.auto_ml_input_data_config.AutoMLInputDataConfig"
    ]
    """<p>An array of channel objects that describes the input data and its location. Each channel is a named input source. Similar to <code>InputDataConfig</code> supported by <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html">HyperParameterTrainingJobDefinition</a>. Format(s) supported: CSV, Parquet. A minimum of 500 rows is required for the training dataset. There is not a minimum number of rows required for the validation dataset.</p>"""
    output_data_config: NotRequired[
        "capo_sagemaker.types.auto_ml_output_data_config.AutoMLOutputDataConfig"
    ]
    """<p>Provides information about encryption and the Amazon S3 output path needed to store artifacts from an AutoML job. Format(s) supported: CSV.</p>"""
    problem_type: NotRequired["capo_sagemaker.types.problem_type.ProblemType"]
    """<p>Defines the type of supervised learning problem available for the candidates. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types"> SageMaker Autopilot problem types</a>.</p>"""
    auto_ml_job_objective: NotRequired[
        "capo_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    """<p>Specifies a metric to minimize or maximize as the objective of a job. If not specified, the default objective metric depends on the problem type. See <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html">AutoMLJobObjective</a> for the default values.</p>"""
    auto_ml_job_config: NotRequired[
        "capo_sagemaker.types.auto_ml_job_config.AutoMLJobConfig"
    ]
    """<p>A collection of settings used to configure an AutoML job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the role that is used to access the data.</p>"""
    generate_candidate_definitions_only: NotRequired[
        "capo_sagemaker.types.generate_candidate_definitions_only.GenerateCandidateDefinitionsOnly"
    ]
    """<p>Generates possible candidates without training the models. A candidate is a combination of data preprocessors, algorithms, and algorithm parameter settings.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web ServicesResources</a>. Tag keys must be unique per resource.</p>"""
    model_deploy_config: NotRequired[
        "capo_sagemaker.types.model_deploy_config.ModelDeployConfig"
    ]
    """<p>Specifies how to generate the endpoint name for an automatic one-click Autopilot model deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAutoMLJobRequest) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    if "input_data_config" in value:
        import capo_sagemaker.types.auto_ml_input_data_config

        out["InputDataConfig"] = (
            capo_sagemaker.types.auto_ml_input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_sagemaker.types.auto_ml_output_data_config

        out["OutputDataConfig"] = (
            capo_sagemaker.types.auto_ml_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "problem_type" in value:
        import capo_sagemaker.types.problem_type

        out["ProblemType"] = capo_sagemaker.types.problem_type.serialize_aws_json_1_1(
            value["problem_type"]
        )
    if "auto_ml_job_objective" in value:
        import capo_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            capo_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "auto_ml_job_config" in value:
        import capo_sagemaker.types.auto_ml_job_config

        out["AutoMLJobConfig"] = (
            capo_sagemaker.types.auto_ml_job_config.serialize_aws_json_1_1(
                value["auto_ml_job_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "generate_candidate_definitions_only" in value:
        out["GenerateCandidateDefinitionsOnly"] = value[
            "generate_candidate_definitions_only"
        ]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "model_deploy_config" in value:
        import capo_sagemaker.types.model_deploy_config

        out["ModelDeployConfig"] = (
            capo_sagemaker.types.model_deploy_config.serialize_aws_json_1_1(
                value["model_deploy_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAutoMLJobRequest:
    out: CreateAutoMLJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoMLJobName") is not None:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    if data.get("InputDataConfig") is not None:
        import capo_sagemaker.types.auto_ml_input_data_config

        out["input_data_config"] = (
            capo_sagemaker.types.auto_ml_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_sagemaker.types.auto_ml_output_data_config

        out["output_data_config"] = (
            capo_sagemaker.types.auto_ml_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("ProblemType") is not None:
        import capo_sagemaker.types.problem_type

        out["problem_type"] = (
            capo_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    if data.get("AutoMLJobObjective") is not None:
        import capo_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            capo_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if data.get("AutoMLJobConfig") is not None:
        import capo_sagemaker.types.auto_ml_job_config

        out["auto_ml_job_config"] = (
            capo_sagemaker.types.auto_ml_job_config.deserialize_aws_json_1_1(
                data["AutoMLJobConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("GenerateCandidateDefinitionsOnly") is not None:
        out["generate_candidate_definitions_only"] = data[
            "GenerateCandidateDefinitionsOnly"
        ]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ModelDeployConfig") is not None:
        import capo_sagemaker.types.model_deploy_config

        out["model_deploy_config"] = (
            capo_sagemaker.types.model_deploy_config.deserialize_aws_json_1_1(
                data["ModelDeployConfig"]
            )
        )
    return out
