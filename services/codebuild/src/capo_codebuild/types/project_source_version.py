"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSourceVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.string


class ProjectSourceVersion(TypedDict, closed=True):
    source_identifier: "capo_codebuild.types.string.String"
    """<p>An identifier for a source in the build project. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length. </p>"""
    source_version: "capo_codebuild.types.string.String"
    """<p>The source version for the corresponding source identifier. If specified, must be one of:</p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example, <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For GitLab: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul> <p> For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSourceVersion) -> dict:
    out: dict = {}
    out["sourceIdentifier"] = value["source_identifier"]
    out["sourceVersion"] = value["source_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectSourceVersion:
    out: ProjectSourceVersion = {}  # type: ignore[typeddict-item]
    if data.get("sourceIdentifier") is not None:
        out["source_identifier"] = data["sourceIdentifier"]
    else:
        raise DeserializationError("ProjectSourceVersion.source_identifier required")
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    else:
        raise DeserializationError("ProjectSourceVersion.source_version required")
    return out
