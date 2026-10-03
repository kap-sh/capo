"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateCodeRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.git_config_for_update


class UpdateCodeRepositoryInput(TypedDict, closed=True):
    code_repository_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the Git repository to update.</p>"""
    git_config: NotRequired[
        "capo_sagemaker.types.git_config_for_update.GitConfigForUpdate"
    ]
    """<p>The configuration of the git repository, including the URL and the Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the repository. The secret must have a staging label of <code>AWSCURRENT</code> and must be in the following format:</p> <p> <code>{"username": <i>UserName</i>, "password": <i>Password</i>}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCodeRepositoryInput) -> dict:
    out: dict = {}
    if "code_repository_name" in value:
        out["CodeRepositoryName"] = value["code_repository_name"]
    if "git_config" in value:
        import capo_sagemaker.types.git_config_for_update

        out["GitConfig"] = (
            capo_sagemaker.types.git_config_for_update.serialize_aws_json_1_1(
                value["git_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCodeRepositoryInput:
    out: UpdateCodeRepositoryInput = {}  # type: ignore[typeddict-item]
    if data.get("CodeRepositoryName") is not None:
        out["code_repository_name"] = data["CodeRepositoryName"]
    if data.get("GitConfig") is not None:
        import capo_sagemaker.types.git_config_for_update

        out["git_config"] = (
            capo_sagemaker.types.git_config_for_update.deserialize_aws_json_1_1(
                data["GitConfig"]
            )
        )
    return out
