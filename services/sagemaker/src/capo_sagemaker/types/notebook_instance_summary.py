"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_code_repository_names_or_urls
    import capo_sagemaker.types.code_repository_name_or_url
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.instance_type
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.notebook_instance_arn
    import capo_sagemaker.types.notebook_instance_lifecycle_config_name
    import capo_sagemaker.types.notebook_instance_name
    import capo_sagemaker.types.notebook_instance_status
    import capo_sagemaker.types.notebook_instance_url


class NotebookInstanceSummary(TypedDict, closed=True):
    notebook_instance_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the notebook instance that you want a summary for.</p>"""
    notebook_instance_arn: NotRequired[
        "capo_sagemaker.types.notebook_instance_arn.NotebookInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the notebook instance.</p>"""
    notebook_instance_status: NotRequired[
        "capo_sagemaker.types.notebook_instance_status.NotebookInstanceStatus"
    ]
    """<p>The status of the notebook instance.</p>"""
    url: NotRequired["capo_sagemaker.types.notebook_instance_url.NotebookInstanceUrl"]
    """<p>The URL that you use to connect to the Jupyter notebook running in your notebook instance. </p>"""
    instance_type: NotRequired["capo_sagemaker.types.instance_type.InstanceType"]
    """<p>The type of ML compute instance that the notebook instance is running on.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that shows when the notebook instance was created.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp that shows when the notebook instance was last modified.</p>"""
    notebook_instance_lifecycle_config_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>The name of a notebook instance lifecycle configuration associated with this notebook instance.</p> <p>For information about notebook instance lifestyle configurations, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html">Step 2.1: (Optional) Customize a Notebook Instance</a>.</p>"""
    default_code_repository: NotRequired[
        "capo_sagemaker.types.code_repository_name_or_url.CodeRepositoryNameOrUrl"
    ]
    """<p>The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html">Amazon Web Services CodeCommit</a> or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    additional_code_repositories: NotRequired[
        "capo_sagemaker.types.additional_code_repository_names_or_urls.AdditionalCodeRepositoryNamesOrUrls"
    ]
    """<p>An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html">Amazon Web Services CodeCommit</a> or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceSummary) -> dict:
    out: dict = {}
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    if "notebook_instance_arn" in value:
        out["NotebookInstanceArn"] = value["notebook_instance_arn"]
    if "notebook_instance_status" in value:
        import capo_sagemaker.types.notebook_instance_status

        out["NotebookInstanceStatus"] = (
            capo_sagemaker.types.notebook_instance_status.serialize_aws_json_1_1(
                value["notebook_instance_status"]
            )
        )
    if "url" in value:
        out["Url"] = value["url"]
    if "instance_type" in value:
        import capo_sagemaker.types.instance_type

        out["InstanceType"] = capo_sagemaker.types.instance_type.serialize_aws_json_1_1(
            value["instance_type"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    if "default_code_repository" in value:
        out["DefaultCodeRepository"] = value["default_code_repository"]
    if "additional_code_repositories" in value:
        import capo_sagemaker.types.additional_code_repository_names_or_urls

        out["AdditionalCodeRepositories"] = (
            capo_sagemaker.types.additional_code_repository_names_or_urls.serialize_aws_json_1_1(
                value["additional_code_repositories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookInstanceSummary:
    out: NotebookInstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("NotebookInstanceName") is not None:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    if data.get("NotebookInstanceArn") is not None:
        out["notebook_instance_arn"] = data["NotebookInstanceArn"]
    if data.get("NotebookInstanceStatus") is not None:
        import capo_sagemaker.types.notebook_instance_status

        out["notebook_instance_status"] = (
            capo_sagemaker.types.notebook_instance_status.deserialize_aws_json_1_1(
                data["NotebookInstanceStatus"]
            )
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.instance_type

        out["instance_type"] = (
            capo_sagemaker.types.instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("NotebookInstanceLifecycleConfigName") is not None:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    if data.get("DefaultCodeRepository") is not None:
        out["default_code_repository"] = data["DefaultCodeRepository"]
    if data.get("AdditionalCodeRepositories") is not None:
        import capo_sagemaker.types.additional_code_repository_names_or_urls

        out["additional_code_repositories"] = (
            capo_sagemaker.types.additional_code_repository_names_or_urls.deserialize_aws_json_1_1(
                data["AdditionalCodeRepositories"]
            )
        )
    return out
