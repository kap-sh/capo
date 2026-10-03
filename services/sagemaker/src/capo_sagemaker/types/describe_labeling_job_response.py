"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeLabelingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.human_task_config
    import capo_sagemaker.types.job_reference_code
    import capo_sagemaker.types.label_attribute_name
    import capo_sagemaker.types.label_counters
    import capo_sagemaker.types.labeling_job_algorithms_config
    import capo_sagemaker.types.labeling_job_arn
    import capo_sagemaker.types.labeling_job_input_config
    import capo_sagemaker.types.labeling_job_name
    import capo_sagemaker.types.labeling_job_output
    import capo_sagemaker.types.labeling_job_output_config
    import capo_sagemaker.types.labeling_job_status
    import capo_sagemaker.types.labeling_job_stopping_conditions
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp


class DescribeLabelingJobResponse(TypedDict, closed=True):
    labeling_job_status: NotRequired[
        "capo_sagemaker.types.labeling_job_status.LabelingJobStatus"
    ]
    """<p>The processing status of the labeling job. </p>"""
    label_counters: NotRequired["capo_sagemaker.types.label_counters.LabelCounters"]
    """<p>Provides a breakdown of the number of data objects labeled by humans, the number of objects labeled by machine, the number of objects than couldn't be labeled, and the total number of objects labeled. </p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the job failed, the reason that it failed. </p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the labeling job was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the labeling job was last updated.</p>"""
    job_reference_code: NotRequired[
        "capo_sagemaker.types.job_reference_code.JobReferenceCode"
    ]
    """<p>A unique identifier for work done as part of a labeling job.</p>"""
    labeling_job_name: NotRequired[
        "capo_sagemaker.types.labeling_job_name.LabelingJobName"
    ]
    """<p>The name assigned to the labeling job when it was created.</p>"""
    labeling_job_arn: NotRequired[
        "capo_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the labeling job.</p>"""
    label_attribute_name: NotRequired[
        "capo_sagemaker.types.label_attribute_name.LabelAttributeName"
    ]
    """<p>The attribute used as the label in the output manifest file.</p>"""
    input_config: NotRequired[
        "capo_sagemaker.types.labeling_job_input_config.LabelingJobInputConfig"
    ]
    """<p>Input configuration information for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.labeling_job_output_config.LabelingJobOutputConfig"
    ]
    """<p>The location of the job's output data and the Amazon Web Services Key Management Service key ID for the key used to encrypt the output data, if any.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that SageMaker assumes to perform tasks on your behalf during data labeling.</p>"""
    label_category_config_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 location of the JSON file that defines the categories used to label data objects. Please note the following label-category limits:</p> <ul> <li> <p>Semantic segmentation labeling jobs using automated labeling: 20 labels</p> </li> <li> <p>Box bounding labeling jobs (all): 10 labels</p> </li> </ul> <p>The file is a JSON structure in the following format:</p> <p> <code>{</code> </p> <p> <code> "document-version": "2018-11-28"</code> </p> <p> <code> "labels": [</code> </p> <p> <code> {</code> </p> <p> <code> "label": "<i>label 1</i>"</code> </p> <p> <code> },</code> </p> <p> <code> {</code> </p> <p> <code> "label": "<i>label 2</i>"</code> </p> <p> <code> },</code> </p> <p> <code> ...</code> </p> <p> <code> {</code> </p> <p> <code> "label": "<i>label n</i>"</code> </p> <p> <code> }</code> </p> <p> <code> ]</code> </p> <p> <code>}</code> </p>"""
    stopping_conditions: NotRequired[
        "capo_sagemaker.types.labeling_job_stopping_conditions.LabelingJobStoppingConditions"
    ]
    """<p>A set of conditions for stopping a labeling job. If any of the conditions are met, the job is automatically stopped.</p>"""
    labeling_job_algorithms_config: NotRequired[
        "capo_sagemaker.types.labeling_job_algorithms_config.LabelingJobAlgorithmsConfig"
    ]
    """<p>Configuration information for automated data labeling.</p>"""
    human_task_config: NotRequired[
        "capo_sagemaker.types.human_task_config.HumanTaskConfig"
    ]
    """<p>Configuration information required for human workers to complete a labeling task.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""
    labeling_job_output: NotRequired[
        "capo_sagemaker.types.labeling_job_output.LabelingJobOutput"
    ]
    """<p>The location of the output produced by the labeling job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLabelingJobResponse) -> dict:
    out: dict = {}
    if "labeling_job_status" in value:
        import capo_sagemaker.types.labeling_job_status

        out["LabelingJobStatus"] = (
            capo_sagemaker.types.labeling_job_status.serialize_aws_json_1_1(
                value["labeling_job_status"]
            )
        )
    if "label_counters" in value:
        import capo_sagemaker.types.label_counters

        out["LabelCounters"] = (
            capo_sagemaker.types.label_counters.serialize_aws_json_1_1(
                value["label_counters"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "job_reference_code" in value:
        out["JobReferenceCode"] = value["job_reference_code"]
    if "labeling_job_name" in value:
        out["LabelingJobName"] = value["labeling_job_name"]
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "label_attribute_name" in value:
        out["LabelAttributeName"] = value["label_attribute_name"]
    if "input_config" in value:
        import capo_sagemaker.types.labeling_job_input_config

        out["InputConfig"] = (
            capo_sagemaker.types.labeling_job_input_config.serialize_aws_json_1_1(
                value["input_config"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.labeling_job_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.labeling_job_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "label_category_config_s3_uri" in value:
        out["LabelCategoryConfigS3Uri"] = value["label_category_config_s3_uri"]
    if "stopping_conditions" in value:
        import capo_sagemaker.types.labeling_job_stopping_conditions

        out["StoppingConditions"] = (
            capo_sagemaker.types.labeling_job_stopping_conditions.serialize_aws_json_1_1(
                value["stopping_conditions"]
            )
        )
    if "labeling_job_algorithms_config" in value:
        import capo_sagemaker.types.labeling_job_algorithms_config

        out["LabelingJobAlgorithmsConfig"] = (
            capo_sagemaker.types.labeling_job_algorithms_config.serialize_aws_json_1_1(
                value["labeling_job_algorithms_config"]
            )
        )
    if "human_task_config" in value:
        import capo_sagemaker.types.human_task_config

        out["HumanTaskConfig"] = (
            capo_sagemaker.types.human_task_config.serialize_aws_json_1_1(
                value["human_task_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "labeling_job_output" in value:
        import capo_sagemaker.types.labeling_job_output

        out["LabelingJobOutput"] = (
            capo_sagemaker.types.labeling_job_output.serialize_aws_json_1_1(
                value["labeling_job_output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLabelingJobResponse:
    out: DescribeLabelingJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("LabelingJobStatus") is not None:
        import capo_sagemaker.types.labeling_job_status

        out["labeling_job_status"] = (
            capo_sagemaker.types.labeling_job_status.deserialize_aws_json_1_1(
                data["LabelingJobStatus"]
            )
        )
    if data.get("LabelCounters") is not None:
        import capo_sagemaker.types.label_counters

        out["label_counters"] = (
            capo_sagemaker.types.label_counters.deserialize_aws_json_1_1(
                data["LabelCounters"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("JobReferenceCode") is not None:
        out["job_reference_code"] = data["JobReferenceCode"]
    if data.get("LabelingJobName") is not None:
        out["labeling_job_name"] = data["LabelingJobName"]
    if data.get("LabelingJobArn") is not None:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if data.get("LabelAttributeName") is not None:
        out["label_attribute_name"] = data["LabelAttributeName"]
    if data.get("InputConfig") is not None:
        import capo_sagemaker.types.labeling_job_input_config

        out["input_config"] = (
            capo_sagemaker.types.labeling_job_input_config.deserialize_aws_json_1_1(
                data["InputConfig"]
            )
        )
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.labeling_job_output_config

        out["output_config"] = (
            capo_sagemaker.types.labeling_job_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("LabelCategoryConfigS3Uri") is not None:
        out["label_category_config_s3_uri"] = data["LabelCategoryConfigS3Uri"]
    if data.get("StoppingConditions") is not None:
        import capo_sagemaker.types.labeling_job_stopping_conditions

        out["stopping_conditions"] = (
            capo_sagemaker.types.labeling_job_stopping_conditions.deserialize_aws_json_1_1(
                data["StoppingConditions"]
            )
        )
    if data.get("LabelingJobAlgorithmsConfig") is not None:
        import capo_sagemaker.types.labeling_job_algorithms_config

        out["labeling_job_algorithms_config"] = (
            capo_sagemaker.types.labeling_job_algorithms_config.deserialize_aws_json_1_1(
                data["LabelingJobAlgorithmsConfig"]
            )
        )
    if data.get("HumanTaskConfig") is not None:
        import capo_sagemaker.types.human_task_config

        out["human_task_config"] = (
            capo_sagemaker.types.human_task_config.deserialize_aws_json_1_1(
                data["HumanTaskConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("LabelingJobOutput") is not None:
        import capo_sagemaker.types.labeling_job_output

        out["labeling_job_output"] = (
            capo_sagemaker.types.labeling_job_output.deserialize_aws_json_1_1(
                data["LabelingJobOutput"]
            )
        )
    return out
