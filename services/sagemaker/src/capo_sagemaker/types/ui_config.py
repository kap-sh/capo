"""Generated from Smithy shape ``com.amazonaws.sagemaker#UiConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.human_task_ui_arn
    import capo_sagemaker.types.s3_uri


class UiConfig(TypedDict, closed=True):
    ui_template_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 bucket location of the UI template, or worker task template. This is the template used to render the worker UI and tools for labeling job tasks. For more information about the contents of a UI template, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2.html"> Creating Your Custom Labeling Task Template</a>.</p>"""
    human_task_ui_arn: NotRequired[
        "capo_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
    ]
    """<p>The ARN of the worker task template used to render the worker UI and tools for labeling job tasks.</p> <p>Use this parameter when you are creating a labeling job for named entity recognition, 3D point cloud and video frame labeling jobs. Use your labeling job task type to select one of the following ARNs and use it with this parameter when you create a labeling job. Replace <code>aws-region</code> with the Amazon Web Services Region you are creating your labeling job in. For example, replace <code>aws-region</code> with <code>us-west-1</code> if you create a labeling job in US West (N. California).</p> <p> <b>Named Entity Recognition</b> </p> <p>Use the following <code>HumanTaskUiArn</code> for named entity recognition labeling jobs:</p> <p> <code>arn:aws:sagemaker:aws-region:394669845002:human-task-ui/NamedEntityRecognition</code> </p> <p> <b>3D Point Cloud HumanTaskUiArns</b> </p> <p>Use this <code>HumanTaskUiArn</code> for 3D point cloud object detection and 3D point cloud object detection adjustment labeling jobs. </p> <ul> <li> <p> <code>arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudObjectDetection</code> </p> </li> </ul> <p> Use this <code>HumanTaskUiArn</code> for 3D point cloud object tracking and 3D point cloud object tracking adjustment labeling jobs. </p> <ul> <li> <p> <code>arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudObjectTracking</code> </p> </li> </ul> <p> Use this <code>HumanTaskUiArn</code> for 3D point cloud semantic segmentation and 3D point cloud semantic segmentation adjustment labeling jobs.</p> <ul> <li> <p> <code>arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudSemanticSegmentation</code> </p> </li> </ul> <p> <b>Video Frame HumanTaskUiArns</b> </p> <p>Use this <code>HumanTaskUiArn</code> for video frame object detection and video frame object detection adjustment labeling jobs. </p> <ul> <li> <p> <code>arn:aws:sagemaker:region:394669845002:human-task-ui/VideoObjectDetection</code> </p> </li> </ul> <p> Use this <code>HumanTaskUiArn</code> for video frame object tracking and video frame object tracking adjustment labeling jobs. </p> <ul> <li> <p> <code>arn:aws:sagemaker:aws-region:394669845002:human-task-ui/VideoObjectTracking</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UiConfig) -> dict:
    out: dict = {}
    if "ui_template_s3_uri" in value:
        out["UiTemplateS3Uri"] = value["ui_template_s3_uri"]
    if "human_task_ui_arn" in value:
        out["HumanTaskUiArn"] = value["human_task_ui_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UiConfig:
    out: UiConfig = {}  # type: ignore[typeddict-item]
    if data.get("UiTemplateS3Uri") is not None:
        out["ui_template_s3_uri"] = data["UiTemplateS3Uri"]
    if data.get("HumanTaskUiArn") is not None:
        out["human_task_ui_arn"] = data["HumanTaskUiArn"]
    return out
