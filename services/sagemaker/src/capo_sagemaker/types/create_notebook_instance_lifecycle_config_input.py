"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateNotebookInstanceLifecycleConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_list
    import capo_sagemaker.types.notebook_instance_lifecycle_config_name
    import capo_sagemaker.types.tag_list


class CreateNotebookInstanceLifecycleConfigInput(TypedDict, closed=True):
    notebook_instance_lifecycle_config_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>The name of the lifecycle configuration.</p>"""
    on_create: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_list.NotebookInstanceLifecycleConfigList"
    ]
    """<p>A shell script that runs only once, when you create a notebook instance. The shell script must be a base64-encoded string.</p>"""
    on_start: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_list.NotebookInstanceLifecycleConfigList"
    ]
    """<p>A shell script that runs every time you start a notebook instance, including when you create the notebook instance. The shell script must be a base64-encoded string.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotebookInstanceLifecycleConfigInput) -> dict:
    out: dict = {}
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    if "on_create" in value:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["OnCreate"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.serialize_aws_json_1_1(
                value["on_create"]
            )
        )
    if "on_start" in value:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["OnStart"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.serialize_aws_json_1_1(
                value["on_start"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotebookInstanceLifecycleConfigInput:
    out: CreateNotebookInstanceLifecycleConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("NotebookInstanceLifecycleConfigName") is not None:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    if data.get("OnCreate") is not None:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["on_create"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.deserialize_aws_json_1_1(
                data["OnCreate"]
            )
        )
    if data.get("OnStart") is not None:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["on_start"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.deserialize_aws_json_1_1(
                data["OnStart"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
