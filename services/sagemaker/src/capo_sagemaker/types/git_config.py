"""Generated from Smithy shape ``com.amazonaws.sagemaker#GitConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.branch
    import capo_sagemaker.types.git_config_url
    import capo_sagemaker.types.secret_arn


class GitConfig(TypedDict, closed=True):
    repository_url: NotRequired["capo_sagemaker.types.git_config_url.GitConfigUrl"]
    """<p>The URL where the Git repository is located.</p>"""
    branch: NotRequired["capo_sagemaker.types.branch.Branch"]
    """<p>The default branch for the Git repository.</p>"""
    secret_arn: NotRequired["capo_sagemaker.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of <code>AWSCURRENT</code> and must be in the following format:</p> <p> <code>{"username": <i>UserName</i>, "password": <i>Password</i>}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitConfig) -> dict:
    out: dict = {}
    if "repository_url" in value:
        out["RepositoryUrl"] = value["repository_url"]
    if "branch" in value:
        out["Branch"] = value["branch"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GitConfig:
    out: GitConfig = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryUrl") is not None:
        out["repository_url"] = data["RepositoryUrl"]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    return out
