"""Generated from Smithy shape ``com.amazonaws.personalize#CreateBatchInferenceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.batch_inference_job_config
    import capo_personalize.types.batch_inference_job_input
    import capo_personalize.types.batch_inference_job_mode
    import capo_personalize.types.batch_inference_job_output
    import capo_personalize.types.name
    import capo_personalize.types.num_batch_results
    import capo_personalize.types.role_arn
    import capo_personalize.types.tags
    import capo_personalize.types.theme_generation_config


class CreateBatchInferenceJobRequest(TypedDict, closed=True):
    job_name: "capo_personalize.types.name.Name"
    """<p>The name of the batch inference job to create.</p>"""
    solution_version_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution version that will be used to generate the batch inference recommendations.</p>"""
    filter_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the filter to apply to the batch inference job. For more information on using filters, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter-batch.html">Filtering batch recommendations</a>.</p>"""
    num_results: NotRequired["capo_personalize.types.num_batch_results.NumBatchResults"]
    """<p>The number of recommendations to retrieve.</p>"""
    job_input: "capo_personalize.types.batch_inference_job_input.BatchInferenceJobInput"
    """<p>The Amazon S3 path that leads to the input file to base your recommendations on. The input material must be in JSON format.</p>"""
    job_output: (
        "capo_personalize.types.batch_inference_job_output.BatchInferenceJobOutput"
    )
    """<p>The path to the Amazon S3 bucket where the job's output will be stored.</p>"""
    role_arn: "capo_personalize.types.role_arn.RoleArn"
    """<p>The ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and output Amazon S3 buckets respectively.</p>"""
    batch_inference_job_config: NotRequired[
        "capo_personalize.types.batch_inference_job_config.BatchInferenceJobConfig"
    ]
    """<p>The configuration details of a batch inference job.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the batch inference job.</p>"""
    batch_inference_job_mode: NotRequired[
        "capo_personalize.types.batch_inference_job_mode.BatchInferenceJobMode"
    ]
    """<p>The mode of the batch inference job. To generate descriptive themes for groups of similar items, set the job mode to <code>THEME_GENERATION</code>. If you don't want to generate themes, use the default <code>BATCH_INFERENCE</code>.</p> <p> When you get batch recommendations with themes, you will incur additional costs. For more information, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>. </p>"""
    theme_generation_config: NotRequired[
        "capo_personalize.types.theme_generation_config.ThemeGenerationConfig"
    ]
    """<p>For theme generation jobs, specify the name of the column in your Items dataset that contains each item's name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchInferenceJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["solutionVersionArn"] = value["solution_version_arn"]
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "num_results" in value:
        out["numResults"] = value["num_results"]
    import capo_personalize.types.batch_inference_job_input

    out["jobInput"] = (
        capo_personalize.types.batch_inference_job_input.serialize_aws_json_1_1(
            value["job_input"]
        )
    )
    import capo_personalize.types.batch_inference_job_output

    out["jobOutput"] = (
        capo_personalize.types.batch_inference_job_output.serialize_aws_json_1_1(
            value["job_output"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "batch_inference_job_config" in value:
        import capo_personalize.types.batch_inference_job_config

        out["batchInferenceJobConfig"] = (
            capo_personalize.types.batch_inference_job_config.serialize_aws_json_1_1(
                value["batch_inference_job_config"]
            )
        )
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    if "batch_inference_job_mode" in value:
        import capo_personalize.types.batch_inference_job_mode

        out["batchInferenceJobMode"] = (
            capo_personalize.types.batch_inference_job_mode.serialize_aws_json_1_1(
                value["batch_inference_job_mode"]
            )
        )
    if "theme_generation_config" in value:
        import capo_personalize.types.theme_generation_config

        out["themeGenerationConfig"] = (
            capo_personalize.types.theme_generation_config.serialize_aws_json_1_1(
                value["theme_generation_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchInferenceJobRequest:
    out: CreateBatchInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.job_name required")
    if data.get("solutionVersionArn") is not None:
        out["solution_version_arn"] = data["solutionVersionArn"]
    else:
        raise DeserializationError(
            "CreateBatchInferenceJobRequest.solution_version_arn required"
        )
    if data.get("filterArn") is not None:
        out["filter_arn"] = data["filterArn"]
    if data.get("numResults") is not None:
        out["num_results"] = data["numResults"]
    if data.get("jobInput") is not None:
        import capo_personalize.types.batch_inference_job_input

        out["job_input"] = (
            capo_personalize.types.batch_inference_job_input.deserialize_aws_json_1_1(
                data["jobInput"]
            )
        )
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.job_input required")
    if data.get("jobOutput") is not None:
        import capo_personalize.types.batch_inference_job_output

        out["job_output"] = (
            capo_personalize.types.batch_inference_job_output.deserialize_aws_json_1_1(
                data["jobOutput"]
            )
        )
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.job_output required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.role_arn required")
    if data.get("batchInferenceJobConfig") is not None:
        import capo_personalize.types.batch_inference_job_config

        out["batch_inference_job_config"] = (
            capo_personalize.types.batch_inference_job_config.deserialize_aws_json_1_1(
                data["batchInferenceJobConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("batchInferenceJobMode") is not None:
        import capo_personalize.types.batch_inference_job_mode

        out["batch_inference_job_mode"] = (
            capo_personalize.types.batch_inference_job_mode.deserialize_aws_json_1_1(
                data["batchInferenceJobMode"]
            )
        )
    if data.get("themeGenerationConfig") is not None:
        import capo_personalize.types.theme_generation_config

        out["theme_generation_config"] = (
            capo_personalize.types.theme_generation_config.deserialize_aws_json_1_1(
                data["themeGenerationConfig"]
            )
        )
    return out
