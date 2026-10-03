"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceRecommendationsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.recommendation_job_description
    import capo_sagemaker.types.recommendation_job_input_config
    import capo_sagemaker.types.recommendation_job_name
    import capo_sagemaker.types.recommendation_job_output_config
    import capo_sagemaker.types.recommendation_job_stopping_conditions
    import capo_sagemaker.types.recommendation_job_type
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateInferenceRecommendationsJobRequest(TypedDict, closed=True):
    job_name: NotRequired[
        "capo_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>A name for the recommendation job. The name must be unique within the Amazon Web Services Region and within your Amazon Web Services account. The job name is passed down to the resources created by the recommendation job. The names of resources (such as the model, endpoint configuration, endpoint, and compilation) that are prefixed with the job name are truncated at 40 characters.</p>"""
    job_type: NotRequired[
        "capo_sagemaker.types.recommendation_job_type.RecommendationJobType"
    ]
    """<p>Defines the type of recommendation job. Specify <code>Default</code> to initiate an instance recommendation and <code>Advanced</code> to initiate a load test. If left unspecified, Amazon SageMaker Inference Recommender will run an instance recommendation (<code>DEFAULT</code>) job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.</p>"""
    input_config: NotRequired[
        "capo_sagemaker.types.recommendation_job_input_config.RecommendationJobInputConfig"
    ]
    """<p>Provides information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations.</p>"""
    job_description: NotRequired[
        "capo_sagemaker.types.recommendation_job_description.RecommendationJobDescription"
    ]
    """<p>Description of the recommendation job.</p>"""
    stopping_conditions: NotRequired[
        "capo_sagemaker.types.recommendation_job_stopping_conditions.RecommendationJobStoppingConditions"
    ]
    """<p>A set of conditions for stopping a recommendation job. If any of the conditions are met, the job is automatically stopped.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.recommendation_job_output_config.RecommendationJobOutputConfig"
    ]
    """<p>Provides information about the output artifacts and the KMS key to use for Amazon S3 server-side encryption.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The metadata that you apply to Amazon Web Services resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in the Amazon Web Services General Reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceRecommendationsJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_type" in value:
        import capo_sagemaker.types.recommendation_job_type

        out["JobType"] = (
            capo_sagemaker.types.recommendation_job_type.serialize_aws_json_1_1(
                value["job_type"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "input_config" in value:
        import capo_sagemaker.types.recommendation_job_input_config

        out["InputConfig"] = (
            capo_sagemaker.types.recommendation_job_input_config.serialize_aws_json_1_1(
                value["input_config"]
            )
        )
    if "job_description" in value:
        out["JobDescription"] = value["job_description"]
    if "stopping_conditions" in value:
        import capo_sagemaker.types.recommendation_job_stopping_conditions

        out["StoppingConditions"] = (
            capo_sagemaker.types.recommendation_job_stopping_conditions.serialize_aws_json_1_1(
                value["stopping_conditions"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.recommendation_job_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.recommendation_job_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceRecommendationsJobRequest:
    out: CreateInferenceRecommendationsJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobType") is not None:
        import capo_sagemaker.types.recommendation_job_type

        out["job_type"] = (
            capo_sagemaker.types.recommendation_job_type.deserialize_aws_json_1_1(
                data["JobType"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("InputConfig") is not None:
        import capo_sagemaker.types.recommendation_job_input_config

        out["input_config"] = (
            capo_sagemaker.types.recommendation_job_input_config.deserialize_aws_json_1_1(
                data["InputConfig"]
            )
        )
    if data.get("JobDescription") is not None:
        out["job_description"] = data["JobDescription"]
    if data.get("StoppingConditions") is not None:
        import capo_sagemaker.types.recommendation_job_stopping_conditions

        out["stopping_conditions"] = (
            capo_sagemaker.types.recommendation_job_stopping_conditions.deserialize_aws_json_1_1(
                data["StoppingConditions"]
            )
        )
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.recommendation_job_output_config

        out["output_config"] = (
            capo_sagemaker.types.recommendation_job_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
