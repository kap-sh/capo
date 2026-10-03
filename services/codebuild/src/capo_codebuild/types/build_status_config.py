"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildStatusConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class BuildStatusConfig(TypedDict, closed=True):
    context: NotRequired["capo_codebuild.types.string.String"]
    """<p>Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.</p> <dl> <dt>Bitbucket</dt> <dd> <p>This parameter is used for the <code>name</code> parameter in the Bitbucket commit status. For more information, see <a href="https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build">build</a> in the Bitbucket API documentation.</p> </dd> <dt>GitHub/GitHub Enterprise Server</dt> <dd> <p>This parameter is used for the <code>context</code> parameter in the GitHub commit status. For more information, see <a href="https://developer.github.com/v3/repos/statuses/#create-a-commit-status">Create a commit status</a> in the GitHub developer guide.</p> </dd> </dl>"""
    target_url: NotRequired["capo_codebuild.types.string.String"]
    """<p>Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.</p> <dl> <dt>Bitbucket</dt> <dd> <p>This parameter is used for the <code>url</code> parameter in the Bitbucket commit status. For more information, see <a href="https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build">build</a> in the Bitbucket API documentation.</p> </dd> <dt>GitHub/GitHub Enterprise Server</dt> <dd> <p>This parameter is used for the <code>target_url</code> parameter in the GitHub commit status. For more information, see <a href="https://developer.github.com/v3/repos/statuses/#create-a-commit-status">Create a commit status</a> in the GitHub developer guide.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildStatusConfig) -> dict:
    out: dict = {}
    if "context" in value:
        out["context"] = value["context"]
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildStatusConfig:
    out: BuildStatusConfig = {}  # type: ignore[typeddict-item]
    if data.get("context") is not None:
        out["context"] = data["context"]
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    return out
