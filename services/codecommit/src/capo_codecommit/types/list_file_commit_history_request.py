"""Generated from Smithy shape ``com.amazonaws.codecommit#ListFileCommitHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.limit
    import capo_codecommit.types.next_token
    import capo_codecommit.types.path
    import capo_codecommit.types.repository_name


class ListFileCommitHistoryRequest(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the file.</p>"""
    commit_specifier: NotRequired["capo_codecommit.types.commit_name.CommitName"]
    """<p>The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as <code>refs/heads/main</code>. If none is provided, the head commit is used.</p>"""
    file_path: "capo_codecommit.types.path.Path"
    """<p>The full path of the file whose history you want to retrieve, including the name of the file.</p>"""
    max_results: NotRequired["capo_codecommit.types.limit.Limit"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileCommitHistoryRequest) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "commit_specifier" in value:
        out["commitSpecifier"] = value["commit_specifier"]
    out["filePath"] = value["file_path"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileCommitHistoryRequest:
    out: ListFileCommitHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("commitSpecifier") is not None:
        out["commit_specifier"] = data["commitSpecifier"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
