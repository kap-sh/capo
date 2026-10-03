"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateLabelingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.human_task_config
    import capo_sagemaker.types.label_attribute_name
    import capo_sagemaker.types.labeling_job_algorithms_config
    import capo_sagemaker.types.labeling_job_input_config
    import capo_sagemaker.types.labeling_job_name
    import capo_sagemaker.types.labeling_job_output_config
    import capo_sagemaker.types.labeling_job_stopping_conditions
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.tag_list


class CreateLabelingJobRequest(TypedDict, closed=True):
    labeling_job_name: NotRequired[
        "capo_sagemaker.types.labeling_job_name.LabelingJobName"
    ]
    """<p>The name of the labeling job. This name is used to identify the job in a list of labeling jobs. Labeling job names must be unique within an Amazon Web Services account and region. <code>LabelingJobName</code> is not case sensitive. For example, Example-job and example-job are considered the same labeling job name by Ground Truth.</p>"""
    label_attribute_name: NotRequired[
        "capo_sagemaker.types.label_attribute_name.LabelAttributeName"
    ]
    """<p>The attribute name to use for the label in the output manifest file. This is the key for the key/value pair formed with the label that a worker assigns to the object. The <code>LabelAttributeName</code> must meet the following requirements.</p> <ul> <li> <p>The name can't end with "-metadata". </p> </li> <li> <p>If you are using one of the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html">built-in task types</a> or one of the following, the attribute name <i>must</i> end with "-ref".</p> <ul> <li> <p>Image semantic segmentation (<code>SemanticSegmentation)</code> and adjustment (<code>AdjustmentSemanticSegmentation</code>) labeling jobs for this task type. One exception is that verification (<code>VerificationSemanticSegmentation</code>) <i>must not</i> end with -"ref".</p> </li> <li> <p>Video frame object detection (<code>VideoObjectDetection</code>), and adjustment and verification (<code>AdjustmentVideoObjectDetection</code>) labeling jobs for this task type.</p> </li> <li> <p>Video frame object tracking (<code>VideoObjectTracking</code>), and adjustment and verification (<code>AdjustmentVideoObjectTracking</code>) labeling jobs for this task type.</p> </li> <li> <p>3D point cloud semantic segmentation (<code>3DPointCloudSemanticSegmentation</code>), and adjustment and verification (<code>Adjustment3DPointCloudSemanticSegmentation</code>) labeling jobs for this task type. </p> </li> <li> <p>3D point cloud object tracking (<code>3DPointCloudObjectTracking</code>), and adjustment and verification (<code>Adjustment3DPointCloudObjectTracking</code>) labeling jobs for this task type. </p> </li> </ul> </li> </ul> <p/> <important> <p>If you are creating an adjustment or verification labeling job, you must use a <i>different</i> <code>LabelAttributeName</code> than the one used in the original labeling job. The original labeling job is the Ground Truth labeling job that produced the labels that you want verified or adjusted. To learn more about adjustment and verification labeling jobs, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html">Verify and Adjust Labels</a>.</p> </important>"""
    input_config: NotRequired[
        "capo_sagemaker.types.labeling_job_input_config.LabelingJobInputConfig"
    ]
    """<p>Input data for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.</p> <p>You must specify at least one of the following: <code>S3DataSource</code> or <code>SnsDataSource</code>. </p> <ul> <li> <p>Use <code>SnsDataSource</code> to specify an SNS input topic for a streaming labeling job. If you do not specify and SNS input topic ARN, Ground Truth will create a one-time labeling job that stops after all data objects in the input manifest file have been labeled.</p> </li> <li> <p>Use <code>S3DataSource</code> to specify an input manifest file for both streaming and one-time labeling jobs. Adding an <code>S3DataSource</code> is optional if you use <code>SnsDataSource</code> to create a streaming labeling job.</p> </li> </ul> <p>If you use the Amazon Mechanical Turk workforce, your input data should not include confidential information, personal information or protected health information. Use <code>ContentClassifiers</code> to specify that your data is free of personally identifiable information and adult content.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.labeling_job_output_config.LabelingJobOutputConfig"
    ]
    """<p>The location of the output data and the Amazon Web Services Key Management Service key ID for the key used to encrypt the output data, if any.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete data labeling.</p>"""
    label_category_config_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI of the file, referred to as a <i>label category configuration file</i>, that defines the categories used to label the data objects.</p> <p>For 3D point cloud and video frame task types, you can add label category attributes and frame attributes to your label category configuration file. To learn how, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-label-category-config.html">Create a Labeling Category Configuration File for 3D Point Cloud Labeling Jobs</a>. </p> <p>For named entity recognition jobs, in addition to <code>"labels"</code>, you must provide worker instructions in the label category configuration file using the <code>"instructions"</code> parameter: <code>"instructions": {"shortInstruction":"&lt;h1&gt;Add header&lt;/h1&gt;&lt;p&gt;Add Instructions&lt;/p&gt;", "fullInstruction":"&lt;p&gt;Add additional instructions.&lt;/p&gt;"}</code>. For details and an example, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-named-entity-recg.html#sms-creating-ner-api">Create a Named Entity Recognition Labeling Job (API) </a>.</p> <p>For all other <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html">built-in task types</a> and <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates.html">custom tasks</a>, your label category configuration file must be a JSON file in the following format. Identify the labels you want to use by replacing <code>label_1</code>, <code>label_2</code>,<code>...</code>,<code>label_n</code> with your label categories.</p> <p> <code>{ </code> </p> <p> <code>"document-version": "2018-11-28",</code> </p> <p> <code>"labels": [{"label": "label_1"},{"label": "label_2"},...{"label": "label_n"}]</code> </p> <p> <code>}</code> </p> <p>Note the following about the label category configuration file:</p> <ul> <li> <p>For image classification and text classification (single and multi-label) you must specify at least two label categories. For all other task types, the minimum number of label categories required is one. </p> </li> <li> <p>Each label category must be unique, you cannot specify duplicate label categories.</p> </li> <li> <p>If you create a 3D point cloud or video frame adjustment or verification labeling job, you must include <code>auditLabelAttributeName</code> in the label category configuration. Use this parameter to enter the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html#sagemaker-CreateLabelingJob-request-LabelAttributeName"> <code>LabelAttributeName</code> </a> of the labeling job you want to adjust or verify annotations of.</p> </li> </ul>"""
    stopping_conditions: NotRequired[
        "capo_sagemaker.types.labeling_job_stopping_conditions.LabelingJobStoppingConditions"
    ]
    """<p>A set of conditions for stopping the labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.</p>"""
    labeling_job_algorithms_config: NotRequired[
        "capo_sagemaker.types.labeling_job_algorithms_config.LabelingJobAlgorithmsConfig"
    ]
    """<p>Configures the information required to perform automated data labeling.</p>"""
    human_task_config: NotRequired[
        "capo_sagemaker.types.human_task_config.HumanTaskConfig"
    ]
    """<p>Configures the labeling task and how it is presented to workers; including, but not limited to price, keywords, and batch size (task count).</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key/value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLabelingJobRequest) -> dict:
    out: dict = {}
    if "labeling_job_name" in value:
        out["LabelingJobName"] = value["labeling_job_name"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLabelingJobRequest:
    out: CreateLabelingJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelingJobName") is not None:
        out["labeling_job_name"] = data["LabelingJobName"]
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
    return out
