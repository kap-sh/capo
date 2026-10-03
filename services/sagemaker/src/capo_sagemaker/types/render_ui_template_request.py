"""Generated from Smithy shape ``com.amazonaws.sagemaker#RenderUiTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.human_task_ui_arn
    import capo_sagemaker.types.renderable_task
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.ui_template


class RenderUiTemplateRequest(TypedDict, closed=True):
    ui_template: NotRequired["capo_sagemaker.types.ui_template.UiTemplate"]
    """<p>A <code>Template</code> object containing the worker UI template to render.</p>"""
    task: NotRequired["capo_sagemaker.types.renderable_task.RenderableTask"]
    """<p>A <code>RenderableTask</code> object containing a representative task to render.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that has access to the S3 objects that are used by the template.</p>"""
    human_task_ui_arn: NotRequired[
        "capo_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
    ]
    """<p>The <code>HumanTaskUiArn</code> of the worker UI that you want to render. Do not provide a <code>HumanTaskUiArn</code> if you use the <code>UiTemplate</code> parameter.</p> <p>See a list of available Human Ui Amazon Resource Names (ARNs) in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UiConfig.html">UiConfig</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenderUiTemplateRequest) -> dict:
    out: dict = {}
    if "ui_template" in value:
        import capo_sagemaker.types.ui_template

        out["UiTemplate"] = capo_sagemaker.types.ui_template.serialize_aws_json_1_1(
            value["ui_template"]
        )
    if "task" in value:
        import capo_sagemaker.types.renderable_task

        out["Task"] = capo_sagemaker.types.renderable_task.serialize_aws_json_1_1(
            value["task"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "human_task_ui_arn" in value:
        out["HumanTaskUiArn"] = value["human_task_ui_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RenderUiTemplateRequest:
    out: RenderUiTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("UiTemplate") is not None:
        import capo_sagemaker.types.ui_template

        out["ui_template"] = capo_sagemaker.types.ui_template.deserialize_aws_json_1_1(
            data["UiTemplate"]
        )
    if data.get("Task") is not None:
        import capo_sagemaker.types.renderable_task

        out["task"] = capo_sagemaker.types.renderable_task.deserialize_aws_json_1_1(
            data["Task"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("HumanTaskUiArn") is not None:
        out["human_task_ui_arn"] = data["HumanTaskUiArn"]
    return out
